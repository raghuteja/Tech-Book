# What is CDN, How to design CDN?

### CDN Functions

* Reduce Network traffic
* Serves client from the closest cache available and allowed to serve the content
* Serve client from the next closest cache if primary cache goes down

### What does CDN do?

Find the closest node and send the user there

**How to find closest node?**

1. DNS (Determines location of the resolver and chooses the closest location)
2. Anycast TCP