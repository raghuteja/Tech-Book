# Storm

Storm is a real time distributed data processing engine that powers the real time stream data management tasks

- Streaming data processing framework
- Atleast once processing semantics
- Horizontally scalable and fault tolerant

### Architecture

Storm's architecture consists of streams of tuples flowing through topologies. A topology is a directed graph where vertices represent computation and the edges represent the data flow between the computation components

Vertices are further divided into two sets - **Spouts** and **Bolts**

Spouts pull data from queues and bolts process the incoming tuples and pass them to next set of bolts downstream

- **Stream :** A sequence of tuples
- **Spout :** Source of streams
- **Bolt :** Applies function on input streams and emits one or more output streams
- **Topology :** A graph of Spouts, Streams and Bolts

#### Overview

Clients submit topology to master node called **Nimbus**. 

- **Nimbus :** Central coordinator of jobs
- **Supervisor :** A node that performs processing
- **Worker :** A JVM process where topology executes
- **Task :** A thread of bolt or spout execution

![](/assets/images/Storm-Cluster-Architecture.png)

Each worker node runs under supervisor that communicates with Nimbus, Cluster state is maintained under zookeeper

