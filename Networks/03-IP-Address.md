# IP Address

An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. An IP address serves two principal functions: host or network interface identification and location addressing.

### IPv4

An IPv4 an address consists of 32 bits which limits the address space to 2{% sup %}32{% endsup %} possible unique addresses

In early stages IP address will contain two parts : network number portion and host number portion. The highest order octet (most significant eight bits) in an address was designated as the network number and the remaining bits were called the rest field or host identifier and were used for host numbering within a network.

#### Classful Network Architecture

| Class | Leading bits | Size of n/w number bit field | Size of rest bit field | No.of n/w | Addresses per n/w | Start address | End address |
| -- | -- | -- | -- | -- | -- | -- | -- |
| Class A | 0 | 8 | 24 | 2{% sup %}7{% endsup %} | 2{% sup %}24{% endsup %} | 0.0.0.0 | 127.255.255.255 |
| Class B | 10 | 16 | 16 | 2{% sup %}14{% endsup %} | 2{% sup %}16{% endsup %} | 128.0.0.0 | 191.255.255.255 |
| Class C | 110 | 24 | 8 | 2{% sup %}21{% endsup %} | 2{% sup %}8{% endsup %} | 192.0.0.0 | 223.255.255.255 |
| Class D (multicast) | 1110 | ND | ND | ND | ND | 224.0.0.0 | 239.255.255.255 |
| Class E (reserved) | 1111 | ND | ND | ND | ND | 240.0.0.0 | 255.255.255.255 |

n/w = network, ND = Not Defined

The number of addresses usable for addressing specific hosts in each network is always 2{% sup %}N{% endsup %} - 2, where N is the number of rest field bits, and the subtraction of 2 adjusts for the use of the all-bits-zero host portion for network address and the all-bits-one host portion as a broadcast address.

### Casting

#### Unicast

Sending packet from one host to one particular host

#### Broadcast

Sending packet from one host to multiple hosts

##### Limited Broadcast

Broadcasting packet from one host to all other hosts in the same network (IP : 255.255.255.255)

##### Directed Broadcast

Broadcasting packet from one host to all hosts in other network (IP : Last IP of the network)

### Subnetwork

A subnetwork or subnet is a logical subdivision of an IP network. The practice of dividing a network into two or more networks is called subnetting.

![](/images/Subnetting_operation.svg)

##### Example subnet

Class C Network (200.1.2.0)
Suppose this class C network need to be divided into two equal parts, Then the subnetworks will be 

1. 200.1.2.0 - 200.1.2.127
2. 200.1.2.128 - 200.1.2.255

Similar to actual network, Subnetwork will also have network ID and Directed broadcast IP for then network

![](/images/Subnetting-Example.png)

### Routing

For a given IP address router needs to decide through which interface it should send?

For that reason we have **subnet mask** 

##### Subnetmask

Subnetmask contains 1's and 0's, Number of 1's represents Network ID part and subnet ID part, Number of 0's represent Host ID part

For the above example subnet mask will be 255.255.255.128

Use of it is for any given IP address if we **and** it with subnet mask the output will be network ID of network with which the IP belongs to

For maintaining this table router will maintain some data called routing table

Routing table for the above example

| Network ID | Subnet Mask | Interface |
| -- | -- | -- |
| 200.1.2.0 | 255.255.255.128 | A |
| 200.1.2.0 | 255.255.255.128 | B |
| 0.0.0.0 | 0.0.0.0 | C |

If there is more than one match then choose the one with the largest subnet mask

Similar to above example there can be variable length subnetting.

### CIDR (Classless Interdomain Routing)



### Credits
1. [Wikipedia - Classful Network](https://en.wikipedia.org/wiki/Classful_network)
2. [Wikipedia - Subnetwork](https://en.wikipedia.org/wiki/Subnetwork)
