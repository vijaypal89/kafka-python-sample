from kafka.admin import KafkaAdminClient, NewTopic

topic = "mytopic"


def run():
    config = {
                "client_id": "mykafka",
                "bootstrap_servers": "localhost"
            }
    kafka_admin = KafkaAdminClient(**config)

    print(f"Connected to {str(kafka_admin)}")

    res = kafka_admin.create_topics(new_topics=[
        NewTopic(name=topic, num_partitions=3, replication_factor=1)
    ])

    print(f"Topic created successfully! {str(res)}")


if __name__ == '__main__':
    run()
