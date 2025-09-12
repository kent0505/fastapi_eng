from fastapi import APIRouter, HTTPException, Depends
from core.utils import check_password, hash_password
from core.security import JWTBearer, Roles, UserDep
from db import SessionDep, select
from db.user import User, UserUpdateSchema, UserPasswordSchema

router = APIRouter(dependencies=[Depends(JWTBearer(role=Roles.user))])

@router.get("/")
async def get_user(
    id: UserDep,
    db: SessionDep,
):
    user = await db.scalar(select(User).filter_by(id=id))
    if not user:
        raise HTTPException(404, "user not found")

    return {
        "user": {
            "id": user.id,
            "username": user.username,
            "age": user.age,
            "photo": user.photo,
            "role": user.role,
        }
    }

@router.put("/")
async def edit_user(
    id: UserDep,
    body: UserUpdateSchema,
    db: SessionDep,
):
    user = await db.scalar(select(User).filter_by(id=id))
    if not user:
        raise HTTPException(404, "user not found")
    
    username = body.username.lower().strip()

    if user.username != username:
        exists = await db.scalar(select(User).filter_by(username=username))
        if exists:
            raise HTTPException(409, "username already exist")

    user.username = username
    user.age = body.age
    await db.commit()

    return {"message": "user updated"}

@router.patch("/password")
async def edit_user_password(
    id: UserDep,
    body: UserPasswordSchema,
    db: SessionDep,
):
    user = await db.scalar(select(User).filter_by(id=id))
    if not user:
        raise HTTPException(404, "user not found")
    
    if not check_password(body.password, user.password):
        raise HTTPException(401, "invalid credentials")
    
    if body.new_password.__len__() < 5:
        raise HTTPException(422, "password must be at least 5 characters long")
    
    if body.password == body.new_password:
        raise HTTPException(422, "password must be different")

    user.password = hash_password(body.new_password)
    await db.commit()

    return {"message": "user password updated"}

# @router.patch("/photo")
# async def edit_user_photo(
#     id: UserDep,
#     db: SessionDep,
#     file: UploadFile = File(),
# ):
#     user = await db.scalar(select(User).filter_by(id=id))
#     if not user:
#         raise HTTPException(404, "user not found")

#     # photo = await s3_service.put_object(id, "users", file)

#     # user.photo = photo
#     # await db.commit()

#     return {"message": "user photo updated"}

@router.delete("/")
async def delete_user(
    id: UserDep,
    db: SessionDep,
):
    user = await db.scalar(select(User).filter_by(id=id))
    if not user:
        raise HTTPException(404, "user not found")
    
    await db.delete(user)
    await db.commit()

    return {"message": "user deleted"}
