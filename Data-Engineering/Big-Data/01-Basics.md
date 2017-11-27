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

