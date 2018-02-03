# Kafka Distributed Coordination

For coordination among brokers in Kafka it uses service Zookeeper

### Kafka uses Zookeeper for the following tasks

1. Detecting the addition and the removal of brokers and consumers
2. Triggering a rebalance process in each consumer when the above events happen
3. Maintaining the consumption relationship and keeping track of the consumed offset of each partition
