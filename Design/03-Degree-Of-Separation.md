# Design Degree of separaion

### Determine degree of separation between two people in Facebook/LinkedIn

Assume the data structure as a graph where person as node of graph and friendship as an edge, Now the problem reduces to finding the shortest path between two nodes in a graph

Two ways to do it

* DFS
* BFS

#### DFS

Friend graphs in social networks tend to be shallow but broad, So here, BFS is clearly better than DFS, because DFS will take a lot longer to discover the destination node

#### BFS

**Single direction BFS**

So you can start a Node A and traverse the graph looking for Node B, counting the edges as you go.

To illustrate, let's assume naively that each person anywhere in the population has 100 friends and in this particular case all the friends are distinct.

So Person A has 100 friends, who then have 10K friends, who then have a million friends. If Person B is somewhere in the A's third-degree then we have to search person B in that million friends.

**Double direction BFS**

Person A has 100 friends who then has 10K friends and similarly Person B has 100 friends who then has 10K friends, Then we just need to find if there are any common people that are there in both 10K sets

Now the data size got reduced by a huge amount

#### Scaling up

Since in real scenario there can be a lot more friends who may not be able to fit in single machine, So we might need to use distributed system

We can split the tasks of double direction BFS and do it asynchronously

#### Map-Reduce

List of mutual friends between two friends is the most common feature and every time we cannot compute this for each and every one

We can apply map-reduce and precompute mutual friends between any two firends

Input for mapper : key as person and value as list of friends to that person
Output from mapper/Input for reducer : key as a tuple of two friends and value as list of friends
Input for reducer : Key as a tuple of two friends and value as common friends between those two friends

Check out [this](http://stevekrenzel.com/finding-friends-with-mapreduce) to see with example

### Credits

* [Complete credits goes to Tim-HR](https://github.com/tim-hr/stuff/wiki/System-design:-Calculate-degrees-of-separation)
* [Credits to map-reduce logic goes to Steve](http://stevekrenzel.com/finding-friends-with-mapreduce)