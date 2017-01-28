# QPS Monitoring and Request Throttling

### QPS Monitoring

QPS Monitoring can be done by maintaining a count of how many requests came into the system in a second.

##### How to maintain count?

1. Count can be maintained in some In Memory datastore(Redis/Aerospike). But by using In Memory datastore latency might increase because of IO's.
2. Count can be maintained in a shared map with current time in second as key and **expire map keys older than some caching time**, Updating count can be done using
  1. For Nginx, we can use shared dictionaries
  2. Others By Atomic operations or Read-Write Locks
3. Instead of maintaining count for current second we can maintain the count for last one second, Here no need to use a map, This can be done by
  1. Incrementing value when request gets in
  2. Decrementing value after one second, How to do decrement after one second? - Some languages support execution of function call after specific amount of time (Ex : Golang)

##### What is QPS value?

**For Points 1&2:** QPS value we should not return as the number of requests in current second because the second may not have completed yet. So for QPS value we should return the average  value over last few seconds.

**For Point 3:** QPS value is just returning the variable


### Request Throttling

Whenever the request enters into the system if the current QPS is grater than the threshold QPS then we can drop that request else serve that request