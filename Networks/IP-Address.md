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

### Credits
1. [Wikipedia](https://en.wikipedia.org/wiki/Classful_network)