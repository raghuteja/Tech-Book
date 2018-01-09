# Lamport and Vector Clocks

These two algorithms used to determine the order of events in a distributed computer system.

### Why not use physical timestamps?

In a distributed system, it is not possible in practice to synchronize time across systems. The clocks on different machines can vary quite a bit. You can only get the clocks accurate to within about a millisecond of each other. Hence, the entities can use the concept of a logical clock based on the events through which they communicate

### Causal Ordering

For any two events, A and B, if there’s any way that A could have influenced B, then the Lamport timestamp of A will be less than the Lamport timestamp of B. It’s also possible to have two events where we can’t say which came first; when that happens, it means that they couldn’t have affected each other. If A and B can’t have any affect on each other, then it doesn’t matter which one came first.

### Lamport timestamps

A Lamport clock may be used to create a partial causal ordering of events between processes. Given a logical clock following these rules, the following relation is true: if $$ a \rightarrow b$$ then $$ C(a) \lt C(b) $$ where $$\rightarrow$$ means happened-before.

This relation only goes one way, and is called clock consistency condition: if one event comes before another, then that event's logical clock comes before the other's. 

The strong clock consistency condition, which is two way if $$ C(a) \lt C(b) $$ then $$ a \rightarrow b$$ can be obtained by other techniques such as vector clocks

Using only a simple Lamport clock, only a partial causal ordering can be inferred from the clock

#### Algorithm

Each process maintains a single Lamport timestamp counter. Each event in the process is tagged with a value from this counter. The counter is incremented before the event timestamp is assigned.

* A process increments its counter before each event in that process
* When a process sends a message, it includes its counter value with the message
* On receiving a message, the counter of the recipient is updated, if necessary, to the greater of its current counter and the timestamp in the received message. The counter is then incremented by 1 before the message is considered received.

### Vector clocks



### Credits

* [Lamport and vector timestamps](https://www.cs.rutgers.edu/~pxk/417/notes/clocks/index.html)