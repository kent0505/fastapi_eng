from pydantic import BaseModel
from db import Base, Mapped, mapped_column

class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    age: Mapped[str] = mapped_column(nullable=True)
    photo: Mapped[str] = mapped_column(nullable=True)
    role: Mapped[str] = mapped_column() # admin, user
    lesson: Mapped[int] = mapped_column(default=1)
    paid: Mapped[int] = mapped_column(default=0)
    activities: Mapped[int] = mapped_column(default=0)

class LoginSchema(BaseModel):
    username: str
    password: str

class UserUpdateSchema(BaseModel):
    username: str
    age: str

class UserPasswordSchema(BaseModel):
    password: str
    new_password: str
