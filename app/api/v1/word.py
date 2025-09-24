from fastapi import APIRouter, HTTPException, UploadFile, Depends
from core.security import JWTBearer

router = APIRouter(dependencies=[Depends(JWTBearer())])

@router.post("/txt")
async def upload_txt(file: UploadFile):
    if not file.filename.endswith(".txt"):
        raise HTTPException(400, "only .txt files are allowed")

    with open("static/words.txt", "wb") as f:
        f.write(await file.read())

    return {"filename": file.filename}

@router.delete("/txt")
async def delete_txt():
    with open("static/words.txt", "w", encoding="utf-8") as f:
        f.write("")

    return {"message": "words deleted"}
