from abc import ABC, abstractmethod

from confluent_kafka import Message
from datetime import datetime, timezone
import os
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, declarative_base

from .models import RawLogging, Base



class DbWriter(ABC):

    engine: Engine = create_engine(
        f'{os.getenv("DB_DRIVER", "postgresql+psycopg2")}://{os.getenv("DB_USER", "dev")}:{os.getenv("DB_PASSWORD", "password")}@{os.getenv("DB_HOSTNAME", "localhost")}/{os.getenv("DB_NAME", "loggingDB")}'
    )

    def __init__(self):
        Base.metadata.create_all(self.engine)


    @staticmethod
    def _get_time(timestamp: int) -> datetime:
        return datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc)

    @abstractmethod
    def write(self, msg: str):
        pass

class RawWriter(DbWriter):

    def write(self, msg: Message):
        with Session(self.engine) as session:
            new_message = RawLogging(
                topic=msg.topic(),
                value=msg.value().decode("utf-8"),
                date=self._get_time(msg.timestamp()[1])
            )
            session.add(new_message)
            session.commit()
