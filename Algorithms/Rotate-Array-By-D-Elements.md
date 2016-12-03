# Rotate Array of size n by d elements

### Problem

Rotate an array of size n by d elements

### Algorithm

#### Juggling Algorithm

In this method, the array is divided into M cycles, where M = GCD\(n, d\), and rotate the corresponding elements in each cycle

**How does the GCD decide the number of cycles needed to rotate the array?**

Because the inner loop increments in steps of d, and stops when it gets back to the starting point, i.e. a total span which is some multiple of n. That multiple is LCM\(n, d\). Thus the number of elements in that cycle is LCM\(n, d\) / d. The total number of such cycles is n / \(LCM\(n, d\) / d\), which is equal to GCD\(n, d\).

**Why is it that once we finish a cycle, we start the new cycle from the next element i.e, can't the next element be already a part of a processed cycle?**

The inner loop increments in steps of d, which is a multiple of GCD\(n, d\). Thus by the time we start the i-th cycle, for a hit we'd need \(k\*GCD + z\) % n == i \(for 0 &lt;= z &lt; i\). This leads to \(kGCD\) % n == \(i - z\). This clearly has no solutions.

#### Reversal Algorithm

For arr\[\] = \[1, 2, 3, 4, 5, 6, 7\], d =2 and n = 7  
A = \[1, 2\] and B = \[3, 4, 5, 6, 7\]  
Reverse A, we get ArB = \[2, 1, 3, 4, 5, 6, 7\]  
Reverse B, we get ArBr = \[2, 1, 7, 6, 5, 4, 3\]  
Reverse all, we get \(ArBr\)r = \[3, 4, 5, 6, 7, 1, 2\]

#### Block swap algorithm

### Implementation

```c
/*Juggling Algorithm : Function to left rotate arr[] of siz n by d*/
void leftRotate(int arr[], int d, int n)
{
  int i, j, k, temp;
  for (i = 0; i < gcd(d, n); i++)
  {
    /* move i-th values of blocks */
    temp = arr[i];
    j = i;
    while(1)
    {
      k = j + d;
      if (k >= n)
        k = k - n;
      if (k == i)
        break;
      arr[j] = arr[k];
      j = k;
    }
    arr[j] = temp;
  }
}
```

### Variants

### Source

* [GeeksforGeeks](http://www.geeksforgeeks.org/array-rotation/)
* [Stackoverflow](http://stackoverflow.com/questions/23321216/rotating-an-array-using-juggling-algorithm)



