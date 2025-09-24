from pydantic import BaseModel
from db import Base, Mapped, mapped_column

class Answer(Base):
    __tablename__ = "answers"

    title: Mapped[str] = mapped_column()
    correct: Mapped[int] = mapped_column(default=0)
    qid: Mapped[int] = mapped_column() # question id

class AnswerSchema(BaseModel):
    title: str
