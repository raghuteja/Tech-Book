# Storm

- Streaming data processing framework
- Atleast once processing semantics
- Horizontally scalable and fault tolerant

### Programming model

- Stream : A sequence of tuples
- Spout : Source of streams
- Bolt : Applies function on input streams and emits one or more output streams
- Topology : A graph of Spouts, Streams and Bolts

### Architecture

- Nimbus : Central coordinator of jobs
- Supervisor : A node that performs processing
- Task : A thread of bolt or spout execution
- Worker : A JVM process where topology executes

Stream grouping assigns tasks through consistent hashing like mechanism

![](/assets/images/Storm-Cluster-Architecture.png)

### Credits

1. [Yahoo](https://www.slideshare.net/RobertEvans26/scaling-apache-storm-hadoop-summit-2015)
2. [Safari Books Online](https://www.safaribooksonline.com/library/view/learning-path-advanced/9781491978665/)