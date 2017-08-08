# Scaling datastore

### Read replication

Single master and multiple slaves

This is helpful only when we have lots and lots of reads when compared to writes

#### Problems

If there is some delay in sync between master and slave then we will get consistency issue, In most of distributed systems we are more worried about eventual consistency

Sometimes one master won't be sufficient if writes are more, Solution for this is...

### Sharding

