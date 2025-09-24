from fastapi import APIRouter, HTTPException, Depends
from core.security import JWTBearer
from db import SessionDep, select
from db.lesson import Lesson
from db.question import Question, QuestionSchema

router = APIRouter(dependencies=[Depends(JWTBearer())])

@router.post("/")
async def add_question(
    body: QuestionSchema,
    db: SessionDep,
):
    lesson = await db.scalar(select(Lesson).filter_by(id=body.lid))
    if not lesson:
        raise HTTPException(404, "lesson not found")

    question = Question(
        title=body.title,
        lid=body.lid,
    )
    db.add(question)
    await db.commit()

    return {"message": "question added"}

@router.patch("/")
async def edit_question(
    id: int,
    body: QuestionSchema,
    db: SessionDep,
):
    question = await db.scalar(select(Question).filter_by(id=id))
    if not question:
        raise HTTPException(404, "question not found")

    question.title = body.title
    # lid не меняется
    await db.commit()

    return {"message": "question updated"}

@router.delete("/")
async def delete_question(
    id: int,
    db: SessionDep,
):
    question = await db.scalar(select(Question).filter_by(id=id))
    if not question:
        raise HTTPException(404, "question not found")

    await db.delete(question)
    await db.commit()

    return {"message": "question deleted"}
