# CAP Theorem

CAP Theorem states that, in a distributed system you can only have two out of the following three guarantees across a read/write pair, one of them must be sacrificed. 

1. Consistency
2. Availability
3. Partition Tolerance

**Consistency **

A read is guaranteed to return the most recent write for a given client.

**Availability**

A non-failing node will return a response.

**Partition Tolerance**

The system will continue to function when network partitions occur i.e, two nodes can't talk to each other but there are clients able to talk to either one or both of those nodes.

In distributed computing we have to keep in mind that networks aren't completely reliable


![](/assets/CAP_Theorem.png)


# Credits

1. [Image taken from ResearchGate](https://www.researchgate.net/figure/282519669_fig1_Figure-1-CAP-theorem-with-databases-that-choose-CA-CP-and-AP)