from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from db import SessionDep, select
from db.user import User
from db.lesson import Lesson
from db.word import Word
from db.sentence import Sentence

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(
    request: Request,
    db: SessionDep,
):
    users = (await db.scalars(select(User))).all()
    lessons = (await db.scalars(select(Lesson).order_by(Lesson.position.asc()))).all()
    words = (await db.scalars(select(Word))).all()
    sentences = (await db.scalars(select(Sentence))).all()

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "users": users,
            "lessons": lessons,
            "words": words,
            "sentences": sentences,
        }
    )
