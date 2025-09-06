from pydantic import BaseModel
from db import Base, Mapped, mapped_column
from core.security import Roles

class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column(default=Roles.user.value) # admin, user

# class UserSchema(BaseModel):
#     phone: str
#     name: str
#     age: str

# class UserEditSchema(BaseModel):
#     name: str
#     age: str
#     fcm: str

# class AdminSchema(BaseModel):
#     name: str = "Otabek"
#     phone: str = "+998998472580"

# class PhoneSchema(BaseModel):
#     phone: str = "+998998472580"

class LoginSchema(BaseModel):
    username: str
    password: str
