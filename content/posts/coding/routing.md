---
title: "路由那些事"
date: 2020-04-11
draft: false
slug: routing
categories: ["算法与程序设计"]
tags: ["计算机网络"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


路由器根据路由表（Routing Table）转发数据包。路由控制分为静态路由和动态路由。静态路由是管理员事先设定好路由信息的方式。动态路由需要路由器进行通信，再根据路由协议得到路由表。

路由协议分为两大类
+ **外部网关协议**（Exterior Gateway Protocol）
+ **内部网关协议**（Interior Gateway Protocol）

EGP和IGP的关系类似于IP地址网络部分和主机部分的关系。根据EGP在区域网络之间进行路由选择，根据IGP在网络内部进行路由选择。

最具代表性的路由算法有两种
+ **距离向量**（Distance-Vector）
路由器之间互换各自网络的方向及位置的信息，并以这些信息为基础制作路由表。这种方法处理简单，但容易发生路由循环。
+ **链路状态**（Link-State）
通过信息同步，路由器了解网络的整体连接状态/网络拓扑，并根据该图确定通往目标网络的路径。能够保证路由信息的准确性和最优性，但是处理复杂巨大的网络时要付出计算代价。

常见的内部网关协议有 RIP和 OSPF，外部网关协议有 BGP。

## RIP（Routing Information Protocol）

RIP广泛应用与LAN。路由器将信息每隔30s向周围的路由器进行广播，广播的内容是自己与某个网络的最短距离。（如果等到6次都没有收到某个路由器的信息，那么就断开与它的连接。）

**RIP基于距离向量决定路径**。距离的单位为“跳数”，即经过路由器的个数。如果一个网络有两条路径，那么就选择距离较短的。

RIP协议存在一些问题，比如循环广播导致无限计数，难以处理环路中突发故障的情况。为此，RIP采用如下几种方法：
+ 最长距离不超过16
+ 水平分割（split horizon）：路由器不再把受到的路由消息返还给发送端。
+ 毒性逆转（poisoned reverse）：当网络中发生链路断开的情况，不是不再发送这个消息，二是将这个无法通信的消息传播出去。即，发生一个距离为16的消息。
+ 触发更新（triggered update）：当路由信息发生变化时，不等待30秒而是立即发送出去。

使用RIP协议，在一个具有众多环路的复杂的网络中，想要达到一个稳定的状态也是需要花一段时间的，并且，哪怕网络处在稳定的状态，还是要定期交换路由信息，一定程度上是对网络资源的浪费。

## OSPF（Open Shortest Path First）

**OSPF是链路状态型路由协议**。路由器之间交换链路状态生成网络拓扑信息，然后再根据拓扑信息生成路由控制表。支持子网掩码。

RIP的路由选择，要求途中经过的路由器个数越少越好。与之相比，OSPF可以给每一条链路赋予一个权重（每条链路可以具有不同的带宽），并始终选择一个权重最小的路径。

RIP的包，只有一种类型，一边确认是否连接了网络，一边传送网络信息。而在OSPF中，根据作用的不同可以分为5种：

|| 类型 | 功能|
| :---: | :--- | :--- |
| 1| 问候（HELLO）| 确认向量路由器
| 2| 数据库描述（Database Description）|链路状态数据库的摘要信息|
| 3|链路状态请求（Link State Request） | 请求从数据库中获取链路状态信息|
|4| 链路状态更新（Link State Update）| 更新链路状态数据库中的链路状态信息|
| 5|链路状态确认应答（Link State Acknowlegment） |链路状态信息更新的确认应答 |

通过上述不同类型的包，OSPF不仅可以大大减少网络流量，还可以达到迅速更新路由信息的目的。

当网络规模越来越大时，OSPF为了减少计算负荷，引入了区域的概念。区域将若干个网络和主机划分为一个小组，成为一个“自治系统”（AS）。每个区域设置若干个边界路由器与外界相连。

## BGP（Border Gateway Protocol）

BGP 是连接不同组织机构的一种协议，因此属于外部网关协议，主要用于连接不同ISP。

ISP、区域网络等会将每个网络编配成一个个自治系统（AS）进行管理。每个自治系统拥有一个16比特的 AS 编号。有了 AS 编号的域，相当于一个“国家”。两个自治系统要想直接通信必须架设专线，不然就要通过其他 AS 进行中转。

**BGP是路径向量协议**。根据BGP交换路由信息的路由器叫做BGP扬声器。RIP和OSPF基于最短路径进行数据包转发，而BGP基于 AS 之间的合约进行数据包转发，一般选择 AS 数最少的路径，不过仍然要遵守各个 AS 之间的约定进行路由选择。

## MPLS（Multi Protocol Label Switching）

MPLS是一种新技术，叫做标记交换，它对每个 IP 包做上标记，然后根据这个标记进行转发。

标记的转发无法在传统的路由器上进行，在MPLS网络中实现标记交换功能的路由器叫做标记交换路由器（LSR， Label Switching Router），与外部网络连接的那部分 LSR 叫做标记边缘路由器（LER，Label Edge Router）。

MPLS 会给每个数据包的 IP 首部追加32比特的标记，这个标记能决定数据转发的路径。

MPLS 有着极高的转发速度，处理比传统的路由协议更加简单，可以通过高速的硬件实现转发。