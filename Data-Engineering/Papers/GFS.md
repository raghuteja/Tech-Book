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

