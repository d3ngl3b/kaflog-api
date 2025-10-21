import os
import sys

from confluent_kafka import Consumer, KafkaError, KafkaException

from .db_client import RawWriter, DbWriter

conf = {'bootstrap.servers': os.getenv("BOOTSTRAP_SERVERS"),
        'group.id': os.getenv("GROUP_ID_DB"),
        'enable.auto.commit': os.getenv("ENABLE_COMMIT"),
        'auto.offset.reset': os.getenv("AUTO_OFFSET")}

writer = RawWriter()

running = True



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
                msg_process(writer, msg)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()
        shutdown()

def msg_process(writer: DbWriter, msg: str):
    writer.write(msg)

def shutdown():
    running = False

def main():
    consumer = Consumer(conf)
    ts = os.getenv("TOPICS").split(",")

    basic_consume_loop(consumer, topics=ts)

if __name__ == "__main__":
    main()
