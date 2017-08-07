# Design a data structure to implement Least Recently Used (LRU)

LRU : Discards the least recently used items first.

### Operations

1. Insert(key, value)
2. find(key)

### Logic

Algorithm should keep track of which was used when, If the cache limit is reached and we want to insert one more we need to evict least recently used item from cache and insert the new item

#### Implementation

Data structures used:
1. Doubly linked list : maximum size is equal to cache size, The most recently used will be near front end and least recently pages will be near rear end.
2. Hash : with key as key and value as pointer to doubly linked list node
