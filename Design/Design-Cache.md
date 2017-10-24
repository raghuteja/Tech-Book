# Design Caching system

### Eviction strategy

To add new entries in cache and if the cache size is full we might need to evict some entries to make space for new entry

### Types of caching systems

#### Write through cache

Writes go through the cache and write is confirmed as success only if writes to DB and the cache BOTH succeed. Write latency will be higher in this case as there are writes to 2 separate systems.

#### Write around cache

Write directly goes to the DB. The cache system reads the information from DB incase of a miss. While this ensures lower write load to the cache and faster writes, this can lead to higher read latency incase of applications which write and re-read the information quickly.

#### Write back cache

Write is directly done to the caching layer and confirmed as the write to the cache completes. The cache then asynchronously syncs this write to the DB. Very low latency, we stand the risk of losing the data incase the caching layer dies. We can improve our odds by introducing having more than one replica acknowledging the write.

### Implementing LRU Cache

In case of single machine single threaded : [LRU Implementation](/Data-Structures/LRU-Implementation.md)

In case of multi threaded : We might need to use read/write level locks in case of hash map

### Sharding

If the data is too high and cannot fit in single machine, we might need to split it into multiple machines

#### How to shard data

Sharding is done based on key, we can pick shard based on $$hash(key) \space \% \space TOTAL\_SHARDS$$, If we want to increase the number of shards then we might need to reshuffle a lot of data from one machine to another machine. To avoid this we can use [consistent hashing](/Data-Engineering/Distributed-Systems/Consistent-Hashing.md)

#### Failure cases

If shard goes down then the latency for the keys corresponding the shard will increase, To avoid this we can use replication which further introduces bunch of complications

Read [KV Store design](/Design/KV-Store.md) to understand completely

### Credits

* [Interview Bit](https://www.interviewbit.com/problems/design-cache/)