---
title: "网络流的原始对偶算法"
date: 2022-04-03
draft: false
slug: primal-dual-1
toc: false
categories: ["运筹与优化", "整数和组合优化"]
tags: ["网络流"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

# Primal-dual Method to Network Flow

原始对偶算法是解决组合优化问题的通法。最短路和最大流是网络流中最经典的两个问题，它们都可以在原始对偶算法的框架下进行解决。

网络流问题大都可以写成线性规划，不同的网络流问题有着不同的LP形式，但解决的思路是通用的。

对于有向图 $(V, E)$，它的 **node-arc incidence matrix** 是一个 $|V| \times |E|$ 的矩阵：
$$
A_{v, \,e} = \begin{cases} 
+1, &\text{if arc } e \text{ starts at node } v \\
-1, &\text{if arc } e \text{ ends at node } v \\
0, &\text{otherwise}
\end{cases}
$$
矩阵的每一行对应于一个 vertex，每一列对应于一个 arc (edge)。

<img src="../figures/primal-dual-1/image-20220403151941394.png" alt="image-20220403151941394" style="zoom:67%;" />

上图的点—弧关联矩阵是：
$$
\begin{aligned}
 & \quad\;\, e_1  \quad\; e_2 \quad\;\, e_3 \quad\;\, e_4 \quad\;\, e_5 \quad\; e_6 \quad\;\, e_7 \quad\; e_8  \quad\; e_9 \\
A=&\left(\begin{array}{rrrrrrrrr}
1 & 1 & 1 & 0 & 0 & 0 & 0 & -1 & 0 \\
-1 & 0 & 0 & 1 & -1 & 0 & 0 & 0 & 0 \\
0 & -1 & 0 & -1 & 1 & 1 & 1 & 0 & 0 \\
0 & 0 & -1 & 0 & 0 & -1 & 0 & 1 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & -1 & 0 & -1
\end{array}\right)\; \begin{array}{r}
v_1 \\
v_2 \\
v_3 \\
v_4 \\
v_5
\end{array}
\end{aligned}
$$
在点 $i \in V$ 处的流量守恒 (flow conservation) 是：
$$
a_i^T f = 0
$$
其中 $f \in \mathrm{R}^{|E|}$，表示每条边的流量。

如果 $a_i^T f > 0$，表示 $i$ 处有流量流出；如果 $a_i^T f < 0$，表示 $i$ 处有流量流入。

**注意上面的点—弧关联矩阵是一个缺秩的矩阵，它有一个多余的约束。** 这点也好理解，当你知道 $|V|-1$ 个点的流量的时候，你自然就知道剩下一个点的流量了。

### Shortest Path

容易写出，$s\to t$ 的最短路问题的流量守恒是：
$$
Af =\left[\begin{array}{c}
1\\
-1 \\
0 \\
\vdots \\
0 \\
\end{array} \right]\;
\begin{array}{l}
s: \text{a unit flow leaving} \\
t: \text{a unit flow entering}\\
\text{flow conservation}  \\
\vdots\\
\text{flow conservation} \\
\end{array}
$$
从 $s$ 到 $t$ 的一条路可以设想为：一个单位流，从 $s$ 流向 $t$，这样的流必然满足：

+ 起点 $s$ 流出一个单位的流
+ 终点 $t$ 流入一个单位的流
+ 其余点流量守恒

由于 $A$ 是缺秩的，去掉任意一行约束都可以，但是我们一般删去关于 $t$ 的那一行，记矩阵 $\bar{A}$。最后得到最短路线性规划模型为：
$$
\begin{aligned}
\min_f \; \; & c^T f \\
\text{s.t. } & \bar{A} f = \begin{bmatrix}
1 \\
0 \\
\vdots \\
0 \\
\end{bmatrix}, \quad f \geq 0
\end{aligned} \tag{SP}
$$
其中 $c$ 是每条边的权重（费用），决策目标是最小化 $s$ 到 $t$ 的单位流的费用。

**最短路问题的原问题，决策变量是每一条边，约束条件是每个点的流量守恒。**

### Max Flow

假设从 $s$ 到 $t$ 有一条容量为 $\mathrm{v}$ 的流，记 $d = \begin{bmatrix}-1 & +1 & 0 & \cdots & 0 \end{bmatrix}^T$，最大流的流量守恒表示为：
$$
Af + d\mathrm{v} = 0
$$
不难发现 $Af + d \mathrm{v} = 0 \Leftrightarrow Af + d\mathrm{v}  \leq 0$ .

因此最大流的数学规划模型为：

$$
\begin{aligned}
\max_{f, \,\mathrm{v}} \;\; & \mathrm{v} \\
\text{s.t. } \; &  Af + d \mathrm{v} \leq 0 \\
 & 0 \leq f \leq b
\end{aligned} \tag{MF}
$$
其中 $b$ 是每条边的容量上限。

### Primal Dual — Shortest Path

最短路的对偶问题是：
$$
\begin{aligned}
\max_y \; & y_s - y_t \\
\text{s.t. } & y_i - y_j \leq c_{ij} \, , \;\; \forall (i, j) \in E \\
 & y \text{ free}
\end{aligned}
$$
注意到对偶问题的决策变量是每个顶点，约束条件是每条边。

因为原问题多了一个约束条件，所以对偶问题多了一个决策变量，通常我们令 $y_t = 0$ .
$$
\begin{aligned}
\max \; & y_s \\
\text{s.t. } & y_i - y_j \leq c_{ij} \, , \;\; \forall\, (i, j) \in E \\
 & y \text{ free}, \;\; y_t= 0
\end{aligned} \tag{SP-D}
$$
下面介绍用原始对偶算法解决最短路问题的思路：

从一个可行解 $y=0$ 出发，记 $J$ 是有效约束指标集，我们可以直接写出 DRP：
$$
\begin{aligned}
\max \; & y_s \\
\text{s.t. } & y_i - y_j \leq 0 \, , \;\; \forall\, (i, j) \in J \\
& y_i \leq 1, \;\; y_t=0
\end{aligned}
\tag{SP-DRP}
$$
事实上，上面这个问题是非常好求解的！因为 $y_s$ 要么为 1 要么为 0 。

+ 如果 $J$ 中存在 $s \to t$ 的路径，那么可以让 $y_s = 0$ ，说明已经达到最优
+ 如果 $J$ 中不存在 $s \to t$ 的路径，那么 $y_s$ 最大可以取到 1，继续迭代

SP-DRP 的最优解是：
$$
\bar{y}_i = \begin{cases}
1, & i\, \text{ reachable from } s \text{ using arcs in } J \\
0, & i\, \text{ from which } t \text{ is reachable using arcs in } J \\
1, & \text{all other nodes}
\end{cases}
$$
记：
$$
\theta=\min _{\substack{(i, j) \notin J \\ y_{i}-y_{j}>0}}\left\{c_{i j}-\left(y_{i}-y_{j}\right)\right\}
$$
则 $y_{\text{new}} = y + \theta \bar{y}$，使 $\theta$ 最小的 $(i, j)$ 将进入到 $J_{\text{new}}$ 中。**这一过程的思想就是，不断向 $J$ 中添加边，直到 $J$ 包含一条从 $s$ 到 $t$ 的路径。**













