# Consistent Hashing

Consistent hashing is a special kind of hashing such that when a hash table is resized, only K/n keys need to be remapped on average, where K is the number of keys, and n is the number of slots. In contrast, in most traditional hash tables, a change in the number of array slots causes nearly all keys to be remapped because the mapping between the keys and the slots is defined by a modular operation.

### Design

Choose some standard base hash function that maps keys to the number range [0,1]. Each URL is thus mapped to a point on the unit circle.

At the same time, map every cache in the system to a point on the unit circle.

Now assign each key to the first cache whose point it encounters moving clockwise

### Uses

* Used in distributed key value store

### Credits

* [Medium](https://medium.com/@sent0hil/consistent-hashing-a-guide-go-implementation-fe3421ac3e8f)
* [Wikipedia](https://en.wikipedia.org/wiki/Consistent_hashing)