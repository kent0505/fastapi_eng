from fastapi import APIRouter, Depends
from core.security import JWTBearer, Roles
from core.utils import parse_words
from db import SessionDep, select
from db.lesson import Lesson
from db.word import Word
from db.sentence import Sentence

router = APIRouter(dependencies=[Depends(JWTBearer(role=Roles.user))])

@router.get("/lessons")
async def get_lessons(db: SessionDep):
    lessons = (await db.scalars(select(Lesson).order_by(Lesson.position.asc()))).all()

    return {"lessons": lessons}

@router.get("/words")
async def get_words(db: SessionDep):
    # words = (await db.scalars(select(Word))).all()
    words = parse_words("static/words.txt")

    return {"words": words}

@router.get("/sentences")
async def get_sentences(db: SessionDep):
    sentences = (await db.scalars(select(Sentence))).all()

    return {"sentences": sentences}
