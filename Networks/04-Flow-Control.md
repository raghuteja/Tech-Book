# Flow Control in Networks

### Delays in Networks

1. Transmission delay
2. Propagation delay
3. Queueing delay
4. Processing delay

#### Transmission delay

Equal to $$ Data to be transferred \over Bandwidth $$

#### Propagation delay

Equal to $$ Distance \over Velocity $$

Total time taken to send a packet from source to destination is $$ Transmission delay + Propagation delay $$

#### Queueing delay

At destination once the packets are arrived they will be placed in buffer and processed one by one, So the amount of time packet sits in buffer is queueing delay

#### Processing delay

Taking packet and one by one from buffer in destination side and processing it is called processing delay

In most of the cases Queueing delay and Processing delay is considered as negligible

### Stop and Wait Method

Sender will send a packet and after receiver comsumes that packet and sends acknowledgement, Then sender will send next packet

##### Possible scenarios and their solutions

1. If sender sends packet that got lost in the middle then sender will wait for ack and receiver will wait for packet (Deadlock) - Solution is timeout at sender side, If within the timeout sender doesnot get ack it will resend the packet again (ARQ - Automatic Repeat Request)
2. If ack is lost then after timeout sender will resend packet again, but at receiver we should know that its the same packet that got resent by sender - Solution is sequence number of packets
3. If ack is delayed, sender is going to send packet and again and receiver is going to send the ack again, If sender sends next packet then ack can come for previous packet - Solution is sequence number in ack's
