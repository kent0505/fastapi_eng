from fastapi import APIRouter, HTTPException, Depends
from core.security import JWTBearer
from db import SessionDep, select
from db.sentence import Sentence, SentenceSchema

router = APIRouter(dependencies=[Depends(JWTBearer())])

@router.post("/")
async def add_sentence(
    body: SentenceSchema,
    db: SessionDep,
):
    sentence = Sentence(
        text=body.text,
        additional=body.additional,
    )
    db.add(sentence)
    await db.commit()

    return {"message": "sentence added"}

@router.put("/")
async def edit_sentence(
    id: int,
    body: SentenceSchema,
    db: SessionDep,
):
    sentence = await db.scalar(select(Sentence).filter_by(id=id))
    if not sentence:
        raise HTTPException(404, "sentence not found")

    sentence.text = body.text
    sentence.additional = body.additional
    await db.commit()

    return {"message": "sentence updated"}

@router.delete("/")
async def delete_sentence(
    id: int,
    db: SessionDep,
):
    sentence = await db.scalar(select(Sentence).filter_by(id=id))
    if not sentence:
        raise HTTPException(404, "sentence not found")

    await db.delete(sentence)
    await db.commit()

    return {"message": "sentence deleted"}
