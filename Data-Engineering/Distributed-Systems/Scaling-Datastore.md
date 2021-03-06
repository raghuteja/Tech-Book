#Scaling data store

### Read replication

Single master and multiple slaves

This is helpful only when we have lots and lots of reads when compared to writes

**Pros**
If application is read heavy, then instead of reading from master we can use slaves for reading databases and Insert queries can be executed on master which ultimately propagated to slaves
**Cons**
Still its a single point failure for writes

#### Problems

If there is some delay in sync between master and slave then we will get consistency issue, In most of distributed systems we are more worried about eventual consistency

Sometimes one master won't be sufficient if writes are more, Solution for this is...

### Sharding

Multiple master and multiple slaves

We have to do sharding only in case we are not able to handle write load on one machine

Split the write traffic on to multiple machines by adding more master servers and there will be read replicas for all master servers.

In this case, as long as our queries are based on the shard key queries are simple, But complexity comes if we are querying based on the non-shard key, In this case, we need to scatter query on all servers and gather the results.

To make distributions uniform and decrease data movement incase of adding/removing servers we will be using [Consistent Hashing](/Design/Consistent-Hashing.md)