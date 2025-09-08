from fastapi import APIRouter
from api.v1.auth import router as auth_router
from api.v1.user import router as user_router
from api.v1.lesson import router as lesson_router

router = APIRouter()

router.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
router.include_router(user_router, prefix="/api/v1/user", tags=["User"])
router.include_router(lesson_router, prefix="/api/v1/lesson", tags=["Lesson"])
