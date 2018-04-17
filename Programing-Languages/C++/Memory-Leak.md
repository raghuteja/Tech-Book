# Memory Leak

Memory leak is a type of resource leak that occurs when a computer program incorrectly manages memory allocations in such a way that memory which is no longer needed is not released.

### Example of Memory Leak

```c
#include <stdlib.h>

void f(int n)
{
  int* array = calloc(n, sizeof(int));
  do_some_work(array);
  return
}
```

To fix the above memory leak 

```c
#include <stdlib.h>

void f(int n)
{
  int* array = calloc(n, sizeof(int));
  do_some_work(array);
  free(array);
}
```


### Credits

1. [Wikipedia](https://en.wikipedia.org/wiki/Memory_leak)