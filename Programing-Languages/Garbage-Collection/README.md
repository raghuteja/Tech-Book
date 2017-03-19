# Garbage Collection

Garbage collection (GC) is a form of automatic memory management.

### Manual Memory Management

Manually free up memory after completion of usage, Here there is a high probability of memory leak

### Automated Memory Management

Initial approach was reference counting

![](/images/GC-Memory.png)

**Live Object** - Reachable (Referenced by someone else)
**Dead Object** - UnReachable (Unreferenced from any where)

### Steps

**Mark**
Starts from root node of application, walks the object graph, mark objects that are reachable as live

**Sweep (Delete)**
Delete unreachable objects

**Compact**
Compacting the memory moving around the objects and making allocation contiguous