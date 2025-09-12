from fastapi import APIRouter
from api.v1.auth import router as auth_router
from api.v1.client import router as client_router
from api.v1.user import router as user_router
from api.v1.admin import router as admin_router
from api.v1.lesson import router as lesson_router
from api.v1.word import router as word_router
from api.v1.sentence import router as sentence_router

router = APIRouter()

router.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
router.include_router(client_router, prefix="/api/v1/client", tags=["Client"])
router.include_router(user_router, prefix="/api/v1/user", tags=["User"])
router.include_router(admin_router, prefix="/api/v1/admin", tags=["Admin"])
router.include_router(lesson_router, prefix="/api/v1/lesson", tags=["Lesson"])
router.include_router(word_router, prefix="/api/v1/word", tags=["Word"])
router.include_router(sentence_router, prefix="/api/v1/sentence", tags=["Sentence"])
