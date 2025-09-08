from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from db import SessionDep, select
from db.user import User
from db.lesson import Lesson

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(
    request: Request,
    db: SessionDep,
):
    users = (await db.scalars(select(User))).all()
    lessons = (await db.scalars(select(Lesson).order_by(Lesson.position.asc(), Lesson.id.asc()))).all()

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "users": users,
            "lessons": lessons,
        }
    )
