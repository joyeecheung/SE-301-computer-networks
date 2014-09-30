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

####举例：小学英语经典套话

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
**比喻**

* 饭店预约
* 专属餐桌

**特点**

* Dedicated **end to end connection**
* The connection is called **circuits**
* *bona fide* connection: **switches** on th path maintain the connection
* 建立连接的过程较为复杂
* constant transmission rate: guaranteed
	* packet switching: no guarantee, may have delays

**Use case**

* 传统电话网络

**计算**

* 1个Link支持N个circuit，total transmission rate为R
	* 每个circuit的transmission rate 为R/N
####Multiplexing in Circuit Switched Networks
**FDM**

* Frequency Division Multiplexing

**TDM**

* Time Division Multiplexing

####Packet Switching v.s. Circuit Switching

###A Network of Networks

##Performance: Delay, Loss and Throughput in Packet-Switched Networks
###Overview of Delay in Packet-Switched Networks
####Types of Delay
* Processing Delay
* Queuing Delay
* Transmission Delay
* Propagation Delay
####Transmission Delay v.s. Propagation Delay

### Queuing Delay and Packet Loss
####Queuing Delay
####Packet Loss

###End-to-End Delay
####Traceroute
####End system, Application, and other Delays

###Throughput in Computer Networks

##Protocol Layers and Their Service Models
###Layered Architecture
####Protocol layering
####Application Layer
####Transport Layer
####Network Layer
####Link Layer
####Physical Layer
####The OSI Model

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