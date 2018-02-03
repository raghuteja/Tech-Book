# Zero Copy data transfer

Improving the performance of I/O-intensive applications

Zero copy lets you avoid redundant data copies between intermediate buffers and reduces the number of context switches between user space and kernel space.

### Steps involved in sending file to Socket in general

1. Read data from the storage media to the page cache in an OS
2. Copy data in the page cache to an application buffer
3. Copy application buffer to another kernel buffer
4. Send the kernel buffer to the socket

Includes 4 data copying and 2 system calls

On Linux and Unix OS there exists a sendfile API that can directly transfer bytes from a file channel to a socket channel

This typically avoids 2 of the copies and 1 system call introduced in steps (2) and (3).

### Credits

1. [IBM](https://www.ibm.com/developerworks/linux/library/j-zerocopy/j-zerocopy-pdf.pdf)
