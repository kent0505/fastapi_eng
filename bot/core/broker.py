from faststream.rabbit import RabbitBroker
from enum import Enum
from core.config import settings

class Queue(str, Enum):
    admin = "admin"

broker = RabbitBroker(url=settings.rabbit.url)
