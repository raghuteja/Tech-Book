# Design sorting huge data that does not fit in memory

External sorting technique can be used to sort the data that won't fit in memory

One example is External merge sort algorithm

1. Sorts chunks of data that fit in RAM
2. Merges the sorted chunks together

Merge step can be done in different ways

1. Two way merge 
    * **Pros : ** Reduce number of disk seeks
    * **Cons : ** Increase number of passes
2. N way merge (Can be used when )
    * **Pros : ** Reduce number of passes
    * **Cons : ** Increase number of disk seeks
    
### Credits

1. [Wikipedia](https://en.wikipedia.org/wiki/External_sorting)