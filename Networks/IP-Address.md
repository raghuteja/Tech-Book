# IP Address

An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. An IP address serves two principal functions: host or network interface identification and location addressing.

### IPv4

An IPv4 an address consists of 32 bits which limits the address space to 2{% sup %}32{% endsup %} possible unique addresses

In early stages IP address will contain two parts : network number portion and host number portion. The highest order octet (most significant eight bits) in an address was designated as the network number and the remaining bits were called the rest field or host identifier and were used for host numbering within a network.

#### Classful Network Architecture

| Class | Leading bits | Size of network number bit field | Size of rest bit field | Number of networks | Addresses per network | Total addresses in class | Start address | End address |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |
| Class A | 0 | 8 | 24 | 128 (27) | 16,777,216 (224) | 2,147,483,648 (231) | 0.0.0.0 | 127.255.255.255 |
| Class B | 10 | 16 | 16 | 16,384 (214) | 65,536 (216) | 1,073,741,824 (230) | 128.0.0.0 | 191.255.255.255 |
| Class C | 110 | 24 | 8 | 2,097,152 (221) | 256 (28) | 536,870,912 (229) | 192.0.0.0 | 223.255.255.255 |
| Class D (multicast) | 1110 | not defined | not defined | not defined | not defined | 268,435,456 (228) | 224.0.0.0 | 239.255.255.255 |
| Class E (reserved) | 1111 | not defined | not defined | not defined | not defined | 268,435,456 (228) | 240.0.0.0 | 255.255.255.255 |


### Credits
1. [Wikipedia](https://en.wikipedia.org/wiki/Classful_network)