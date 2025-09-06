from faststream.rabbit import RabbitBroker
from faststream.rabbit.fastapi import RabbitRouter
from pydantic import BaseModel
from enum import Enum
from core.config import settings

class Queue(str, Enum):
    admin = "admin"

class MessageSchema(BaseModel):
    chat_id: int
    text: str

broker = RabbitBroker(url=settings.rabbit.url)

router = RabbitRouter(url=settings.rabbit.url)
