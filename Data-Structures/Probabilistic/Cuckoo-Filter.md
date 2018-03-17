# Cuckoo Filter

Similar to [BloomFilter](/Data-Structures/Probabilistic/Bloom-Filter.md) with major advantages

1. Supports adding and removing items dynamically
2. Provides higher lookup performance than traditional Bloom filters, even when close to full
3. It uses less space than Bloom filters in many practical
applications, if the target false positive rate is less than 3%

