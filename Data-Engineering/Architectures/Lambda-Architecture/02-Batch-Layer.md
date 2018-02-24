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

Ex : HDFS

### Computing batch view from master data

Because your master dataset is continually growing, you must have a strategy for updating your batch views when new data becomes available. 
You could choose a recomputation algorithm, throwing away the old batch views and recomputing functions over the entire master dataset which may not be practically possible all the time. 

**Incremental algorithm** will update the views directly when new data arrives.

Ex : Map-Reduce Paradigm

### Batch views for web analytics queries

#### Page views over time range

A view can be generated per hour basis counts for every URL

To optimize queries for longer time range one can store aggregated counts also over day/month/year

#### Unique visitors over time range

Unique over time range cannot be solved accurately unless you fetch entire data and uniqify them

If we can have some error probability we can generate HyperLogLog for every hour and get unique count over that

To optimize queries for longer time range one can store aggregated HyperLogLog over day/month/year

#### Bounce rate analysis

Similar to page views we just need to maintain bounce count and total count