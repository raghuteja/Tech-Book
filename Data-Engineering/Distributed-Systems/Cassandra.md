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

When a write request enters to Cassandra system first it will be written into commit log, Each commit log will have an internal bit flag to indicate if it needs flushing

Once it is written in commit log Cassandra will write into **MemTables** (In memory resident datastructure)

Once the memtable reaches threshold the contents of memtable will be flushed into a file in disk called **SSTable** (Sorted strings table)

#### Hinted Handoff

Hinted Handoff is the event in case of node failure to ensure availability of ring

Other nodes will store the data and post a note that once node comes down we need to resend to the node that was down

Disadvantage of hinted handoff is there can be network congestion once the node is up because all the other nodes will start transferring data

We can disable Hinted handoff but in that case cluster will decide new key ranges based on $$n-1$$ nodes

#### Compaction

Compaction is merging large accumulated files, In Cassandra compaction is needed for merging SSTables

#### Reads

When ever a read request comes it will first search in memtable if it finds return else search in all SSTables

Its practically impossible to search in all SSTables, So there will be a **bloomfilter** associated with each SSTable and searches bloomfilter first

#### Tombstone

Analogous to soft-delete in RDBMS, Tombstone is just a deletion marker in SSTable until the compaction is done

