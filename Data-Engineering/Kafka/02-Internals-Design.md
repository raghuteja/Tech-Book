# Kafka Internals

Internally each partition in kafka is furhter split into segments. When Kafka writes to a partition, it internally writes to a active segment. If the segment's size limit is reached, a new segment is opened and that becomes the new active segment.

For better performance, Kafka flushes the segment files to disk only after a configurable number of messages have been published or a certain amount of time has elapsed. A message is only exposed to the consumers after it is flushed.

### Segments

Segments are named by their base offset. The base offset of a segment is an offset greater than offsets in previous segments and less than or equal to offsets in that segment.

On disk, a partition is a directory and each segment is an index file and a log file. Messages are stored in log files. Each message is its value, offset, timestamp, key, message size, compression codec, checksum, and version of the message format.

The data format on disk is exactly the same as what the broker receives from the producer over the network and sends to its consumers. This allows Kafka to efficiently transfer data with [zero copy](/General/Zero-Copy.md).

Every segment of a log (the files \*.log) has it's corresponding index (the files \*.index) with the same name as they represent the base offset.

Segment indexes map message offsets to their position in the log. The index file is memory mapped, and the offset look up uses binary search to find the nearest offset less than or equal to the target offset. Not every message within a log has it's corresponding message within the index. The configuration parameter `index.interval.bytes`, which is 4096 bytes by default, sets an index interval which basically describes how frequently (after how many bytes) an index entry will be added.

The index file is made up of 8 byte entries, 4 bytes to store the offset relative to the base offset and 4 bytes to store the position. The offset is relative to the base offset so that only 4 bytes is needed to store the offset. 

Size of the .index file is configuration parameter segment.index.bytes, which is 10MB by default, describes the size of this file. This space is reallocated and will shrink only after log rolls.

Kafka wraps compressed messages together
Producers sending compressed messages will compress the batch together and send it as the payload of a wrapped message.

### Efficiency

Kafka rely on the underlying file system page cache. It has the main benefit of avoiding double buffering, messages are only cached in the page cache.

### Credits

1. [Medium Travis Jeffery](https://thehoard.blog/how-kafkas-storage-internals-work-3a29b02e026)
