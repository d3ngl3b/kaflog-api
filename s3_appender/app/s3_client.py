import uuid
from abc import ABC, abstractmethod
import boto3
from botocore.exceptions import ClientError
from confluent_kafka import Message
from collections import deque

import os

class Formatter(ABC):

    @abstractmethod
    def format(self, msg) -> str:
        pass

class Uploader(ABC):

    formatter: Formatter
    batch_size: int = 1
    queue: deque[str] = deque([])

    def _generate_filename(self) -> str:
        unique_name = uuid.uuid4().int >> 64  # take upper 64 bits for compactness
        return f"data_{unique_name}.txt"

    def upload_file(self, object_name=None):

        bucket = os.getenv("BUCKET")
        file_name = os.getenv("DATA_FILE_PATH")

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(self._generate_filename())

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            return False
        return True

    def write_queue(self):
        with open(os.getenv("DATA_FILE_PATH"), "a") as file:
            for _ in range(
                min(self.batch_size, len(self.queue))
            ):
                message = self.queue.popleft()
                file.write(
                    self.formatter.format(message)
                )

    def add(self, msg):

        self.queue.append(
            msg
        )

        if len(self.queue) == self.batch_size:
            self.write_queue()
            self.upload_file()

class RawFormatter(Formatter):

    def format(self, msg: Message) -> str:
        value = msg.value().decode("utf-8") if msg.value() else ""
        ts = msg.timestamp()[1] if msg.timestamp() else 0
        return f"{msg.topic()} | {value} | {ts}\n"

class RawUploader(Uploader):

    def __init__(self):
        self.formatter = RawFormatter()
