# Design HashMap

### Basic HashMap

Hashmap works based on the hashing principle, Hashing is the mechanism of assigning unique code to a variable or attribute using an algorithm to enable easy retrieval.

A true hashing mechanism should always return the same hashCode() when it is applied to the same object.

#### Collision

**What happens if two keys have the same Hashcode?**

When a collision occurs we need to store both the entries, We can use Linked hashmap incase of collision

Linked hashmap will maintain a linked list on collision of a key and store both the entities in the linked list

Worst case if all keys leads to same hashcode the complexity will be $$O(N)$$ to put and get methods. So We can use Binary Tree in such cases other than linked list.

**Alternatives for collision**

Another alternatives for collision is probing (Linear probing and quadratic probing)

#### Resize
So hashmap needs to maintain the array and generate hashcode specific to key and store it in array

**What happens if the size of the array is about to reach and we need to insert more entities?**

Array resize will happen similar to vector we will double the array size and re-populate existing data to the new array

### Concurrent HashMap

ConcurrentHashMap utilizes the same principles of HashMap, but is designed primarily for a multi-threaded application.

#### Implementation

We will set the concurrency level of concurrent hashmap which is estimated number of concurrently updating threads.

So we will maintain concurrency level number of buckets and locks and each bucket signifies an array similar to hashmap explained above

When we need to do get/put operation the corresponding thread will lock the corresponding bucket and release lock once it is done

This way if other threads want to do operations on other buckets they can do it asynchronously

In java concurrent hashmap does the same thing where as hashtable locks the entire map

