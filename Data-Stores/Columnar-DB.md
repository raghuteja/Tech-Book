# Columnar data stores

A columnar database is a database management system that stores data tables as columns rather than as rows.

### Pros
1. If you are querying for single column or doing any aggregation, columnar db will be fast (Reason : Disk Seek time)
2. Requires less amount of space for storage (Reason : Compression (Since similar data types are grouped together))

### Cons
1. Data Insertions will be slow (Due to multiple places for each column)
