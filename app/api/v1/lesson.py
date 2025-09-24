from fastapi import APIRouter, HTTPException, Depends
from core.security import JWTBearer
from db import SessionDep, select
from db.lesson import Lesson, LessonSchema

router = APIRouter(dependencies=[Depends(JWTBearer())])

@router.post("/")
async def add_lesson(
    body: LessonSchema,
    db: SessionDep,
):
    lesson = Lesson(
        title=body.title,
        data=body.data,
    )
    db.add(lesson)
    await db.commit()
    await db.refresh(lesson)

    lesson.position = lesson.id
    await db.commit()

    return {"message": "lesson added"}

@router.put("/")
async def edit_lesson(
    id: int,
    body: LessonSchema,
    db: SessionDep,
):
    lesson = await db.scalar(select(Lesson).filter_by(id=id))
    if not lesson:
        raise HTTPException(404, "lesson not found")

    lesson.title = body.title
    lesson.data = body.data
    await db.commit()

    return {"message": "lesson updated"}

@router.patch("/")
async def edit_lesson_position(
    id: int,
    position: float,
    db: SessionDep,
):
    lesson = await db.scalar(select(Lesson).filter_by(id=id))
    if not lesson:
        raise HTTPException(404, "lesson not found")

    lesson.position = position
    await db.commit()

    return {"message": "lesson position updated"}

@router.delete("/")
async def delete_lesson(
    id: int,
    db: SessionDep,
):
    lesson = await db.scalar(select(Lesson).filter_by(id=id))
    if not lesson:
        raise HTTPException(404, "lesson not found")

    await db.delete(lesson)
    await db.commit()

    return {"message": "lesson deleted"}
