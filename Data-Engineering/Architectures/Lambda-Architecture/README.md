# Big-Data: Principles and best practices

Lets build a simple application which tracks the number of pageviews for any URL and returns top 100 URL's

**Problem : ** Started with the traditional database as the requests got increased we will start getting timeouts from DB as it cannot keep up the load

**Solution : ** Instead of updating every request at a time we can maintain queue and do batch updates

**Problem : ** As the requests increases doing batch updates also may not be able to scale well 

**Solution : ** We then selected a write heavy database which supports sharding so that we can spreads the write load across multiple machines (Shard key can be hash of URL in current scenario)

**Problem(s) : ** 

* As the application grows you need to reshard the database very frequently to keep up with the write load, managing that impractical
* Fault tolerant issue (What if one of the shard goes down?)
* Data corruption issue (What if because of some human error you updated counts wrongly in database), How to fix it?

**Solution : ** 

* In Distributed databases things like sharding and replication are handled for you
* Core technique is data is immutable, instead of storing counts store the raw data (This is helpful in case of human fault tolerance)

**Problem : ** We can store raw data and use distributed database so that all the above problems will be solved, But what about the queries on that raw data which will take longer time (We should take care of latency on queries also)

**Solution : ** Lambda Architecture

### What is Lambda Architecture

Lambda architecture is a data-processing architecture designed to handle massive quantities of data by taking advantage of both batch and stream-processing methods.

### Complete Credits

1. [Big Data: Principles and best practices of scalable realtime data systems](https://www.amazon.in/Big-Data-Principles-Practices-Real-Time/dp/9351198065)