# Hadoop Architecture

#### Rack
A rack is a collection of nodes physically stored together and are connected to the same switch, So network bandwidth between any two nodes in the same rack is greater than network bandwidth between any two nodes on the different rack

#### Cluster
A cluster is a collection of racks

#### Hadoop Architecture

###### Distributed file system
1. HDFS
2. IBM Spectrum scale

###### MapReduce engine
1. Framework for performing calculations on the data in the file system
2. Has builtin resource manager and scheduler


#### HDFS
Two core components
1. One Name Node (Master) [contains metadata about data stored]
2. Multiple Data Nodes (Slaves) [data is stored in these nodes]

* Data can be replicated with some replication factor
* HDFS stores files in blocks(storage unit of HDFS)
* Follows WORM [Write Once Read Many]
* Instead of data to processing, hadoop can do processing to data, Such that there won't be any network congestion
