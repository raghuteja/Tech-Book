# DNS (Domain Name Server)

A Domain Name System (DNS) translates a domain name to an IP address.

Your router or ISP provides information about which DNS server(s) to contact when doing a lookup. Lower level DNS servers cache mappings, which could become stale due to DNS propagation delays. DNS results can also be cached by your browser or OS for a certain period of time, determined by the time to live (TTL).

Some DNS services can route traffic through various methods:

1. Weighted round robin
2. Latency-based
3. Geolocation-based

### Architecture

DNS architecture is a hierarchical distributed database

1. Querying and Updating the database.
2. Replicating the information in the database among servers

The DNS domain namespace, as shown in the following figure, is based on the concept of a tree of named domains.

![](/assets/images/How-DNS-Works.jpg)

#### DNS Database distribution

A DNS database can be partitioned into multiple zones. A zone is a portion of the DNS database that belong to the contiguous portion of the DNS namespace. A single DNS server can be configured to more than one zones.

#### DNS Database replication

There can be multiple zones representing the same portion of the namespace

1. Primary : Zone to which all updates for the records that belong to that zone are made
2. Secondary : Read-only copy of the primary zone

#### DNS Querying

1. Recursive : DNS server must contact any other DNS servers it needs to resolve the request
2. Iterative : DNS server is expected to respond with the best local information it has, based on what the DNS server knows from local zone files or from caching

#### Time-To-Live

Indicates a length of time used by other DNS servers to determine how long to cache information for a record before expiring and discarding it.

If the TTL is short, it increases utilization of DNS servers and network traffic. 
If the TTL is long, the cached responses could become outdated.

### Credits

1. Content taken from [Microsoft](https://technet.microsoft.com/en-us/library/dd197427\(v=ws.10\).aspx)
2. Image Credits - [GoHacking](https://www.gohacking.com/)
