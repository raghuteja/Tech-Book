# Design Search Typeahead

### Types of suggestions

* Autosuggest without accounting spelling mistakes
* Autosuggest even incase of spelling mistakes


* Personalized suggestions
* Common suggestions

Assume we need to suggest top 5 typeahead suggestions

We will be picking right suggestions based on priority/frequency


### Design Goals

Latency : Very important
Consistency : Not really
Availability : important

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

To make database more available we might need to replicate the data

### Credits

* [Interview Bit](https://www.interviewbit.com/problems/search-typeahead/)