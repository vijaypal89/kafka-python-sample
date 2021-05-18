# kafka-python-sample
Examples of various Kafka module (Topics, Partitions, Consumers, Produces etc..)

# Steps:
1. Clone the repository
2. Exceute containers.sh      # This file is responsible to run Zookeeper and Kafka containers
3. Execute python topic.py    # This file connects to kafka admin and creates topic - "mytopic" and sets 3 partitions on this topic
4. Execute python consumer.py # This file subscribes on topic name - "mytopic", consumer group - "my-group-1", you can run multiple instance of this consumer, one consumer is responsible to consume from one partition, hence no point of running more than 3 instance.
5. Now you can send messages on this topic with producer.py, Execute python producer.py <msg>. Partition is based on first character of msg, if msg[0] is between 'A' and 'I' it goes to partition 1, elif msg[0] is between 'J' and 'Q' it goes to partition 2 else partition 3.
 
