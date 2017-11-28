# Google File System (GFS)

### Introduction

* Component failures are norm rather than the exception
* Multi GB files are common
* Files are mutated by appending new data, Random writes with in a file does not exist
* Efficiently implement multiple clients concurrently append to the same file with a minimal overhead, can be often used as producer/consumer

### Architecture

* GFS cluster consists of a single master and multiple chunkservers
* Files are divided into fixed-size chunks, Each chunk is identified by an immutable and globally unique 64 bit chunk handle assigned by the master at the time of chunk creation
* Chunkservers store chunks on local disks as Linux files and read or write chunkdata specified by a chunk handle and byte range
* Each chunk will be replicated into multiple chunk servers for reliability
* Master maintains all file system metadata, mapping from files to chunks, and the current locations of chunks.
* The master periodically communicates with each chunkserver in HeartBeat messages to give it instructions and collect its state.
* Clients interact with the master for metadata operations, but all data-bearing communication goes directly to the chunkservers.
* Chunkservers need not cache file data because chunks are stored as local files and so Linux's buffer cache already keeps frequently accessed data in memory

#### Chunk Size

Typical chunk size is 64MB much larger than typical file system blocksize.

**Pros**
* Reduces client-master interactions
* Reduce network overhead by keeping a persistent TCP connection to the chunkserver over an extended
period of time.
* Reduces the size of the metadata stored on the master.

**Cons**
* A small file consists of a small number of chunks, perhaps just one.
* Chunks can become hotspots and this problem can be fixed by increasing replication factor

#### Metadata

Master contains file and chunk namespaces, mapping from files to chunks, All metadata is kept in the master's memory.

Namespaces and file-to-chunkmapping are also kept persistent by logging mutations to an operation log stored on the master's local disk and replicated on remote machines

Master does not store chunklocation information persistently. Instead, it asks each chunkserver about its chunks at master startup and whenever a chunkserver joins the cluster.

**Cons** in storing entire metadata in memory is that the number of chunks and hence the capacity of the whole system is limited by how much memory the master has. Though master store less than 64 bytes of memory for 64 MB block

**Operational Log** contains historical record of critical metadata changes. As it is critial, it will be replicated multiple remote machines and respond to a client operation only after flushing the corresponding log record to disk both locally and remotely.

The master recovers its file system state by replaying the operation log. The master checkpoints its state whenever the log grows beyond a certain size so that it can recover by loading the latest checkpoint from local disk and replaying only the records after that. The checkpoint is in a compact B-tree like form that can be directly mapped into memory and used for namespace lookup without extra parsing. This further speeds up recovery and improves availability

### Credits

1. [GFS](https://research.google.com/archive/gfs.html)