import six
import sys

from kafka import KafkaProducer

topic = "mytopic"


def run(msg):
    config = {
                "client_id": "mykafka",
                "bootstrap_servers": "localhost",
                "value_serializer": lambda data: six.ensure_binary(data)
            }
    producer = KafkaProducer(**config)

    print(f"Connected to {str(producer)}")
    partition = 0
    if msg[0] > "I" and msg[0] < "R":
        partition = 1
    elif msg[0] >= "R":
        partition = 2

    res = producer.send(
        topic=topic,
        value=msg,
        partition=partition
    )

    print(f"Message sent successfully! {str(res)}")


if __name__ == '__main__':
    run(sys.argv[1])
