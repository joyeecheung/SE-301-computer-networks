# 计网 CH1

##什么是Internet?

###以组成来看

一个连接起世界各地的计算设备的计算机网络（Internet is a computer network that interconnects hundreds of millions of computing devices throughout the world.）

####硬件
####Hosts/End systems

* 连接到Internet的设备
* End systems 以 **communication links** 和 **packet switches** 互联

####Packet switch

* 将 packet **转发（forwards）** 到它的目的地的设备。
* **分类**
    * **路由器（Routers）**: 通常放置在 access networks
    * **链路层交换机（Link-layer switches）**: 通常放置在 network core

####Route/Path
The sequence of communication links and packet switches traversed by a travelling packet.

####Transmission rate

* Rate at which communication links transmit data.

####一段数据的旅程

* The sending end system **segments** the data
* Adds **header** bytes to each segment -- **packets**
* Packets will be **reassembled** into the original data by the destination end system.

####ISP

* Internet Service Providers
* A ISP is in itself **a network of packet switches and communication links**

* **分类**
    * Residential ISP: 本地的有线电视/电话公司
        * e.g. 电信，联通，移动
    * Corporate ISP/University ISP
    * WiFi ISP
* **结构**
    * Lower-tier ISPs are interconnected through national and international upper-tier ISPs
    * ISP network 的特性
        * 本身可独立工作
        * 使用IP协议
        * 遵循一定的命名和寻址惯例

####Protocols

* run by end systems, packet switches and other pieces of the Internet to **control the sending and recieving of information**.

* **Big names**
    * **TCP**: Transmission Control Protocol
    * **IP**: Internet Protocol
        * 规定 packets 的格式
    * Together: **TCP/IP**

####Internet standards

* **Internet standards** are develop by **IETF**(Internet Engineering Task Force) and documented in **RFC**(Request For Comments)

####比喻

* Packets -> 卡车
* Communication links -> 公路
* Packet switches-> 交叉路口
* End systems-> 起点和终点


###以服务来看
一种为应用程序提供服务的基础设施（Internet is an infrastructure that provides services to applications.）

####Distrubuted applications
Applications that involves multiple end systems that exchange data with each other.

注意: 应用程序跑在 **end systems**上, 不在 network core. e.g.一个网站跑在终端的一台电脑上，不在路由器/交换机上。

####API

* Application Programming Interface.
* Specifies how a program running on one end system asks the Internet infrastructure to deliver data to a specific destination program running on another end system.
* **Analogy**
    * set of rules
    * postal service API


###什么是协议（Protocol）

####举例：小学英语经典套话 (TODO)

>

####要求
两台设备要交流，必须使用一样的协议

####Definition of protocol
 A protocol defines the **format and the order** of messages exchanged between two or more communicating entities, as well as the **actions** taken on the transmission and/or recipt of a message or other event.

##The Network Edge

###Access Networks

####DSL
####Cable 电视网络
####FTTH 光纤入户
####Dial-up 拨号上网
####Satellite 卫星通讯

###Physical Media
####Twisted-Pair Copper Wire 双绞铜线
####Coaxial Cable
####Fiber Optics 光纤
####Terrestrial Radio Channels
####Satellite Radio Channel

##The Network Core
### Packet Switching
* End System exchange **messages** with each other
* Long messages are broken into **packets**
* Packets travell through communication links at a rate equal to the **full** transimission rate of the link.
	* Send **L bits** over a link with transimission rate **R bits/sec**
	* The time needed is **L/R sectonds**

####Store-and-Forward Transmission
* 路由器/交换机等收完整个数据包之后才肯开始转发（The packet switch must receive the **entire packet** before it can begin to transmit the first bit of the packet onto the outbound link.）
* 没有传完之前，数据放在buffer
* 延迟：等待完全传到路由器上需要L/R，发送到下一个设备又要L/R，一共2L/R
* 如果一个包需要经过N个link（有N-1个路由器），延迟共为NL/R
####Queuing Delays and Packet Loss
* 路由器里对每个link都有一个**output buffer/output queue**
* 如果一个包还没传完，另一个包又来了，则在output buffer排队 -- **queuing delay**
* 如果output buffer放不下，出现**packet loss（丢包）**
	* 丢掉buffer里的包或者新来的包
