# Bloom Filter

Bloom filter is a space-efficient probabilistic data
structure that is used to test whether an element is a member of a set

### Properties

* False positives are possible, but false negatives are not in this structure
* Elements can be added to the set, but not removed
* The more elements that are added to the set, the larger the probability of false positives

### Setup

Both insertions and membership queries are performed in constant time.

A Bloom filter is a bit vector $$B$$ of $$m$$ bits, with k independent hash functions $$h_1, ..., h_k$$ that map each key in $$U$$ to the set $$0, 1, ..., m - 1$$.

1. Initially all m bits of B are set to 0.
2. Insert $$x$$ into Bloom filter, Compute $$h_1(x), ..., h_k(x)$$ and set $$B[h_1(x)] = B[h_2(x)] = ... = B[h_k(x)] = 1$$.
3. Query, Compute $$h_1(x), ..., h_k(x)$$. If $$B[h_1(x)] = B[h_2(x)] = ... = B[h_k(x)] = 1$$ then answer Yes, else answer No.

### Analysis

#### False positive rate probability

Probability that one hash do not set a given bit is $$1 - \dfrac{1}{m}$$ where $$m$$ is number of bits

Probability that a bit is not set by any of hash functions$$(k)$$ for a given input is $$\bigg(1 - \dfrac{1}{m}\bigg)^k$$

Probability that a bit is not set after inserting n elements is $$\bigg(1 - \dfrac{1}{m}\bigg)^{kn} = \textit{e}^{\scriptsize{-\dfrac{kn}{m}}}$$

Probability of false positive means specific set of k bits should be equal to 1 i.e, $$\bigg(1 - \bigg(1 - \dfrac{1}{m}\bigg)^{kn}\bigg)^k = \bigg(1 - \textit{e}^{\scriptsize{-\dfrac{kn}{m}}}\bigg)^k$$

Applying log on both sides

$$
g = k\ln(1 - e^{-kn/m})
$$

To minimize false positive rate with respect to k

$$
\dfrac{\partial g}{\partial k} = \ln(1 - e^{-kn/m}) + \dfrac{kn}{m}\dfrac{e^{-kn/m}}{1 - e^{-kn/m}}
$$

derivative is zero when $$k = (m/n)\ln2$$

#### Compound error probability after merging

Compound probability after merging n bloom filters is $$\bigg(1 - \displaystyle\prod_{i=1}^n(1 - p_i)\bigg)$$

### Bloom filter tricks

1. Union of bloom filters of same size
2. Intersection of bloom filters of same size
3. Shrink bloom filter size if the number of bits in bloom filter is power of 2, This can be done by ignoring least significant bit after hash

### Limitations

A limitation of standard Bloom filters is that one cannot remove existing items without rebuilding the entire filter (or possibly introducing generally less desirable false negatives).

### Counting Bloom filters

In a counting Bloom filter, each entry in the Bloom filter is not a single bit but rather a small counter. When an item is inserted, the corresponding counters are incremented; when an item is deleted, the corresponding counters are decremented. But they generally use 3–4x space to retain the same false positive rate as a space-optimized Bloom filter.


### Credits

1. [Bloom filters and Hashing](http://people.math.gatech.edu/~randall/AlgsF09/bloomfilters.pdf)
2. <a href="/assets/papers/Bloomfilter.pdf" target="_blank">Complete Paper</a>
3. <a href="/assets/papers/Bloomfilter-Applications.pdf" target="_blank">Bloomfilter Applications</a>
