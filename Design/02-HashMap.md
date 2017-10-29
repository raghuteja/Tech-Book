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

#### GetRandomKey in O(1) operation

GetRandomKey can be achieved by storing keys in an array, when this function is called we will generate random number between 0 and array length and return the corresponding key

* Insert - O(1)
* Update - O(1)
* Fetch - O(1)
* GetRandomKey - O(1)
* Delete - O(N)

As you see above deletion operation is O(N). This is because deleting element in from array is O(N), we can optimize this by swapping the deleted element with last element in array and decreasing the size of array by 1 as the order of keys in array is not important

For example when inserting 4 with value 10, we need to store <4, (10, 1)> in the map where 1 is the index of the key in the array.

Now all operations are of O(1)