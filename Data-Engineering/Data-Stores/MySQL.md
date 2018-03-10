# MySQL

### Caching

On a typical MySQL Server in my.cnf there is a variable called `query_cache_type` which takes values `0` or `1` 

So first time you executes a query it might take longer time but from next time it got executed when the query cache is one and rows have not changed, Then response is going to come back much more quickly

One can use memcache(Memory Cache) which is another layer of cache between application server and database layer. Facebook uses memcache heavily


### Replication

Master sends all changes to another slave and the slave tries to apply all changes to keep up-to-date with the master

1. Whenever the master's database is modified, the change is written to a file called binlog. This is done by the client thread that executed the query that modified the database.
2. Dump thread in master continuously reads the master's binlog and sends it to the slave.
3. IO thread in slave receives the binlog that the master's dump thread sent, and writes it to a file called relay log.
4. SQL thread in slave continuously reads the relay log and applies the changes to the slave server.

#### BinLog Formats

Binlog format in Mysql can be controlled by a session variable `@@session.binlog_format` which can take three possible values `STATEMENT`, `ROW`, `MIXED`

##### Statement based logging

SQL query is written to the binlog in text

##### Row based logging

Rows that changed are written to the binlog in a binary format. Each row may consist of a Before Image (BI) and/or an After Image (AI).

* Write_rows_log_event: adds a new row to a table. Has only AI.
* Update_rows_log_event: modifies an existing row in a table. Has both BI and AI.
* Delete_rows_log_event: removes an existing row from a table. Has only BI.

The sets of columns recorded in the BI and AI are determined by the value of binlog_row_image. To specify the sets of columns, PKE (for Primary Key Equivalent) is defined as follows

* If a PK exists, the PKE is equal to the PK.
* Otherwise, if there exists a UK where all columns have the NOT NULL attribute, then that is the PKE (if there are more than one such UKs, then one is chosen arbitrarily).
* Otherwise, the PKE is equal to the set of all columns.

##### Mixed

With mixed logging format, the server automatically switches from statement-based to row-based logging under the some conditions. More on this can be found [here](https://dev.mysql.com/doc/refman/5.7/en/binary-log-mixed.html)

### Difference between InnoDB and MyISAM (Storage engines in MySQL)

1. Major difference is InnoDB implements row-level lock where as MyISAM can do only a table-level lock.
2. InnoDB implements transactions, foreign keys and relationship constraints, MyISAM does not.

### Credits

1. [MySQL Documentation](https://dev.mysql.com/doc/internals/en/replication.html)