####Forwarding Tables and Routing Protocols
* 不同的计算机网络有不同的forwarding
* **Forwarding Tables**
	* Source includes the destination IP in the packet's header
	* routers extracts **portions** of the packet's destination IP
	* checks it against the **forwarding table**
	* forwards it to an **adjacent router** (through the router's outbound link)
* **Routing Protocols**
	* 用于 **自动调整forwarding tables**
	* 决定从路由器到目的地的 **最短路径**
* 课本自带[demo applet](http://media.pearsoncmg.com/aw/aw_kurose_network_2/applets/transmission/delay.html)
	* 如何运行过时的applet：确定applet安全（e.g.课本自带的applet）后[开启例外](http://www.java.com/en/download/help/jcp_security.xml)

[queuing demo](http://media.pearsoncmg.com/aw/aw_kurose_network_2/applets/queuing/queuing.html)
### Circuit Switching
* **比喻**
	* 饭店预约
	* 专属餐桌
* **特点**
	* Dedicated **end to end connection**
	* The connection is called **circuits**
	* *bona fide* connection: **switches** on th path maintain the connection
	* 建立连接的过程较为复杂
	* constant transmission rate: guaranteed
		* packet switching: no guarantee, may have delays
* **Use case**
	* 传统电话网络
* **计算**
	* 1个Link支持N个circuit，total transmission rate为R
		* 每个circuit的transmission rate 为R/N

####Multiplexing in Circuit Switched Networks
* **FDM**
	* Frequency Division Multiplexing
	* frequency spectrums are divided into **bands**, one for each circuit
	* **bandwidth** in hertz/cycles per second
* **TDM**
	* Time Division Multiplexing
	* Time is divided into **frames**, frames are divided into **slots**, one for each circuit
	* Transmission rate R = number of frames per second * bits per slot
* **Downside**
	* other circuits are idle during **silent periods**
	* circuit establishment is **complicated**
	* requires **complex signaling** software to coordinate the opeartion
* **Calculation**
	* for TDM link
	* circuit transmission rate R = total bit rate / number of slots
	* time to transmit a file of L bits: L/R

####Packet Switching v.s. Circuit Switching
* **Pros of Packet Switching**
	* suitable for data transmission
	* offers **better sharing** of transmission capacity
	* simpler, more efficient, less costly
* **Cons of Packet Switching**
	* Not suitable for real-time services
	* Headers increase the total amount of data to send
	* Need to reassemble at the destiniation
* **Why is packet switching more efficient**
	* **Probabilities** of idleness
	* Essentially the same performance as circuit switching
	* Allows more users, while in CS the number of users is more limited
	* A burst of data may use the **full link rate**, while in CS other circuits can't help
* **Crutial difference**
	* PS allocate link use **on demand**
	* CS **pre-allocate** link use **regardless of demand**
* **Trend**
	* Both popular, but PS are more so.
	* Telephone networks would use PS for the expensive portion

###A Network of Networks
* **access network**
	* 不一定是电信公司，可以是普通公司或者大学、机构
* **Basic Structure**
	* **end systems** are connected to (pays) **access ISP**
	* **access ISPs** are connected to (pays) **regional ISPs**
	* **regional ISPs** are connected to (pays) **tier-1 ISPs**
	* **tier-1 ISPs** are connected to each other **without payments**
* **multi-home**
	* connected to **one or more providers**
	* 如果其中一个provider挂了，服务还能用
* **PoP**
	* point of presence
	* group of routers in the **providers' network** (hence no PoP in access ISP)
	* 每层customer租赁第三方的高速连接自己的一个路由到provider的PoP里的某个路由
* **peer**
	* **nearby** ISPs **at the same level** are directly connected to each other to **bypass the upstream**
	* settlement-free(no payments)
* **IXP**
	* Internet Exchange Point
	* 第三方公司，提供ISP peer的交点
* **Content Provider Networks**
	* e.g. Google
	* 遍布世界的数据中心，通过私有TCP/IP网络互联
	* 向下与lower-tier ISP进行peer，互不付费
	* 向上与tier-1 ISP连接，付给他们钱，以连接到只能通过tier-1 ISP连接的地区
	* 好处
		* 降低花费
		* 有更多的控制

##Performance: Delay, Loss and Throughput in Packet-Switched Networks
* Total Nodal Delay = nodal processing delay + queuing delay + tranmission delay + propagation delay
* d<sub>nodal</sub> = d<sub>proc</sub> + d<sub>queue</sub> + d<sub>trans</sub> + d<sub>prop</sub>

###Overview of Delay in Packet-Switched Networks

####Types of Delay
* **Processing Delay**
	* Time to examine the packet's **header**, determine the next **direction**, check **errors** ...
	* Order of microseconds or less
* **Queuing Delay**
	* Time during which the packet **waits in the buffer**
	* **varies greatly**, depending on the intensity and nature of the traffic
	* order of microseconds ~ milliseconds
* **Transmission Delay**
	* If FCFS, length of the packet is L bits, transmission rate is R
	* transmission delay is L/R
	* The time switches need to **push the whole packet** into the link
* **Propagation Delay**
	* Time required to propagate a packet from on end to another in the link
	* **propagation speed** depends on the physical medium
		* ~ speed of light
	* **calclations**
		* Distance between the two ends **d**, propagation speed **s**, then propagation delay is **d/s**
		* order of milliseconds

####Transmission Delay v.s. Propagation Delay
* **Transmission delay**
	* `f(packet length, transmission rate of the link)`
* **Propagation delay**
	* `f(distance between the two routers)`
* **比喻**
	* 路由器 = 收费站
	* bit = 车
	* packet = 车队
	* transmission delay = 车队逐个收完费用的时间
	* propagation delay = 车队行驶到下一个收费站用的时间

### Queuing Delay and Packet Loss
####Queuing Delay
* varies from packet to packet
* typically use statisitacl measures: mean, variance, probability
* **Traffic intensity**
	* Condition
		* On average, **a** packets arrive at the queue per second
		* **R** is the transmission rate
		* each packet is **L** bits
	* Traffic intensity = La/R
		* number of bits **need to** pass through / number of bits **can** pass through
	* **Significance**
		* if La/R > 1
			* needs exceed capacity, the queue will tend to grow without bound
			* **Design your system so that the traffic intesnsity is no greater than 1**
		* if La/R <= 1
			* the queuing delay depends on the nature of the arriving traffic
				* periodical arrival: the queuing delay is almost always 0
				* burst of arrival: if N packets arrive simultaneously every NL/R seconds, nth packet has a queuing delay of (n-1)L/R seconds.
		* if it -> 0
			* packets arrive few and far, usually no queuing delay
		* if it -> 1
			* from time to time the arrival rate will exceed the transmission capacity, the queue will grow and shrink

####Packet Loss
* occurs when a packet arrives at a **full queue**, the router will drop it
* syndrome: transmitted by the source, but never reach the destination
* usually the lost packet will be **retransmitted**

###End-to-End Delay
* In a network without queuing delay and has N-1 routers:
	* d<sub>end-to-end</sub> = N(d<sub>proc</sub> + d<sub>trans</sub> +　d<sub>prop</sub>)
	* d<sub>trans</sub> = L/R (L is packet size)

####Traceroute
* 源发送N-1个特殊的包到目的地
* 当第n个路由器接到第n个包，会不转发这个包，而是传回一条信息给源（第m个包（m>n）会继续转发），目的host也一样
* 源收集这些信息来展示包的路径
* RFC1393规定Traceroute要重复发三遍这N-1个包，记录所有实验结果
* 由于queuing delay的差异，第n个包的延迟可能还大于第n+1个包

####End system, Application, and other Delays
* End system wanting to transmit a packet into a **shared medium** might **purposefully** delay its transmission **as part of the protocal**
* VoIP need to **fill a packet with encoded digitized speech** before sending it - **packetization delay**

###Throughput in Computer Networks
* 以实际接收量计算
* **instantaneous throughput**
	* the rate at which Host B is receiving the file at a instant of time
* **average throughput**
	* If F bits needs T seconds to be received by Host B, then the average throughput is F/T bits/sec
* **significance**
	* For many applications, the **delay doesn't matter**, what matters is the throughput
* **bottleneck**
	* R<sub>s</sub> = the rate between the server and the router
	* R<sub>c</sub> = the rate between client and the router
	* If no delay in the network core, throughput is **min{R<sub>s</sub>, R<sub>c</sub>}**, time to transfer a file of F bits is **F/min{R<sub>s</sub>, R<sub>c</sub>}**
	* If the nth link has transmission rate R<sub>n</sub>, then the throughput is **min{R<sub>1</sub>, ..., R<sub>n</sub>}**

##Protocol Layers and Their Service Models

###Layered Architecture
* **类比**
	* TODO：图1.22
* Each layer provides its service by
	* performing certain **actions** within the layer
	* using the services of the layer **directly below** it
* **advantages**
	* **modularity**
	* easier to **change the implementation** of each layer

####Protocol layering
* Network designers organize **protocols** and the network **hardware** and **software** that implement the protocols in **layers**
* **service model**
	* focus on the services that the layers offers to the layer above
* **implementation**
	* **application layer protocols**
		* usually implemented in **software** in the **end systems**
	* **transport layer protocols**
		* usually implemented in **software** in the **end systems**
	* **physical layer and data link layer**
		* usually implemented in a **network interface card**
		* because they are responsible for handling communication over a **specific link**
	* **network layer protocols**
		* usually implemented with **both hardware and software**
	* **distribution**
		* usually the function of protocols are **distributed** among components that make up the network
		* there is often **a peice of** a layer n protocol in each of the network components
* **Advantages**
	* RFC 3439
	* provide a **structured** way to discuss system components
	* **modularity** -- easier to update each component
* **Disadvantages**
	* **Duplicate** of lower layer functionality in layers
	* One layer might **need information only present in another layer** (but not directly below it)
* **Protocol stack**
	* Protocols of various layers
	* **Internet protocol stack**
		* physical, link, network, transport, application layers

####Application Layer
* **What it does**
	* runs network appplications and their application-layer protocols
* **What it moves**
	* **messages**
* **Where**
	* end systems
* **Protocol**
	* HTTTP
	* SMTP
	* FTP
	* DNS

####Transport Layer
* **What it does**
	* transports application-layer messages between application endpoints
* **What it moves**
	* **segment**
* **Where**
	* end systems
* **Protocol**
	* TCP
		* connection-oriented
		* guaranteed delivery
		* flow constrol(speed matching)
		* congestion control(adjust transmission rate)
	* UDP
		* connection-less
		* no reliability
		* no flow control
		* no congestion control
* **Relationship**
	* pass **transport-layer segment and a destination address** to the network layer

####Network Layer
* **What it does**
	* deliver segements passed by the transport layerin the source to the transport layer in the destination
	* routes a datagram through a series of routers between the source and destination
* **What it moves**
	* **datagrams**
* **Where**
	* end systems, routers
* **Protocol**
	* IP
		* defines the **fields** in the datagram and how the end systems and routers **act** on these fields
	* routing protocols
		* determine the **routes** that the datagram take
		* within a network, the network administrator can run **any routing protocol** desired
* **Alias**
	* IP layer
		* because IP is the glue that binds the Internet together
* **Relationships**
	* at each node, passes the datagram down to the link layer
	* at each node, receive the datagram delivered by the link layer

####Link Layer
* **What it does**
	* delivers the datagram between nodes along the route
* **What it moves**
	* **frames**
* **Where**
	* end systems, routers, links
* **Protocol**
	* Ehternet
	* WiFi
	* DOCSIS (cable)
* **Relationship**
* **Property**
	* Different protocols, different services
	* Reliability depends on the protocol

####Physical Layer
* **What it does**
	* move **individual bits** within the frame from one node to the next
* **What it moves**
	* **individual bits**
* **Where**
	* links
* **Protocol**
	* depends on the link and the **actual transmission medium**

####The OSI Model
* Open System Interconnection model
* **only one of** many different protocol suites
* educational purposes
* **components**
	* application layer, **presentation layer, session layer**, transport layer, network layer, datalink layer, physical layer
* **presentation layer**
	* help applications to interpret the meaning of data
	* **data compression, data encryption, data description(format)**
* **session layer**
	* **delimiting and synchronization** of data exchange
	* build a **checkpointing and recovery** scheme
* **in practice**
	* the presentation layer and session layer are usually built into the **application layer**
	* up to the application developer to decide whether they will be implemented

###Encapsulation

##Networks Under Attack

###The bad guys can put malware into your host via the Internet
###The bad guys can attack servers and network infrastructure
###The bad guys can sniff packets
###The bad guys can masquerade as someone you trust

##History of Computer Networking and the Internet
###The Development of Packet Switching: 1961 - 1972
###Proprietary Networks and Internetworking: 1972 - 1980
###A Proliferation of Networks: 1980 - 1990
###The Internet Explosion: The 1990s
###The New Millenium

##Summary