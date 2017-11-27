# Lambda Architecture (Basics)

### What is data system

Data system answers questions based on current and past data

`query = function(all data)`

Querying on huge dataset will take longer time so Lambda Architecture defines a consistent approach to meet the latency requirements

### Properties

* Robustness and fault tolerance
* Low latency reads and updates
* Scalability
* Extensibility
* Minimal maintenance

### Fully incremental approach

* Database should support updates (Data compaction consumes high CPU usage)
* Extreme complexity of achieving eventual consistency
* Lack of human-fault tolerant database might result in corrupted state

### Design

![](/assets/lambda-architecture.png)

1. All data entering the system is dispatched to both the batch layer and the speed layer for processing.
2. The batch layer has two functions: 
    * managing the master dataset (an immutable, append-only set of raw data)
    * To pre-compute the batch views.
3. The serving layer indexes the batch views so that they can be queried in low-latency, ad-hoc way.
4. The speed layer compensates for the high latency of updates to the serving layer and deals with recent data only.
5. Any incoming query can be answered by merging results from batch views and real-time views.