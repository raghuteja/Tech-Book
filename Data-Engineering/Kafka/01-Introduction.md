# Kafka Introduction

Kafka is a highly scalable fault tolerant realtime messaging system

Messages in Kafka are categorized into topics. Topics are additionally broken down into a number of partitions.

A partition is an ordered, immutable sequence of messages that are appended to. A partition cannot be split across multiple brokers or even multiple disks.


**Retention policy : ** How much data or how long data should be retained, after which Kafka purges messages in order regardless of whether the message has been consumed.

### Producers

Producers create new messages. In other publish/subscribe systems, these may be called publishers or writers.


### Consumers

Consumers read messages. In other publish/subscribe systems, these clients may be called subscribers or readers.

Consumers work as part of a consumer group, which is one or more consumers that work together to consume a topic. The group assures that each partition is only consumed by one member.

### Credits

1. [Apache Kafka Documentation](https://kafka.apache.org/documentation/)