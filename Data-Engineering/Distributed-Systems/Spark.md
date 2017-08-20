# Spark

Spark applies scatter gather pattern in distributed programming similar to map reduce

In spark data model is in the form of RDD (Resilient distributed datasource)

Spark is aganostic of storage model (Can works on/on top of HDFS, Cassandra etc...)

Transformation functions turn one RDD to another and action functions will be used to reduce

It is kind of batch mode processing frameworks

### Properties of RDD

- Can be larger than a single computer
- Read from an input source
- Can be output from a pure function
- Immutable
- Typed
- Ordered
- Lazily Evaluated
- Partitioned
- Collection of things

### Spark Architecture

![](/assets/Spark-Cluster-Architecture.png)

### Credits

1. [Apache Spark: core concepts, architecture and internals](http://datastrophic.io/core-concepts-architecture-and-internals-of-apache-spark/)
2. [Safari Books Online](https://www.safaribooksonline.com/library/view/learning-path-advanced/9781491978665/)