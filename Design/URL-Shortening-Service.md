# Implementing URL Shortening Service

Given a URL, We need to find hash function F that maps URL to a short alias `F(URL) = alias` and satisfies following conditions

1. Each URL can only be mapped to a unique alias
2. Each alias can be mapped back to a unique URL easily

The above function F is a Bijective Function.

The second condition is the core as in the run time, the system should look up by alias and redirect to the corresponding URL quickly.

### Basic Solution

For every given URL, generate a random alias and store it in datastore, In runtime we will lookup in datastore by alias, get corresponding URL and redirect to that URL, The main problem here is performance.

If there are already a milion records and we want to insert a new record the database needs to go look at the correct page for this alias. However, when using incremental IDs, insertion can be much easier, It will just go to the last page.

One downside is using incremental ids will make mapping less flexible if the system allows users to set custom short URL, From performance perspective we are going to use incremental ID's.

##### Converting given long url to alias

First convert given long url to some long integer by using hashing or by mysql auto increments and then convert id to alias

* If that url already exists in datastore ignore it, No need to shorten it again
* Think of an alphabet we want to use. In your case that's `[a-zA-Z0-9]`. It contains _62 letters_.
* Then convert that long integer to base 62

##### Converting given alias to long url

* Convert short url 62 base key to base 10 long integer
* Find the corresponding long url in datastore for the given long integer

### Offline key generation

We can have a Offline Key Generation Service that generates random six letter strings beforehand and stores them in a database. Whenever we want we will just take one of the already generated keys and use it. This can be faster compared to above because we will not be encoding the URL. Service can make sure all the keys inserted are unique.

Here we need to keep track of two sets of keys used and unused, To make it faster we can load some part of unused key set and load in memory. When we want to encode an url we just need to pick one from unused set loaded in memory and mark it as used and store that key and url in some datastore

To handle more QPS we can horizontally scale this key generation service and grant some part of keys to each generation service, so that we won't have any clash in keys

### Data storage

A single machine may not be capable to store all the mappings. How do we scale with multiple instances? We need a distributed key value store

#### Partitioning schemes

##### Range based partition

Partitioning based on range i.e, all urls starting with 'a' will go to one server and all 'b' s will go to another.

This way the data can be skewed

##### Hash based partition

Hash the key and store it in corresponding server by using the hash output. This can also leads the data in skewed form i.e, overloaded partitions. Solution to this is [Consistent Hashing](/Design/Consistent-Hashing.md)

#### Distributed key-value stores

* Aerospike
* Amazon's Dynamo

### How to get shortened URL to original URL faster

If certain URL's are getting accessed faster, we can keep those set of url's in cache for faster access.

We can have the cache eviction policy as [LRU (Least Recently Used)](/Data-Structures/LRU-Implementation.md)

### Credits

* [Design tinyurl](http://blog.gainlo.co/index.php/2016/03/08/system-design-interview-question-create-tinyurl-system/)
* [Educative](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5668600916475904)

