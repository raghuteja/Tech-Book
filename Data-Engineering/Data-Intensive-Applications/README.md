# Data-Intensive Applications

What data intensive applications need?

1. **Databases** : Store data for future reference
2. **Caches** : Remember the result of an expensive operation
3. **Search Indexes** : Search data by keyword or filter
4. **Stream Processing** : Send a message to another process
5. **Batch Processing** : Periodically crunch a large amount of accumulated data

If you have an application-managed caching layer (using Memcached or similar), or a full-text search server (such as Elasticsearch or Solr) separate from your main database, it is normally the application code’s responsibility to keep those caches and indexes in sync with the main database.

### Questions

* How do you ensure that the data remains correct and complete, even when things go wrong internally? 
* How do you provide consistently good performance to clients, even when parts of your system are degraded? 
* How do you scale to handle an increase in load? 
* What does a good API for the service look like?

To answer the above questions we need to focus on three concerns that are important in most software systems.

1. Reliability
2. Scalability
3. Maintainability

### Credits

1. [Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems](https://www.amazon.in/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/9352135245/ref=tmm_pap_swatch_0)