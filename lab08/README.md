# Stream processing part 1 - Apache Kafka

In this laboratory you will learn how to run Kafka and perform basic operations. If you are
stuck, ask the instructor for help or read the solution.

## 1. Starting Kafka

Run the following commands to start *[Kafka](https://kafka.apache.org/)*:
```bash
$ mkdir kafka_lab && cd kafka_lab
$ wget https://dlcdn.apache.org/kafka/3.1.0/kafka_2.13-3.1.0.tgz
$ tar -xzf kafka_2.13-3.1.0.tgz
$ cd kafka_2.13-3.1.0
$ ./bin/zookeeper-server-start.sh config/zookeeper.properties
# in second terminal:
$ ./bin/kafka-server-start.sh config/server.properties
```

## 2. Creating topics

Run `./bin/kafka-topics.sh` and read the output. Focus on the following options:
`--bootstrap-server, --config, --create, --delete, --describe, --list, --partitions,
--topic`. Use this program to create topic `my_first_topic` with 10 partitions. Hint:
bootstrap-server expected format is `kafka_address:kafka_port`, and default Kafka port
is 9092.

<details>
<summary>Solution</summary>
<br>

```bash
$ ./bin/kafka-topics.sh --create --topic my_first_topic --partitions 10 --bootstrap-server localhost:9092
```
</details>

Use the same program to list all topics. Make sure your attempt to create a topic
was successful. Then use `--describe` option to get more details about the topic.

<details>
<summary>Solution</summary>
<br>

```bash
$ ./bin/kafka-topics.sh --list --bootstrap-server localhost:9092
my_first_topic
$ ./bin/kafka-topics.sh --describe --topic my_first_topic --bootstrap-server localhost:9092
Topic: my_first_topic	TopicId: VCMVMJJtTviWJo2nQDeBPQ	PartitionCount: 10	ReplicationFactor: 1	Configs: segment.bytes=1073741824
	Topic: my_first_topic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_first_topic	Partition: 1	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_first_topic	Partition: 2	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_first_topic	Partition: 3	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_first_topic	Partition: 4	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_first_topic	Partition: 5	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_first_topic	Partition: 6	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_first_topic	Partition: 7	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_first_topic	Partition: 8	Leader: 0	Replicas: 0	Isr: 0
	Topic: my_first_topic	Partition: 9	Leader: 0	Replicas: 0	Isr: 0
```
</details>

## 3. Sending and receiving messages

Run `./bin/kafka-console-producer.sh` and read the output. For now focus on two options:
`--bootstrap-server, --topic`. Use this program to send several messages to `my_first_topic`
(each line you enter will be treated as a separate message).

<details>
<summary>Solution</summary>
<br>

```bash
$ ./bin/kafka-console-producer.sh --topic my_first_topic --bootstrap-server localhost:9092
>This is my first message
>This is my second message
```
</details>

You can stop the producer with Ctrl-C, but keep it running, as it will be needed for next tasks.

Open two more terminals and use `./bin/kafka-console-consumer.sh` in each to read messages
from `my_first_topic`.

<details>
<summary>Solution</summary>
<br>

```bash
# in second terminal:
$ ./bin/kafka-console-consumer.sh --topic my_first_topic --bootstrap-server localhost:9092
# in third terminal
$ ./bin/kafka-console-consumer.sh --topic my_first_topic --bootstrap-server localhost:9092
```

Note that consumers didn't write the first two messages. By default, they will consume only
new messages, so messages produced while a consumer is down will be skipped. To read all the
messages, start consumers with `--from-beginning` option added.

```bash
# in fourth terminal:
$ ./bin/kafka-console-consumer.sh --topic my_first_topic --bootstrap-server localhost:9092 --from-beginning
This is my first message
This is my second message
```

New messages should be received by both consumers.
```bash
# send more messages in first terminal (producer):
>This is my third message
>This is my fourth message
# receive in second terminal (consumer 1):
This is my third message
This is my fourth message
# receive in third terminal (consumer 2):
This is my third message
This is my fourth message
```
</details>

## 4. Assigning consumer groups

Stop the consumers with Ctrl-C, then start them again, but this time with a consumer group
assigned. Send ten different messages and observe output from the consumers.

<details>
<summary>Solution</summary>
<br>

To start the consumers run:
```bash
# in second terminal:
$ ./bin/kafka-console-consumer.sh --topic my_first_topic --bootstrap-server localhost:9092 --group my_group
# in third terminal:
$ ./bin/kafka-console-consumer.sh --topic my_first_topic --bootstrap-server localhost:9092 --group my_group
```

Each message should be read by just one consumer, and messages should be distributed
equally between the consumers.

```bash
# first terminal (producer):
>message 1
>message 2
...
>message 10
# second terminal (consumer 1):
message 1
message 3
message 5
message 7
message 9
# third terminal (consumer 2):
message 2
message 4
message 6
message 8
message 10
```
</details>

## 5. Checking offsets and lag
Stop all consumers with Ctrl-C. Use `./bin/kafka-consumer-groups.sh` script to get the details
of your consumer group.

<details>
<summary>Solution</summary>
<br>

```bash
$ ./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group my_group --describe

Consumer group 'my_group' has no active members.

GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID     HOST            CLIENT-ID
my_group        my_first_topic  1          0               0               0               -               -               -
my_group        my_first_topic  9          3               3               0               -               -               -
my_group        my_first_topic  2          0               0               0               -               -               -
my_group        my_first_topic  3          0               0               0               -               -               -
my_group        my_first_topic  0          2               2               0               -               -               -
my_group        my_first_topic  8          0               0               0               -               -               -
my_group        my_first_topic  5          0               0               0               -               -               -
my_group        my_first_topic  7          4               4               0               -               -               -
my_group        my_first_topic  6          4               4               0               -               -               -
my_group        my_first_topic  4          1               1               0               -               -               -

```
</details>

Now start two consumers within group `my_group`, and run the script again.

<details>
<summary>Solution</summary>
<br>

```bash
$ ./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group my_group --describe
GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                           HOST            CLIENT-ID
my_group        my_first_topic  9          3               3               0               console-consumer-70f5666e-4146-4e0c-97d4-67777dc7eebb /127.0.0.1      console-consumer
my_group        my_first_topic  6          4               4               0               console-consumer-70f5666e-4146-4e0c-97d4-67777dc7eebb /127.0.0.1      console-consumer
my_group        my_first_topic  8          0               0               0               console-consumer-70f5666e-4146-4e0c-97d4-67777dc7eebb /127.0.0.1      console-consumer
my_group        my_first_topic  5          0               0               0               console-consumer-70f5666e-4146-4e0c-97d4-67777dc7eebb /127.0.0.1      console-consumer
my_group        my_first_topic  7          4               4               0               console-consumer-70f5666e-4146-4e0c-97d4-67777dc7eebb /127.0.0.1      console-consumer
my_group        my_first_topic  1          0               0               0               console-consumer-67bab267-9f45-412f-ba32-0085d9076214 /127.0.0.1      console-consumer
my_group        my_first_topic  2          0               0               0               console-consumer-67bab267-9f45-412f-ba32-0085d9076214 /127.0.0.1      console-consumer
my_group        my_first_topic  3          0               0               0               console-consumer-67bab267-9f45-412f-ba32-0085d9076214 /127.0.0.1      console-consumer
my_group        my_first_topic  0          2               2               0               console-consumer-67bab267-9f45-412f-ba32-0085d9076214 /127.0.0.1      console-consumer
my_group        my_first_topic  4          1               1               0               console-consumer-67bab267-9f45-412f-ba32-0085d9076214 /127.0.0.1      console-consumer

```
Note that now every partition belongs to a consumer. There are two consumers, each has 5
partitions assigned.
</details>

Stop both consumers, then send several messages to the topic, and run the script once more.

<details>
<summary>Solution</summary>
<br>

```bash
$ ./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group my_group --describe

Consumer group 'my_group' has no active members.

GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID     HOST            CLIENT-ID
my_group        my_first_topic  1          0               4               4               -               -               -
my_group        my_first_topic  9          3               3               0               -               -               -
my_group        my_first_topic  2          0               0               0               -               -               -
my_group        my_first_topic  3          0               0               0               -               -               -
my_group        my_first_topic  0          2               2               0               -               -               -
my_group        my_first_topic  8          0               0               0               -               -               -
my_group        my_first_topic  5          0               2               2               -               -               -
my_group        my_first_topic  7          4               4               0               -               -               -
my_group        my_first_topic  6          4               4               0               -               -               -
my_group        my_first_topic  4          1               2               1               -               -               -

```

The group has no active members, so new messages remain unconsumed. Number of unconsumed messages
is shown in the column LAG.
</details>

## 6. Creating simple data pipelines

Create two topics: `transactions` and `balance`, each with 10 partitions. Read the introduction
to kafka-python *[here](https://kafka-python.readthedocs.io/en/master/)*. Write two simple
programs in Python. The first program should send to each partition of `transactions` a random
integer between -10 and 10 once every second. We will assume that positive numbers represent
cash deposits and negative numbers represent cash withdrawals. We will also assume that each
partition represents a separate bank account. The other program should read `transactions` and
send the current balance of each account to `balance`.

<details>
<summary>Solution</summary>
<br>

transaction_generator.py:
```python
import random
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
while True:
    for account_number in range(0, 10):
        transaction_value = random.randrange(-10, 11)
        producer.send('transactions', value=b'%d' % transaction_value, partition=account_number)
        print(f'new transaction: value={transaction_value} account_number={account_number}')
    time.sleep(1)
```

balance_calculator.py:
```python
from kafka import KafkaConsumer, KafkaProducer

balance = {}
consumer = KafkaConsumer('transactions', bootstrap_servers='localhost:9092')
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for msg in consumer:
    account_number = msg.partition
    if account_number in balance:
        balance[account_number] += int(msg.value)
    else:
        balance[account_number] = int(msg.value)
    producer.send('balance', b'%d' % balance[account_number], partition=account_number)
    print(f'current balance for account {account_number} is {balance[account_number]}')
```
</details>

## 7. Ensuring exactly-once delivery semantics (optional)

What will happen when you restart your app? How can you improve it to guarantee
that balance has the same number of messages as transactions and the n-th message in balance
represents the exact balance after n transactions, even with processing app occasionally
failing? Hint: you may need to use *[Producer API](https://kafka.apache.org/31/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html)*
and *[Consumer API](https://kafka.apache.org/31/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html)* for this task.

## 8. Ensuring high availability (optional)
Create a cluster of 3 brokers. Add a topic with replication factor 2. Chek what
happens when you send a message with one of the brokers down. What if two brokers are down?
Read about availability and durability guarantees *[here](https://kafka.apache.org/documentation/#design_ha)*.
Test different values of `acks`.
