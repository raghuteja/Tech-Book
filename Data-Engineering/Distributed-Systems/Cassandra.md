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

