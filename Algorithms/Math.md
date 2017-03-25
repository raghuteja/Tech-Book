# Math algorithms

### Check if number n is prime or not

Loop over from 3 to sqrt\(n\) with increments of 2, If any number is n is divisible by any number then it is not prime else it is.

```cpp
bool isPrime(int n)
{
   if (n<=1) return false;
   if (n==2) return true;
   if (n%2==0) return false;
   int m=sqrt(n);

   for (int i=3; i<=m; i+=2)
      if (n%i==0)
         return false;

   return true;
}
```

### List all prime numbers from 1 to n

Using sieve of Eratosthenes

### GCD of two numbers

```cpp
int GCD(int a, int b)
{
   if (b==0) return a;
   return GCD(b,a%b);
}
```

### LCM of two numbers

LCM \* GCD = a \* b

### Credits

1. [Topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/mathematics-for-topcoders/)