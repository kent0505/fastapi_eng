from fastapi import APIRouter, Depends
from core.security import JWTBearer, Roles
from db import SessionDep, select
from db.lesson import Lesson
from db.word import Word

router = APIRouter(dependencies=[Depends(JWTBearer(role=Roles.user))])

@router.get("/lessons")
async def get_lessons(db: SessionDep):
    lessons = (await db.scalars(select(Lesson).order_by(Lesson.position.asc()))).all()

    return {"lessons": lessons}

@router.get("/words")
async def get_words(db: SessionDep):
    words = (await db.scalars(select(Word))).all()

    return {"words": words}
