# Garbage Collection

Garbage collection (GC) is a form of automatic memory management.

**Live Object** - Reachable (Referenced by someone else)
**Dead Object** - UnReachable (Unreferenced from any where)

### Steps

**Mark**
Starts from root node of application, walks the object graph, mark objects that are reachable as live

**Sweep (Delete)**
Delete unreachable objects

**Compact**
Compacting the memory y moving around the objects and making allocation contigeous