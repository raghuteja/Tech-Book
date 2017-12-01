# Bloom Filter

Bloom filter is a space-efficient probabilistic data
structure that is used to test whether an element is a member of a set

### Properties

* False positives are possible, but false negatives are not in this structure
* Elements can be added to the set, but not removed
* The more elements that are added to the set, the larger the probability of false positives

### Setup

Both insertions and membership queries are performed in constant time.

A Bloom filter is a bit vector $$B$$ of $$m$$ bits, with k independent hash functions $$h_1, ..., h_k$$ that map each key in $$U$$ to the set $$0, 1, ..., m − 1$$.

1. Initially all m bits of B are set to 0.
2. Insert $$x$$ into Bloom filter, Compute $$h_1(x), ..., h_k(x)$$ and set $$B[h_1(x)] = B[h_2(x)] = ... = B[h_k(x)] = 1$$.
3. Query, Compute $$h_1(x), ..., h_k(x)$$. If $$B[h_1(x)] = B[h_2(x)] = ... = B[h_k(x)] = 1$$ then answer Yes, else answer No.

### Analysis



### Credits

1. [Bloom filters and Hashing](http://people.math.gatech.edu/~randall/AlgsF09/bloomfilters.pdf)