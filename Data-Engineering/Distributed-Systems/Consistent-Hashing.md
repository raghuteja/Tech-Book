# Consistent Hashing

### Motivation

Consistent hashing is a special kind of hashing such that when a hash table is resized, only K/n keys need to be remapped on average, where K is the number of keys, and n is the number of slots. In contrast, in most traditional hash tables, a change in the number of array slots causes nearly all keys to be remapped because the mapping between the keys and the slots is defined by a modular operation.

m items need to be stored in n distributed web caches

General hash `h(x) = (ax+b) mod n`

What if n changes?

simple solution is mod n => mod (n+1) : In this case almost all of the items need to move

Consistent hashing will take care of this by handling bare minimum movement

### Design

Choose some standard base hash function that maps keys to the number range [0,1]. Each URL is thus mapped to a point on the unit circle.

At the same time, map every cache in the system to a point on the unit circle.

Now assign each key to the first cache whose point it encounters moving clockwise

### Replication

Instead of assigning key to the first cache in clockwise we will assign key to first three caches in clockwise rotation.

The main problem here is consistancy which means there can be a situation where read doesn't return the most up-to-date value.

For that we have a consistency rule : `R + W > N`

1. N is Number of replicas
2. R is Number of nodes a read operation should contact before successful read operation
3. R is Number of nodes a write operation should contact before successful read operation

How this formula came?

There are N nodes that might hold the value. A write contacts at least W nodes. A subsequent read contacts at least R nodes. Since R + W > N there is at least one node that both Read operation and Write operation is made, so this node is able to return the latest write to the read operation.

Max value of R is N and W is N, This corresponds to reading and writing at ConsistencyLevel ALL

In case if we need very low latency we should be expecting eventual consistency instead of instant consistency

### Implementation

Maintain a binary search tree whose keys are machine values

1. To insert an item, Find the successor and add it to the machine
2. To insert a machine, Find the successor and get items from that machine
3. To delete a machine, Find the successor and push items to that machine

### Uses

* Used in distributed key value store

### Credits

* [Medium](https://medium.com/@sent0hil/consistent-hashing-a-guide-go-implementation-fe3421ac3e8f)
* [Wikipedia](https://en.wikipedia.org/wiki/Consistent_hashing)
* [MIT Lecture](https://www.youtube.com/watch?v=hM547xRIdzc)
* [R + W > N Explanation](https://stackoverflow.com/a/7823201/1465334)