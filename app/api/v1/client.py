from fastapi import APIRouter, Depends
from core.security import JWTBearer, Roles
from db import SessionDep, select
from db.lesson import Lesson

router = APIRouter(dependencies=[Depends(JWTBearer(role=Roles.user))])

@router.get("/")
async def get_lessons(db: SessionDep):
    lessons = (await db.scalars(select(Lesson).order_by(Lesson.position.asc()))).all()

    return {"lessons": lessons}
