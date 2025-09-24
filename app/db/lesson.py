from pydantic import BaseModel
from db import Base, Mapped, Float, mapped_column

class Lesson(Base):
    __tablename__ = "lessons"

    title: Mapped[str] = mapped_column()
    data: Mapped[str] = mapped_column()
    position: Mapped[int] = mapped_column(Float, default=0)

class LessonSchema(BaseModel):
    title: str
    data: str
