# ACID Transactions

**A : Atomicity**

Atomicity means that you can guarantee that all of a transaction happens, or none of it does

**C : Consistency**

Consistency means that you guarantee that your data will be consistent, i.e, system should not be corrupted

**I : Isolation**

Isolation means that one transaction cannot read data from another transaction that is not yet completed. If two transactions are executing concurrently, each one will see the world as if they were executing sequentially, and if one needs to read data that is written by another, it will have to wait until the other is finished.

**D: Durability**

Durability means that once a transaction is complete, it is guaranteed that all of the changes have been recorded to a durable medium (such as a hard disk)