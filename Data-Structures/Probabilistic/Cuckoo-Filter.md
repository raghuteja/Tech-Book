# Cuckoo Filter

Similar to [BloomFilter](/Data-Structures/Probabilistic/Bloom-Filter.md) with major advantages

1. Supports adding and removing items dynamically
2. Provides higher lookup performance than traditional Bloom filters, even when close to full
3. It uses less space than Bloom filters in many practical
applications, if the target false positive rate is less than 3%

Cuckoo filter internally uses optimized [Cuckoo Hashing](/Data-Structures/Hashing/Cuckoo-Hashing.md) technique called partial-key cuckoo hashing

### Partial Key cuckoo hashing

To make cuckoo filters highly space efficient, we use a multi-way associative cuckoo hash table to provide high-speed lookup and high table occupancy (e.g., 95% hash table slots filled); to further reduce the hash table size, each item is first hashed into a constant-sized fingerprint before inserted into this hash table.

#### Insert

```code
// Insert(x)
f = fingerprint(x)
i1 = hash(x)
i2 = i1 ^ hash(f) // XOR operation

if bucket[i1] or bucket[i2] has an empty entry then
    add f to that bucket;
    return Success;

// Need to relocate existing items

i = randomly pick i1 or i2
for n = 0; n < MaxNumKicks; n++ do
    randomly select an entry e from bucket[i]
    swap f and the fingerprint stored in entry e
    i = i ^ hash(f)
    if bucket[i] has an empty entry then
        add f to bucket[i]
        return Success
        
// Hashtable is considered full

return Failure
```

#### Lookup

```code
// Lookup(x)
f = fingerprint(x)
i1 = hash(x)
i2 = i1 ^ hash(f) // XOR operation

if bucket[i1] or bucket[i2] has f then
    return True
    
return False
```

#### Delete

```code
// Delete(x)
f = fingerprint(x)
i1 = hash(x)
i2 = i1 ^ hash(f) // XOR operation

if bucket[i1] or bucket[i2] has f then
    remove a copy of f from this bucket
    return True

return False
```


### Credits

1. [Cuckoo Filter: Practically Better Than Bloom](https://www.cs.cmu.edu/~dga/papers/cuckoo-conext2014.pdf)
2. <a href="/assets/papers/CuckooFilter.pdf" target="_blank">Complete Paper</a>
