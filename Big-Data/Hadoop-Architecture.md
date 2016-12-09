# Hadoop Architecture

#### Rack
A rack is a collection of nodes physically stored togeather and are connected to the same switch, So network bandwidth between any two nodes in the same rack is grater than network bandwidth between any two nodes on the different rack

#### Cluster
A cluster is a collection of racks

#### Hadoop 2.2 Architecture

###### Distributed file system
1. HDFS
2. IBM Spectrum scale

###### MapReduce engine
1. Framework for performing calculations on the data in the file system
2. Has builtin resource manager and scheduler
