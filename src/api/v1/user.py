from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def get_users():
    return {"message": "hello"}
