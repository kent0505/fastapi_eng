from fastapi import APIRouter, HTTPException, Depends
from core.security import JWTBearer
from db import SessionDep, select
from db.word import Word, WordSchema

router = APIRouter(dependencies=[Depends(JWTBearer())])

@router.post("/")
async def add_word(
    body: WordSchema,
    db: SessionDep,
):
    word = Word(
        en=body.en,
        ru=body.ru,
    )
    db.add(word)
    await db.commit()

    return {"message": "word added"}

@router.put("/")
async def edit_word(
    id: int,
    body: WordSchema,
    db: SessionDep,
):
    word = await db.scalar(select(Word).filter_by(id=id))
    if not word:
        raise HTTPException(404, "word not found")

    word.en = body.en
    word.ru = body.ru
    await db.commit()

    return {"message": "word updated"}

@router.delete("/")
async def delete_word(
    id: int,
    db: SessionDep,
):
    word = await db.scalar(select(Word).filter_by(id=id))
    if not word:
        raise HTTPException(404, "word not found")

    await db.delete(word)
    await db.commit()

    return {"message": "word deleted"}
