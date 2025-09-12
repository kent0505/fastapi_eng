from fastapi import APIRouter, HTTPException, Depends
from core.security import JWTBearer, Roles, UserDep
from db import SessionDep, select
from db.user import User

router = APIRouter(dependencies=[Depends(JWTBearer())])

@router.patch("/")
async def update_role(
    admin: UserDep,
    id: int,
    role: Roles,
    db: SessionDep,
):
    user = await db.scalar(select(User).filter_by(id=id))
    if not user:
        raise HTTPException(404, "user not found")

    if admin == id:
        raise HTTPException(409, "admin can't change own role")

    user.role = role.value
    await db.commit()

    return {"message": "user role updated"}
