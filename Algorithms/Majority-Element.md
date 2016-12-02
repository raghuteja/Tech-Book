# Majority Element \(Boyer–Moore majority vote algorithm\)

### Problem

Find the majority element in the array i.e, the element occurs more than n/2 times

### Algorithm

The algorithm maintains in its local variables a sequence element and a counter, with the counter initially zero. It then processes the elements of the sequence, one at a time. When processing an element x, if the counter is zero, the algorithm stores x as its remembered sequence element and sets the counter to one. Otherwise, it compares x to the stored element and either increments the counter \(if they are equal\) or decrements the counter \(otherwise\). At the end of this process, if the sequence has a majority, it will be the element stored by the algorithm.

### Implementation

```c
int findCandidate(int a[], int size)
{
    int maj_index = 0, count = 1;
    int i;
    for (i = 1; i < size; i++)
    {
        if (count == 0)
        {
            maj_index = i;
            count = 1;
        }
        else if (a[maj_index] == a[i])
            count++;
        else
            count--;
    }
    return a[maj_index];
}
```

### Source

* [Wikipedia](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)



