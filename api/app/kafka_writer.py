import time
import os
import socket
import sys

from confluent_kafka import Producer, KafkaError
from abc import ABC, abstractmethod

from fastapi_cli.cli import callback

from .models import KafkaMessage, OutKafkaMessage

BASIC_CONF = {
    'bootstrap.servers': os.getenv("BOOTSTRAP_SERVERS"),
    'client.id': socket.gethostname()
}

class KafkaProducer(ABC):
    @abstractmethod
    def send_message(self, message: KafkaMessage):
        pass

class MessageWriter(ABC):
    @abstractmethod
    def get_producer(self) -> KafkaProducer:
        pass

    # @abstractmethod
    # def callback(self, err, msg):
    #     pass

    def send_message(self, message: KafkaMessage):
        producer = self.get_producer()
        producer.send_message(message)

class BasicWriter(MessageWriter):

    def get_producer(self) -> KafkaProducer:
        return BasicKafkaProducer()

class BasicKafkaProducer(KafkaProducer):

    def send_message(self, message: KafkaMessage) -> OutKafkaMessage:
        result: OutKafkaMessage
        producer: Producer = Producer(BASIC_CONF)
        try:
            producer.produce(
                topic=message.topic,
                value=message.value,
                key=message.key,
                partition=message.partition
            )
            producer.flush()
            return OutKafkaMessage(
                result="SUCCESS",
                timestamp=int(time.time() * 1000)
            )

        except KafkaError as ke:
            return OutKafkaMessage(
                result=f"ERROR: {ke.name()}",
                timestamp=int(time.time() * 1000)
            )
            raise ke


