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

Probability that a bit is not set by any of hash functions for a given input is $$\bigg(1 - \dfrac{1}{m}\bigg)^k$$

Probability that a bit is not set after inserting n elements is $$\bigg(1 - \dfrac{1}{m}\bigg)^{kn} = \textit{e}^{\scriptsize{-\dfrac{kn}{m}}}$$

Probability of false positive means specific set of k bits should be equal to 1 i.e, $$\bigg(1 - \bigg(1 - \dfrac{1}{m}\bigg)^{kn}\bigg)^k = \bigg(1 - \textit{e}^{\scriptsize{-\dfrac{kn}{m}}}\bigg)^k$$

#### Compound error probability after merging

Compound probability after merging n bloom filters is $$\bigg(1 - \displaystyle\prod_{i=1}^n(1 - p_i)\bigg)$$

### Read complete paper

{% pdf src="/assets/papers/BloomFilter.pdf", width="100%", height="850" %}{% endpdf %}

### Credits

1. [Bloom filters and Hashing](http://people.math.gatech.edu/~randall/AlgsF09/bloomfilters.pdf)