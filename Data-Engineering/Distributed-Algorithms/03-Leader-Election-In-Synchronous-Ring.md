# Leader election in synchronous ring

A network graph of nodes 1 to n clock wise, Nodes do not need to know about their or neighbors numbers, But they are able to distinguish about clock wise and anti clock wise neighbors

Problem is selecting unique leader among themselves

#### Types of problems

* Ring can be uni-directional or bi-directional
* Number of nodes(n) can be known or unknown
* Processes can be identical or can be distinguished by UID

### Identical Processes

**Theorem : ** Let $$A$$ be a system of $$n$$ processes, $$n > 1$$, arranged in a bidirectional ring. If all the processes in $$A$$ are identical, then $$A$$ does not solve the leader-election problem.

**Intuition :** By symmetry, what one does, so do the others

Cannot find leader in identical process because of symmetry, To break symmetry, one solution is UID's

### LCR Algorithm

* Assumes only unidirectional ring
* Does not rely on knowing the size of the ring
* Only the leader performs output
* Uses comparisons on UIDs

Each process sends its identifier around the ring. When a process receives an incoming identifier, it compares that identifier to its own. 

1. If the incoming identifier is greater than its own, it keeps passing the identifier. 
2. If it is less than its own, it discards the incoming identifier.
3. If it is equal to its own, the process declares itself the leader.

As defined above

$$M$$ = set of UIDs