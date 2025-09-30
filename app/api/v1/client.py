from fastapi import APIRouter, Response, Depends
from core.security import verify_api_key
from db import SessionDep, select
from db.lesson import Lesson
from db.question import Question
from db.answer import Answer
from db.sentence import Sentence
from db.article import Article

router = APIRouter(dependencies=[Depends(verify_api_key)])

@router.get("/lessons")
async def get_lessons(db: SessionDep):
    lessons = (await db.scalars(select(Lesson).order_by(Lesson.position.asc()))).all()

    return {"lessons": lessons}

@router.get("/questions")
async def get_questions(db: SessionDep):
    questions = (await db.scalars(select(Question))).all()

    return {"questions": questions}

@router.get("/answers")
async def get_answers(db: SessionDep):
    answers = (await db.scalars(select(Answer))).all()

    return {"answers": answers}

@router.get("/words")
async def get_words():
    with open("static/words.txt", "r", encoding="utf-8") as f:
        content = f.read()

    return Response(content=content, media_type="text/plain")

@router.get("/sentences")
async def get_sentences(db: SessionDep):
    sentences = (await db.scalars(select(Sentence))).all()

    return {"sentences": sentences}

@router.get("/articles")
async def get_articles(db: SessionDep):
    articles = (await db.scalars(select(Article))).all()

    return {"articles": articles}
