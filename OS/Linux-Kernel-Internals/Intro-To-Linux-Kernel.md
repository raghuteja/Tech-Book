# Intro to Linux Kernel

####Tasks Performed By Kernel

1. Process Scheduling
2. Memory Management (RAM and Swap Space)
3. Provision of a file system
4. Creation and Termination of a Process
5. Access to devices (Keyboard, Mouse etc...)
6. Networking
7. Provision of a systemcall API

Application in system communicate via system calls, When an application executes a system call, we say that the kernel is executing on behalf of the application. Furthermore, the application is said to be executing a system call in kernel-space, and the kernel is running in **process context**.

kernel also manages the system's hardware through interrupts. When hardware wants to communicate with the system, it issues an interrupt that literally interrupts the processor, which in turn interrupts the kernel. A number identifies interrupts and the kernel uses this number to execute a specific interrupt handler to process and respond to the interrupt. (Ex: Keyboard)

Interrupt handlers do not run in a process context. Instead, they run in a special **interrupt context** that is not associated with any process. This special context exists solely to let an interrupt handler quickly respond to an interrupt, and then exit.

Each processor is doing exactly one of three things at any given moment

1. In user-space, executing user code in a process
2. In kernel-space, in process context, executing on behalf of a specific process
3. In kernel-space, in interrupt context, not associated with a process, handling an interrupt