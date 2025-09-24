from pydantic import BaseModel
from db import Base, Mapped, mapped_column

class Article(Base):
    __tablename__ = "articles"

    title: Mapped[str] = mapped_column()
    data: Mapped[str] = mapped_column()
    cid: Mapped[int] = mapped_column() # category id

class ArticleSchema(BaseModel):
    title: str
    data: str
    cid: int
