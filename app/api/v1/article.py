from fastapi import APIRouter, HTTPException, Depends
from core.security import JWTBearer
from db import SessionDep, select
from db.article import Article, ArticleSchema

router = APIRouter(dependencies=[Depends(JWTBearer())])

@router.post("/")
async def add_article(
    body: ArticleSchema,
    db: SessionDep,
):
    # category = await db.scalar(select(Article).filter_by(id=body.cid))
    # if not category:
    #     raise HTTPException(404, "category not found")

    article = Article(
        title=body.title,
        data=body.data,
        cid=body.cid,
    )
    db.add(article)
    await db.commit()

    return {"message": "article added"}

@router.patch("/")
async def edit_article(
    id: int,
    body: ArticleSchema,
    db: SessionDep,
):
    article = await db.scalar(select(Article).filter_by(id=id))
    if not article:
        raise HTTPException(404, "article not found")

    # category = await db.scalar(select(Article).filter_by(id=body.cid))
    # if not category:
    #     raise HTTPException(404, "category not found")

    article.title = body.title
    article.data = body.data
    article.cid = body.cid
    await db.commit()

    return {"message": "article updated"}

@router.delete("/")
async def delete_article(
    id: int,
    db: SessionDep,
):
    article = await db.scalar(select(Article).filter_by(id=id))
    if not article:
        raise HTTPException(404, "article not found")

    await db.delete(article)
    await db.commit()

    return {"message": "article deleted"}
