from kafka.consumer import group
import six

from kafka import KafkaConsumer

topic = "mytopic"
consumer_group = "my-group-1"


def run():
    config = {
                "client_id": "mykafka",
                "bootstrap_servers": "localhost",
                "group_id": consumer_group,
                "value_deserializer": lambda data: six.ensure_binary(data)
            }
    topics = [topic]
    consumer = KafkaConsumer(*topics, **config)

    print(f"Listening messeges on Topic {topic}, "
          f"consumer group - {consumer_group}....")

    while True:
        for message in consumer:
            print(f"RCVD msg - {message.value}")
            print(f"Topic: {message.topic}, Partition: {message.partition}, "
                  f"Offset: {message.offset}, Key: {message.key}")


if __name__ == '__main__':
    run()
