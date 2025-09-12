from pydantic import BaseModel
from db import Base, Mapped, mapped_column

class Sentence(Base):
    __tablename__ = "sentences"

    text: Mapped[str] = mapped_column()
    additional: Mapped[str] = mapped_column()

class SentenceSchema(BaseModel):
    text: str
    additional: str
