from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

import os

load_dotenv()

class Bot(BaseModel):
    token: str = os.getenv("TOKEN")

class Rabbit(BaseModel):
    url: str = os.getenv("RABBIT_URL")

class Settings(BaseSettings):
    bot: Bot = Bot()
    rabbit: Rabbit = Rabbit()

settings = Settings()
