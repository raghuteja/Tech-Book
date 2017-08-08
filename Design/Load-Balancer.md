# Load Balancer

Load balancing improves the distribution of workloads across multiple computing resources

Two Types

**Layer - 4** 

Uses information defined at the networking transport layer (Layer 4) as the basis for deciding how to distribute client requests across a group of servers.

Act upon data found in network and transport layer protocols

**Layer - 7**

Distribute requests based upon data found in application layer protocols such as HTTP


Requests are distributed to a particular server based on a configured algorithm.

Some of standard algorithms are

1. Round robin
2. Weighted round robin
3. Least connections
4. Least response time

Layer 7 load balancers can further distribute requests based on application specific data such as HTTP headers, cookies, or data within the application message itself, such as the value of a specific parameter.

