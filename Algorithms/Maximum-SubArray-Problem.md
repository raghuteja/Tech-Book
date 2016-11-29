# Maximum SubArray Problem \(Kadane's algorithm\)

### Problem

Find the continues subarray which has the maximum sum

### Algorithm

Kadane's algorithm consists of a scan through the array values, computing at each position the maximum \(positive sum\) subarray ending at that position. This subarray is either empty \(in which case its sum is zero\) or consists of one more element than the maximum subarray ending at the previous position. The algorithm only needs to keep track of the ending position because the implied starting position is just after the last position at which the sum went negative; a higher sum can always be found by dropping any negative-sum prefix.

### Implementation

```py
def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

### Variants

**Question1**

Problem that does not allow zero length subarrays

**Question2**

You are given a binary array. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the elements. By flipping, we mean change character `0` to `1` and vice-versa. Your aim is to perform ATMOST one operation such that in final string number of `1`s is maximized. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R.

### Source

* [Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem)

