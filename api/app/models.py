from pydantic import BaseModel
from enum import Enum

class InKafkaMessage(BaseModel):
    topic: str | None = None
    value: str | bytes = None
    key: str | bytes = None
    partition: int | None = None

class KafkaMessage(BaseModel):
    topic: str | None = "logs"
    value: str | bytes = None
    key: str | bytes = None
    partition: int | None = None

class OutKafkaMessage(BaseModel):
    result: str | bytes = None
    timestamp: int | None = None
