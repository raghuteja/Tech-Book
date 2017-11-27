# Batch Layer (Lambda Architecture)

Master dataset in lambda architecture is raw and immutable

### Storage

Tradeoff between storing data in normalized form and de-normailzed form

If data is in normalized querying will be slower

Inside master dataset data should be in normalized form and In batch views data can be in denormalized form, As we will query on batch views queries will be faster

### Data transfer format

Data can be serialized using some serialization protocol to transfer from one place to other

Ex : Apache Thrift, Protocol Buffers

### Data storage format

* Distributed KV store
* Distributed file systems

In our web analytics case distributed file systems will be better

Data should be partitioned in such a way that when we want to process particular data we should not read the entire dataset, This process is called **vertical partitioning**

In our case we can store data based on day wise or hour wise

EX : HDFS