from pydantic import BaseModel
from db import Base, Mapped, mapped_column

class Question(Base):
    __tablename__ = "questions"

    title: Mapped[str] = mapped_column()
    lid: Mapped[int] = mapped_column() # lesson id

class QuestionSchema(BaseModel):
    title: str
    lid: int
