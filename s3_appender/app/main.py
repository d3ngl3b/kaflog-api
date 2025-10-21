import os
import sys
from pydoc_data.topics import topics

from confluent_kafka import Consumer, KafkaError, KafkaException

from .s3_client import RawUploader

conf = {'bootstrap.servers': os.getenv("BOOTSTRAP_SERVERS"),
        'group.id': os.getenv("GROUP_ID_S3"),
        'enable.auto.commit': os.getenv("ENABLE_COMMIT"),
        'auto.offset.reset': os.getenv("AUTO_OFFSET")}

uploader = RawUploader()

running = True

# conf = {'bootstrap.servers': 'host1:9092,host2:9092',
#         'group.id': 'foo',
#         'enable.auto.commit': 'false',
#         'auto.offset.reset': 'earliest'}



def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()
        shutdown()

def msg_process(msg: str):
    uploader.add(msg)

def shutdown():
    running = False

def main():
    consumer = Consumer(conf)
    ts = os.getenv("TOPICS").split(",")

    basic_consume_loop(consumer, topics=ts)

if __name__ == "__main__":
    main()
