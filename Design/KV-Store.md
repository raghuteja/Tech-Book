# Design Key Value Store

### Basic KV Store

Simple key value store in a single machine

It's straight forward to use hash table to store key-value pairs, Downside of this is we may not be able to fit in memory if the data is huge

Alternatives for that is 

* Compress the data
* Store the data in disk (Keep frequently used data in memory and rest in disk)

If the data size does not fit in single machine, we might need to scale horizontally

### Distributed KV Store

Main problem here is how to partition data into multiple machines, Sharding

#### System Availability

One main concern in distributed systems are nodes going down and requests will get dropped.

The most common solution for this is replica

By introducing replica system was more available but we are 
