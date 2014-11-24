# Transport Layer

## Introduction and Transport-Layer Services

* logical communication
	* as if the hosts were directly connected
* what it does on the sending side
	* **break** the application-layer messages into chunks
	* **encapsulate** the chunks into network-layer segments
	* **pass** the segment to the network layer
* routers
	* routers **only act on network layer fields** of the datagram
	* ignorant of the info added by transport layer

### Relationship between transport and network layers

* transport-layer and network-layer
	* tranport layer provides logical connection between **process on hosts**
	* network-layer provides logical connection between **hosts**
* 类比
	* application messages = 信封里的信
	* processes = 大院里的人
	* hosts = 大院
	* transport-layer protocol = 值班室大爷
	* network-layer protocol = 邮政
* Service of transport-layer protocol is **constrianed** by what network-layer protocol provides
* Transport layer protocol can, however, add something else (within the constraint) e.g. error checking, encryption...

### Overview of the Transport Layer in the Internet

* **UDP**
	* User Datagram Protocol
	* Unreliable, connectionless service to applications
* **TCP**
	* Tranmission Control Protocol
	* Reliable, connection-oriented service to applications
* IP datagram, TCP/UDP segment (though some might use UDP *datagram*)
* **IP**
	* Internet Protocol
	* Provide logical communication between **hosts**
	* **best effort delivery service**
		* Best effort to deliver, but **no guarantees**
		* Not on delivery, order, integrity...
	* **unreliable service**
	* each host has an IP address
* **Responsiblity of UDP**
	1. Transport layer **multiplexing and demultiplexing**
		* Extend IP's **host-to-host** delivery service to **process-to-process** delivery
    2. **Integrity checking**
    	* Include error-detection fields in segment headers
* **Responsiblity of TCP**
	* What UDP offers
	* **Reliable data transfer**
		* flow control, sequence number, acknowledgements,  timers
		* Make sure the data is delivered **correctly and in order**
    * **Congestion Control**
    	* Not for the invoking application, but for the Internet as a whole
    	* Prevent any TCP connection swamping the links and routers
    	* Regulate the sending rate (UDP don't do that)

## Multiplexing and Demultiplexing


### Connectionless multiplexing and demultiplexing

### Connection-oriented multiplexing and demultiplexing

### Web servers and TCP

### Port scanning

## Connectionless Transport: UDP

### UDP Segment Structure

### UDP Checksum

## Principles of Reliable Data Transfer

### Building a Reliable Data Transfer Protocol

#### Over a perfectly reliable channel: rdt 1.0

#### With bit erros: rdt 2.0

#### Lossy channel + bit errors: rdt 3.0

### Pipelined Reliable Data Transfer Protocols

### Go-Back-N(GBN)

### Selective Repeat (SR)

## Connection-Oriented Transport: TCP

### The TCP connection

### TCP Segment Structure

#### Sequence numbers and acknowledgesment numbers

#### Telnet: A case study for sequence and acknowledgment numbers

### Roud-Trip Time Estimation and Timeout

#### Estimating the Round-Trip Time

#### Setting and Managing the Retransmission Timeout Interval

### Reliable Data Transfer

#### Scenarios

#### Doubling the Timeout Interval

#### Fast Retransmit

#### Go-Back-N or Selective Repeat?

### Flow Control

### TCP Connection Management

### SYN Flood Attack

## Principles of Congestion Control

### The Causes and the Costs of Congestion

#### Scenario 1: Two senders, a Router with Infinite Buffers

#### Scenario 2: Two senders, a Router with Finite Buffers

#### Scenario 3: Four senders, Routers with Finite Buffers, Multihop Paths

### Approaches to Congestion Control

### Network-Assisted Congestion-Control Example: ATM ABR Congestion Control

## TCP Congestion Control

#### Slow start

#### Congestion avoidance

#### Fast recovery

#### TCP Congestion Control: retrospective

#### Macroscopic description of TCP Throughput

#### TCP over high-bandwith paths

### Fairness

#### Fairness and UDP

#### Fairness and Parallel TCP Connections


