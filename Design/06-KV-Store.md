# Design Key Value Store

### Basic KV Store

Simple key value store in a single machine

It's straight forward to use hash table to store key-value pairs, Downside of this is we may not be able to fit in memory if the data is huge

Alternatives for that is 

* Compress the data
* Store the data in disk (Keep frequently used data in memory and rest in disk)

If the data size does not fit in single machine, we might need to scale horizontally

### Distributed KV Store

Main problem here is how to partition data into multiple machines, Sharding. Then system is highly prone to network failures.

When dealing with the possibility of network failures, strong consistency and high data availability cannot be achieved simultaneously ([CAP Theorem](/Data-Engineering/Distributed-Systems/CAP-Theorem.md))

Availability can be increased by using optimistic replication techniques, where changes are allowed to propagate to replicas in the background, and concurrent, disconnected work is tolerated

The challenge with this approach is that it can lead to conflicting changes which must be detected and resolved.

Challenges involved in this are

1. **When to resolve this (During reads or writes) : ** If we do conflict resolution during writes, writes may be rejected if the data store cannot reach all (or a majority of) the replicas at a given time. This results in low availability, So to make system highly available we can do conflict resolution during reads

2. **Who to resolve this : ** Datastore or Application, If conflict resolution is done by datastore then choices are limited such as last write wins or so, As Application is more aware of data schema, we can provide application to resolve this

#### Key Principles

* **Symmetry** : Every node should have same set of responsibilities

* **Heterogeneity** : Work distribution should be proportional to the capabilities of individual servers

### System Architecture

#### Interface

Should support `get(key)` and `put(key, value)` operations

#### Partitioning

[Consistent Hashing](/Data-Engineering/Distributed-Systems/Consistent-Hashing.md)