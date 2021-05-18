#!/bin/bash

docker run -dit --name zookeeper -p 2181:2181 zookeeper
zookeeper_ip=$(docker inspect zookeeper --format '{{.NetworkSettings.IPAddress}}')
docker run -dit -p 9092:9092 --name kafka  -e KAFKA_ZOOKEEPER_CONNECT=${zookeeper_ip}:2181 \
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
-e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 confluentinc/cp-kafka

echo "Running Zookeeper and Kafka container. To check container status run - docker ps"
