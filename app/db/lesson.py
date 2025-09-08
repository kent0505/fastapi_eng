from pydantic import BaseModel
from db import Base, Mapped, mapped_column

class Lesson(Base):
    __tablename__ = "lessons"

    title: Mapped[str] = mapped_column()
    body: Mapped[str] = mapped_column()
    position: Mapped[int] = mapped_column(nullable=True)

class LessonSchema(BaseModel):
    title: str
    body: str
