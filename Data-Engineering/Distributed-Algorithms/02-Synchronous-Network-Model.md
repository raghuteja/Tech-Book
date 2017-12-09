# Synchronous Network Model

### Synchronous Network systems

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

**Halting States : ** A process in a halting state does not send messages, transits to the same state

**Variable start times : ** we might want to consider synchronous systems in which the processes might begin executing at different rounds, This can be modeled by 
* Adding a special node called environment node and having edges to all normal nodes
* Environment process sends wakeup messages when desired
* processes start in quiescent states, do not send messages
* They change state when receiving some wakeup message from environment node or other message

### Failures

* **Process stopping failure : ** A process can stop somewhere in its execution or can stop after sending a subset of the round messages

* **Process Byzantine failure :** Generate its next messages and next state in some arbitrary way, without necessarily following the rules specified by its message generation and state transition functions.

* **Channel failures : ** channels can fail by losing messages

### Inputs and Outputs

* Inputs are just possible values in designated
input variables
* Outputs are values in output variables
    * write-once variables, recording the first write operation
    * can be read multiple times
    
### Executions

* **Executions State assignment :** assignment of a state to each process
* **Message assignment :** assignment of message/null to each channel
* **Execution :** infinite sequence $$C_0, M_1, N_1, C_1, M_2, N_2, ...$$
    * $$C_i$$ state assignment after round $$i$$
    * $$M_i$$ message assignment, messages sent in round $$i$$
    * $$N_i$$ message assignment, messages received in round $$i$$
    * $$M_i \not = N_i$$ if there is message loss
* Executions $$e$$ and $$e^{'}$$ are indistinguishable to process $$i$$, denoted $$e \stackrel{i}{∼} e^{'}$$ if $$i$$ has the same sequence of states, outgoing and incoming messages in $$e$$ and $$e^{'}$$
* Executions can also be said to be indistinguishable to process $$i$$ up to $$r$$ rounds

### Complexity measures

* **Time complexity : ** Number of rounds until output produced or processes halt
* **Communication complexity : ** Total number of (non null) messages sent or number of bits in messages

### Randomization

It is useful to allow random choices, Model is augmented with random function
* $$rand_i$$ is added for each node $$i$$
* $$rand_i(s)$$ for state $$s$$ is a probability distribution over $$states_i$$

Each round starts now by a random choice of new a state, Executions become $$C_0, D_1, M_1, N_1, C_1, D_2, M_2, N_2, ...$$, $$D_r$$ represents state assignment after random choices in round $$r$$

In randomized systems, claims become probabilistic


### Credits

1. [Distributed Algorithms by Nancy A. Lynch](https://www.amazon.com/Distributed-Algorithms-Kaufmann-Management-Systems/dp/1558603484)