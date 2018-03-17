# Cuckoo Hashing

A basic cuckoo hash table consists of an array of buckets where each item has two candidate buckets determined by hash functions h1(x) and h2(x). The lookup procedure checks both buckets to see if either contains this item.

If either of x's two buckets is empty, the algorithm inserts x to that free bucket and the insertion completes. If neither bucket has space the item selects one of the candidate buckets, kicks out the existing item and re-inserts this victim item to its own alternate location.

This procedure may repeat until a vacant bucket is found, or until a maximum number of displacements is reached. If no vacant bucket is found, this hash table is considered too full to insert.