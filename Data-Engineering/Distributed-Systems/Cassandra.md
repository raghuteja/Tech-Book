# Cassandra

### Data Model

#### Cluster

* Cluster is a container of key spaces (Databases in RDBMS)
* Cluster is made up of nodes
* Cassandra assigns data to nodes in the cluster by arranging them in a **Ring**

##### Key Space attributes

* Replication Factor
* Replication Placement strategy
    * Simple Family
    * Network Topology strategy (Based on datacenters and racks)
* Column Family

**How Cassandra decides which node to store data/replica?**
Partitioner will decide where the first copy of data should go, Normally random partitioner

So Random partitioner will divide keys based on key ranges

Replication placement strategy decides where the replicas should reside

**Column Family**

Column Family corresponds to table in RDBMS

* Static column family
* Dynamic column family

Cassandra has a concept of super column family which allows nesting

### Architecture

**System Key space : ** Cassandra has internal key space called system key space to store metadata information, similar to information schema in mysql

Cassandra is Peer-to-Peer architecture unlike master slave architecture

#### Commit Log

When a write request enters to Cassandra system first it will be written into commit log

Once it is written in commit log Cassandra will write into **MemTables** (In memory resident datastructure)

Once the memtable reaches threshold the contents of memtable will be flushed into disk