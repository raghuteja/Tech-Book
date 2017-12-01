# Garbage Collection in Java

Java uses mark and sweep method

As we know in mark and sweep method application need to be paused, If the memory is very high then application will be paused for longer time, So here are the improvisations for this

### Generational Hypothesis

Based on observations
1. Most of objects become unused quickly
2. Others will stay for longer time

So they divided Java VM into **Young Generation** and **Old Generation**(Tenured)

![](/assets/images/Java-Heap-Structure.png)

#### Eden

New objects are allocated in Eden space, Since there can be multiple threads possible Eden is further divided into Thread Local Allocation Buffer (TLAB)

Once TLAB allocation is not possible allocation moves to Eden shared space, If there is no enough space either then GC process inside young generation is triggered. If GC also does not result in sufficient free memory inside Eden, then the object is allocated in the Old Generation.

---

A generational tracing collector starts from the root set, but does not traverse references that lead to objects in the older generation, which reduces the size of the object graph to be traced. But this creates a problem, what if an object in the older generation references a younger object, which is not reachable through any other chain of references from a root?

##### Card Marking

A piece of code executed whenever a member variable (of a reference type) is assigned/written to. If the new reference points to a young object and it's stored in an old object, the write barrier records that fact for the garbage collect.

The heap is divided into a set of cards, each of which is usually smaller than a memory page. The JVM maintains a card map, with one bit (or byte, in some implementations) corresponding to each card in the heap. Each time a pointer field in an object in the heap is modified, the corresponding bit in the card map for that card is set.

So during writes
```
some_obj.field = other_obj;
```
```
card_table[(&old_obj - start_of_heap) >> K] = 1;
```

During minor GC, the garbage collector looks at the card table to determine which heap regions to scan for young pointers:
```
for i from 0 to (heap_size >> K):
    if card_table[i]:
        scan heap[i << K .. (i + 1) << K] for young pointers
```

---


After the marking phase is completed, all the live objects in Eden are copied to one of the Survivor spaces. The whole Eden is now considered to be empty and can be reused to allocate more objects. Such an approach is called "Mark and Copy": the live objects are marked, and then copied (not moved) to a survivor space.

#### Survivor Spaces

Two survivor spaces called from and to, Note that one of the two will always be empty

At the time of GC all objects are copied to empty survivor space and other space will become empty, JVM maintains two survivor spaces to address fragmentation.

This copying objects are done several times till the objects are old enough(survives after several GC runs), If they are old they will be promoted to old generation

Here compact phase is not required

#### Old Generation

GC in the Old Generation happens less frequently than in the Young Generation, Since most of objects in old are expected to live longer there won't be any mark and copy phase instead the objects are moved around for fragmentation

Here compact phase is required

#### Permanent Generation

It is used to store metadata such as classes

### Types of GC's

1. Minor - Happens in Young generation
2. Major - Happens in Old generation
3. Full - Happens in both generations

### Credits

1. [Oracle Java Garbage collection Basics](http://www.oracle.com/webfolder/technetwork/tutorials/obe/java/gc01/index.html)
2. [Plumbr](https://plumbr.eu/handbook/what-is-garbage-collection)
3. [Card Marking](http://stackoverflow.com/a/19155441/1465334)