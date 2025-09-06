from fastapi import APIRouter, HTTPException
from core.security import signJWT
from core.utils import hash_password, check_password, get_timestamp
from core.config import settings
from db import select, SessionDep
from db.user import User, LoginSchema

router = APIRouter()

@router.post("/login")
async def login(
    body: LoginSchema,
    db: SessionDep,
):
    user = await db.scalar(select(User).filter_by(username=body.username))
    if user:
        if not check_password(
            body.password, 
            user.password,
        ):
            raise HTTPException(401, "invalid credentials")
    else:
        user = User(
            username=body.username,
            password=hash_password(body.password),
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

    access_token: str = signJWT(
        user.id, 
        user.role, 
        get_timestamp() + settings.jwt.exp,
    )

    return {
        "access_token": access_token,
        "role": user.role,
    }
