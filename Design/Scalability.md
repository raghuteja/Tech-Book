# Scalability

### Vertical Scaling

It is the ability to increase the capacity of existing hardware or software by adding resources - for example, adding processing power to a server to make it faster.

### Horizontal Scaling

Servers of a scalable web service are hidden behind a load balancer, which evenly distributes load onto group of application servers which typically called **Load Balancer**.

##### How Load Balancer decides which application server to choose?

1. By Load (How busy the server is?)
2. Round-Robin

##### Problems in horizontal scaling
 
1. A single server can get huge number of heavy requests
2. Maintaining sessions, When user logged in it might goes to server1 and maintains session in that server, when he does another request he might be landed in other server where the session itself is not there

So we should not store any user-related data, like sessions or profile pictures, on local disc or memory.

That data need to be stored in a centralized data store which is accessible to all your application servers. It can be an external database or persistent cache, like Redis. An external persistent cache will have better performance than an external database.

Then our persistent storage becomes a single point failure, We can overcome this by Keeping another copy of that which will be called replication in technical terms

### Mysql Scaling

Over the time even if you do that your application gets slower and slower and finally breaks down. The reason is your database. Do master-slave replication \(read from slaves, write to master\) and upgrade your master server by adding RAM.

### Caching

When a lot of data is fetched from the database page rendering might be slow. Here where cache comes into picture

A cache is a simple key-value store and it should reside as a buffering layer between your application and your data storage. Whenever your application has to read data it should at first try to retrieve the data from your cache. Only if it’s not in the cache should it then try to get the data from the main data source.

#### DB Query Caching

When you do a query to your database, you store the result dataset in cache. A hashed version of your query is the cache key. The next time you run the query, you first check if it is already in the cache. The next time you run the query, you check at first the cache if there is already a result. This pattern has several issues. The main issue is the expiration ([See MySQL Caching](Design/MySQL-Caching.md))

#### Object Caching

Cache data that fetched from db as objects which are instances of classes

### Async Calls

#### Option \#1

Using Cron

#### Option \#2

Using Job queue

To maintain job queue we need a reliable message queueing system \(rabbitmq\)

### Credits

* [Scalability Blog](http://www.lecloud.net/tagged/scalability)

