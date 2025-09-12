from pydantic import BaseModel
from db import Base, Mapped, mapped_column

class Word(Base):
    __tablename__ = "words"

    en: Mapped[str] = mapped_column()
    ru: Mapped[str] = mapped_column()

class WordSchema(BaseModel):
    en: str
    ru: str
