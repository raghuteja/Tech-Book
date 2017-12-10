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
* Uses comparisons on UIDs ($$u$$)

Each process sends its identifier around the ring. When a process receives an incoming identifier, it compares that identifier to its own. 

1. If the incoming identifier is greater than its own, it keeps passing the identifier. 
2. If it is less than its own, it discards the incoming identifier.
3. If it is equal to its own, the process declares itself the leader.

Fromally

$$M$$ = set of UIDs

$$states_i$$
* $$send \in M \cup \{null\}$$, initially $$u$$
* $$status \in \{unknown, leader\}$$, initially $$unknown$$

$$start_i$$ consists of the single state defined by the given initializations.

$$msgs_i$$ send the current value of send to $$i+1$$

$$trans_i$$

```
send := null
if the incoming messsage is v, then
    v > u: send := v
    v = u: status := leader
    v < u: do nothing
```

Output after $$n$$ rounds
* Process $$i_max$$ outputs leader by the end of round $$n$$.

#### Halting

We can modify above algorithm by allowing the elected leader to initiate a special report message to be sent around the ring. Any process that receives the report message can halt, after passing it on and set itself as non-leader

#### Complexity analysis

Time complexity - $$O(n)$$
Communication complexity - $$O(n^2)$$


### HS Algorithm

* Assumes bidirectional ring
* Does not rely on knowing the size of the ring
* Only the leader performs output
* Uses comparisons on UIDs ($$u$$)

Processes operate in phases $$0, 1, 2, ...$$. In each phase, processes send token with UID in both directions. Tokens in phase $$l$$ intend to travel $$2^l$$ and turn back to sender

1. If a received UID is greater than self UID, it is relayed on
2. If it is smaller, it is discarded
3. If it is equal, the process outputs leader

Formally

$$M$$ is the set of triples consisting of a UID, a flag value in $$\{out, in\}$$, and a positive integer $$hop-count$$.

$$states_i$$
* $$u$$ of type UID, initially $$i$$'s UID
* $$send+ \in M \cup \{null\}$$, initially $$i$$'s UID, out, 1
* $$send- \in M \cup \{null\}$$, initially $$i$$'s UID, out, 1
* $$status \in \{unknown, leader\}$$, initially $$unknown$$
* $$phase$$ non negative integer, initially 0

$$start_i$$ consists of the single state defined by the given initializations.

$$msgs_i$$ 
* send the current value of $$send+$$ to $$i+1$$
* send the current value of $$send-$$ to $$i-1$$

$$trans_i$$

```
send+ := null
send- := null
if the message from i-1 is (v, out, h) then
    v > u and h > 1: send+ := (v, out, h-1)
    v > u and h = 1: send- := (v, in, 1)
    v = u: status := leader
if the message from i+1 is (v, out, h) then
    v > u and h > 1: send- := (v, out, h-1)
    v > u and h = 1: send+ := (v, in, 1)
    v = u: status := leader
if the message from i-1 is (v, in, 1) and  v != u then
    send+ := (v, in, 1)
if the message from i-1 is (v, in, 1) and  v != u then
    send- := (v, in, 1)
if the messages from i-1 or i+1 is (u, in, 1) then
    phase := phase + 1
    send+ := (u, out, 2**phase)
    send- := (u, out, 2**phase)
```

#### Complexity analysis

Check out the book provided below

#### Correctness

* A process with UID $$u$$ only outputs leader when a message started at $$u$$ travels the whole ring and arrives back at $$u$$.
* At most one process can become leader: the one with the maximum UID.


### 