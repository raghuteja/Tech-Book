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

#### Converting given long url to alias

First convert given long url to some long integer by using hashing or by mysql auto increments and then convert id to alias

* If that url already exists in datastore ignore it, No need to shorten it again
* Think of an alphabet we want to use. In your case that's `[a-zA-Z0-9]`. It contains _62 letters_.
* Then convert that long integer to base 62

#### Converting given alias to long url

* Convert short url 62 base key to base 10 long integer
* Find the corresponding long url in datastore for the given long integer

### Data storage

A single machine may not be capable to store all the mappings. How do we scale with multiple instances? We need a distributed key value store

#### Distributed key-value stores

* Aerospike
* Amazon's Dynamo

### Credits

* [Design tinyurl](http://blog.gainlo.co/index.php/2016/03/08/system-design-interview-question-create-tinyurl-system/)

