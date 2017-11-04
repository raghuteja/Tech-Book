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

