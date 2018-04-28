# Java Concepts

### Final in Java

* `final` class cannot be inherited
* `final` method cannot be overridden
* `final` variable value cannot be changed

### Finally in Java

Java `finally` block is a block that is used to execute important code such as closing connection, stream etc. It is always executed whether exception is handled or not. Java finally block follows try or catch block.

### Finalize in Java

The `java.lang.Object.finalize()` is called by the garbage collector on an object when garbage collection determines that there are no more references to the object. A subclass overrides the finalize method to dispose of system resources or to perform other cleanup.