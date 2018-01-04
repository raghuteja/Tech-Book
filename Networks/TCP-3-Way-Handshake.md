# TCP 3 Way Handshake

TCP's three way handshaking technique is often referred to as "SYN-SYN-ACK" (or more accurately SYN, SYN-ACK, ACK) because there are three messages transmitted by TCP to negotiate and start a TCP session between two computers.

### Event Timeline

1. Host A sends a TCP SYNchronize packet to Host B
2. Host B receives A's SYN
3. Host B sends a SYNchronize-ACKnowledgement
4. Host A receives B's SYN-ACK
5. Host A sends ACKnowledge
6. Host B receives ACK. 
7. TCP socket connection is ESTABLISHED.

SYNchronize and ACKnowledge messages are indicated by a either the SYN bit, or the ACK bit inside the TCP header, and the SYN-ACK message has both the SYN and the ACK bits turned on (set to 1) in the TCP header.

### Teardown

When the communication between two computers ends, another 3-way communication is performed to tear down the TCP socket connection

### Credits

1. [TCP - 3 way handshake](http://www.inetdaemon.com/tutorials/internet/tcp/3-way_handshake.shtml)