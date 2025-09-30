from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

import os

load_dotenv()

class Swagger(BaseModel):
    ui_parameters: dict = {"defaultModelsExpandDepth": -1}

class JWT(BaseModel):
    exp: int = 2629746 # one month
    key: str = os.getenv("KEY")
    algorithm: str = "HS256"
    admin: str = os.getenv("ADMIN")
    api_key: str = os.getenv("API_KEY")

class DB(BaseModel):
    url: str = os.getenv("POSTGRES_URL")

class Rabbit(BaseModel):
    url: str = os.getenv("RABBIT_URL")

class Settings(BaseSettings):
    swagger: Swagger = Swagger()
    jwt: JWT = JWT()
    db: DB = DB()
    rabbit: Rabbit = Rabbit()

settings = Settings()
