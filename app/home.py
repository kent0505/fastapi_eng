from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from db import SessionDep, select
from db.user import User
from db.lesson import Lesson
from db.question import Question
from db.answer import Answer
from db.sentence import Sentence
from db.article import Article

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(
    request: Request,
    db: SessionDep,
):
    users = (await db.scalars(select(User))).all()
    lessons = (await db.scalars(select(Lesson).order_by(Lesson.position.asc()))).all()
    questions = (await db.scalars(select(Question))).all()
    answers = (await db.scalars(select(Answer))).all()
    sentences = (await db.scalars(select(Sentence))).all()
    articles = (await db.scalars(select(Article))).all()

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "users": users,
            "lessons": lessons,
            "questions": questions,
            "answers": answers,
            "sentences": sentences,
            "articles": articles,
        }
    )
