# Design Search Typeahead

### Types of suggestions

* Autosuggest without accounting spelling mistakes
* Autosuggest even incase of spelling mistakes


* Personalized suggestions
* Common suggestions

Assume we need to suggest top 5 typeahead suggestions

We will be picking right suggestions based on priority/frequency

We are currently considering only "Autosuggest without accounting spelling mistakes" and "Non-Personalized suggestions"


### Design Goals

* Latency : Very important
* Consistency : Not really
* Availability : important

### API's for client

```
Read: List(string) getTopSuggestions(string currentQuery) 
Write: void updateSuggestions(string searchTerm)
```

Data structure best suited in this case is trie, since we are using prefixes always

At the application layer level we need to have multiple application servers and a load balancer on top of it to make it highly available, Data should be stored on other machines

### How read query work

It needs to fetch top five results with the given prefix, So bruteforce way will be to scan all the nodes in the subtree and find the 5 most frequent. If we do it like this we might end up traversing GB's of data nodes which is practically impossible for every read query because latency requirements won't match

We can overcome this problem by storing top 5 results under the node inside the node itself, In this way read queries will be much faster

### How write query work

Whenever we get an actual search term, we will traverse down to the node corresponding to it and increase its frequency, So when frequency of current node gets updated we might need to update its parent nodes top 5 results if it comes into that.

Store parent pointers to node

* Store frequencies and strings of top 5 in every node, This way we can compare and update top 5 of all parent nodes
* Store pointers to top 5 nodes in every node, This way we can update pointer if required in all parent nodes

In second option, read query results in 5 pointers and since we have parent pointer we need to traverse back and reverse to get actual 5 strings

### Efficiency read vs write

If writes are high then it might impact performance of reads also as we might need to lock the node to update values/pointers

* Sample write queries i.e, send one query for every 1000 queries
* Offline update (Might impact newly trending items)

### Distributed system

Here straight away answer will be assign a separate node for every brach at first level, Problem here is **Load Imbalance**

Other solution is shard further and keep shard size as small small chunks and assign multiple shards such that it fits in a machine

![](/assets/Search-Typeahead-Trie.svg)

As mentioned in above figure we store the top level nodes in one machines and bottom nodes i.e, shards we will store multiple shards in each machines (because shards data size might not be equally distributed)

**Read request flow : ** Read request enters at top level and inside top level of every node we will store machine id instead of pointer, Then we will send query to that machine

**Write request flow : ** When update request comes it will go similar to read request and update frequency, then we need to check parents if the new updated frequency matches with any of top 5 results in parents, So child will have parent pointer if it is in the same machine or parent machine id if its in other machine


To make database more available we might need to replicate the data

* Master-Slave replication
* Master-Master replication

**Master-Slave replication : ** Writes will go to master and log in change log files and read can go to both master and slave, Slave data will gets updated through change log files. Problem with this solution is write request is single point failure

**Master-Master replication : ** Writes can go through any of the machines but we need to eventually sync up all the replicated nodes which can be done through sending update request to all the other replicas or by anti-entropy using merkle trees, Reads also can go to any machine as we need only evantual consistency

### Credits

* [Interview Bit](https://www.interviewbit.com/problems/search-typeahead/)