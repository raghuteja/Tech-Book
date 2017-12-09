# Synchronous Network Model

* Collection of processes at nodes of a directed graph
* Start with some initial state
* Can send message to neighbors along edges (channels)
* Can receive messages from neighbors
* Proceed in lockstep doing rounds

#### Notation of graph

* $$G = (V, E)$$
* $$n$$ = $$|V|$$
* $$out-nbrs_i$$ = outgoing neighbors of node $$i$$
* $$in-nbrs_i$$ = incoming neighbors of node $$i$$
* $$distance(i, j)$$ = shortest path from node $$i$$ to node $$j$$
* $$diameter$$ = maximum of $$distance(i, j)$$ over all pairs of $$(i, j)$$
* $$M$$ = fixed message alphabet
* $$states_i$$ = set of states for node $$i$$, need not be finate
* $$start_i$$ = non empty subset of $$states_i$$ known as initial states
* $$msgs_i$$ = message generation function mapping $$states_i$$ $$out-nbrs_i$$ to elements of $$M \cup \{null\}$$
* $$trans_i$$ = state transition function mapping $$states_i$$ $$in-nbrs_i$$ to elements of $$M \cup \{null\}$$ to $$states_i$$


Execution starts with all the processes in arbitrary start states and with channels empty. Processes repeat rounds in lockstep, consisting of two steps

1. Apply the message generation function to the current state to generate the messages to be sent to all outgoing neighbors. Put these messages in the appropriate channels.
2. Apply the state transition function to the current state and the incoming messages to obtain the new state. Remove all messages from the channels.

Model is deterministic, So starting states determine all execution

### Credits

1. [Distributed Algorithms by Nancy A. Lynch](https://www.amazon.com/Distributed-Algorithms-Kaufmann-Management-Systems/dp/1558603484)