# Garbage Collection

Garbage collection (GC) is a form of automatic memory management.

### Manual Memory Management

Manually free up memory after completion of usage, Here there is a chance of memory leak

#### Problems with this approach

* **Dangling references**: It is possible to deallocate the space used by an object to which some other object still has a reference.
* **Space Leaks**: This occurs when memory is allocated and no longer referenced but is not released.

### Automated Memory Management

Automated Memory Management(Garbage Collection) solves both the problems mentioned in Manual memory management

Initial approach was reference counting

![](/assets/images/GC-Memory.png)

**Live Object** - Reachable (Referenced by someone else)
**Dead Object** - UnReachable (Unreferenced from any where)

### Steps

**Mark**
Starts from root node of application, walks the object graph, mark objects that are reachable as live

**Sweep (Delete)**
Delete unreachable objects

**Compact**
Compacting the memory moving around the objects and making allocation contiguous

Here cycles won't be leaked as above

One drawback in mark and sweep is application need to be paused while mark phase is going on, which will cause latency issues
During sweep phase application can run in parallel