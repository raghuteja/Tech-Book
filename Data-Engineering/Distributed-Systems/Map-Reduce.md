# MapReduce

MapReduce is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster

**Phases Involved**

- **Map Phase:** Each worker node applies the "map()" function to the local data to generate intermediate key/value pairs and writes the output to a temporary storage. A master node ensures that only one copy of redundant input data is processed.

- **Shuffle Phase:** Worker nodes redistribute data based on the output keys (produced by the "map()" function), such that all data belonging to one key is located on the same worker node.

- **Reduce Phase:** Worker nodes now process each group of output data, per key, in parallel.

