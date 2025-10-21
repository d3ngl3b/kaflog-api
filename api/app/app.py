from fastapi import FastAPI
from pydantic import BaseModel

from .kafka_writer import BasicWriter, MessageWriter
from .models import KafkaMessage

import logging
import os

app = FastAPI()
writer: MessageWriter = BasicWriter()

logging.basicConfig(
    format=("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
    level=logging.INFO,
    filename='app/logs/api.log',
    filemode='w'
)

logging.getLogger("httpx").setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)

@app.post('/produce/')
async def produce_message(message: KafkaMessage):
    logger.info("Produce message endpoint triggered.")
    return writer.send_message(message=message)