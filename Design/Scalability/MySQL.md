# MySQL

### Master-Slave replication

**Pros**
If application is read heavy, then instead of reading from master we can use slaves for reading databases and Insert queries can be executed on master which ultimately propagated to slaves

### Caching

On a typical MySQL Server in my.cnf there is a variable called `query_cache_type` which takes values `0` or `1` 

So first time you executes a query it might take longer time but from next time it got executed when the query cache is one and rows have not changed, Then response is going to come back much more quickly

One can use memcache(Memory Cache) which is another layer of cache between application server and database layer. Facebook uses memcache heavily