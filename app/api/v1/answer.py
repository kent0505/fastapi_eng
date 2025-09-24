from fastapi import APIRouter, HTTPException, Depends
from core.security import JWTBearer
from db import SessionDep, select, update
from db.question import Question
from db.answer import Answer, AnswerSchema

router = APIRouter(dependencies=[Depends(JWTBearer())])

@router.post("/")
async def add_answer(
    qid: int,
    body: AnswerSchema,
    db: SessionDep,
):
    question = await db.scalar(select(Question).filter_by(id=qid))
    if not question:
        raise HTTPException(404, "question not found")

    answer = Answer(
        title=body.title,
        qid=qid,
    )
    db.add(answer)
    await db.commit()

    return {"message": "answer added"}

@router.put("/")
async def edit_answer(
    id: int,
    body: AnswerSchema,
    db: SessionDep,
):
    answer = await db.scalar(select(Answer).filter_by(id=id))
    if not answer:
        raise HTTPException(404, "answer not found")

    answer.title = body.title
    await db.commit()

    return {"message": "answer updated"}

@router.patch("/")
async def edit_correct_answer(
    id: int,
    db: SessionDep,
):
    answer = await db.scalar(select(Answer).filter_by(id=id))
    if not answer:
        raise HTTPException(404, "answer not found")

    await db.execute(
        update(Answer)
        .where(Answer.qid == answer.qid)
        .values(correct=0)
    )
    answer.correct = 1
    await db.commit()

    return {"message": "answer updated"}

@router.delete("/")
async def delete_answer(
    id: int,
    db: SessionDep,
):
    answer = await db.scalar(select(Answer).filter_by(id=id))
    if not answer:
        raise HTTPException(404, "answer not found")

    await db.delete(answer)
    await db.commit()

    return {"message": "answer deleted"}
