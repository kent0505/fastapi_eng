from fastapi import APIRouter, HTTPException
from core.security import signJWT, Roles
from core.utils import hash_password, check_password, get_timestamp
from core.config import settings
from db import SessionDep, select
from db.user import User, LoginSchema

router = APIRouter()

@router.post("/login")
async def login(
    body: LoginSchema,
    db: SessionDep,
):
    username = body.username.lower().strip()

    user = await db.scalar(select(User).filter_by(username=username))
    if not user:
        raise HTTPException(404, "user not found")

    if not check_password(body.password, user.password):
        raise HTTPException(401, "invalid credentials")

    access_token: str = signJWT(
        user.id, 
        user.role, 
        get_timestamp() + settings.jwt.exp,
    )

    return {
        "access_token": access_token,
        "role": user.role,
    }

@router.post("/register")
async def register(
    body: LoginSchema,
    db: SessionDep,
):
    username = body.username.lower().strip()

    user = await db.scalar(select(User).filter_by(username=username))
    if user:
        raise HTTPException(409, "user already exist")

    if body.password.__len__() < 5:
        raise HTTPException(422, "password must be at least 5 characters long")
    
    admin = await db.scalar(select(User).filter_by(role=Roles.admin.value))

    user = User(
        username=username,
        password=hash_password(body.password),
        role=Roles.admin.value if not admin else Roles.user.value,
    )
    db.add(user)
    await db.commit()

    return {"message": "user registered"}
