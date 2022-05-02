---
title: "整数线性规划模型"
date: 2022-04-15
draft: false
toc: false
slug: integer-models
categories: ["运筹与优化", "整数和组合优化"]
tags: ["Polyhedron"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

### Knapsack Problem

背包问题，指的是要往一个容量有限的背包里装尽可能价值更高的物品。

物品重量 $a_i$，背包容量 $b$，问题的可行域是：
$$
S:=\left\{x \in \mathbb{Z}^{n}: \sum_{i=1}^{n} a_{i} x_{i} \leq b, x \geq 0\right\}
$$
如果 $x$ 的取值是 0 或 1，那这就是 0-1 背包问题，其可行域：
$$
K:=\left\{x \in\{0,1\}^{n}: \sum_{i=1}^{n} a_{i} x_{i} \leq b\right\}
$$
对于 0-1 背包问题，其 **minimal cover** 指的是一个指标集，背包不能装下所有的物品，但是任少一件都可以装下。根据 minimal cover 可以诱导出一个集合：
$$
K^{C}:=\left\{x \in\{0,1\}^{n}: \sum_{i \in C} x_{i} \leq|C|-1 \text { for every minimal cover } C \text { for } K\right\} .
$$
可以证明 $K=K^C$ ，也就是说0-1背包问题有两种表示方法。

**虽然这两种表示方法是等价的，但是它们的线性松弛 (linear relaxation) 是不一样的。** 这也说明我们根据其线性松弛得到的近似解的效果也是不一样的。

### Packing, Partitioning, Covering

令 $E=\{1, 2, \dots, n\}$ 是一个集合，$\mathcal{F}=\{F_1, F_2, \dots, F_m\}$ 是 $E$ 的一族子集。由此我们可以定义一个 incidence matrix $A$ :
$$
a_{ij} = \begin{cases}
1 & \text{if } j \in F_i \\
0 & \text{otherwise}
\end{cases}
$$
例：$E=\{1, 2, 3\}, F = \left\{\{1, 2\}, \{1, 3\}, \{2, 3\}\right\}, A = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$ .

我们说 $E$ 的一个 packing, partitioning, covering 指的分别是如下集合：

$$
\begin{aligned}
S^P(A) &= \{x \in \{0, 1\}^n : Ax \leq \mathbf{1}\} \\
S^T(A) &= \{x \in \{0, 1\}^n : Ax = \mathbf{1}\} \\
S^C(A) &= \{x \in \{0, 1\}^n : Ax \geq \mathbf{1}\} \\
\end{aligned}
$$

由此我们可以得到 set packing / partitioning / covering 问题

$$
\begin{aligned}
\text{set packing:} & \qquad \max \left \{\sum_{i=1}^{n}{w_i} x_i: x \in S^P \right\} \\
\text{set partitioning:} & \qquad \min \left \{\sum_{i=1}^{n}{w_i} x_i: x \in S^T \right\} \\
\text{set covering:} & \qquad \min \left \{\sum_{i=1}^{n}{w_i} x_i: x \in S^C \right\} \\
\end{aligned}
$$

许多实际问题都可以建模成 set packing / covering 问题。

#### Independent set -> set packing

一个无向图 $G(V, E)$ 的独立集 (independent set, stable set, coclique) 是 $V$ 的一个不相邻子集，即 $V$ 的独立集的顶点互不相邻。

如果我们把 $E=\{(i, j) \cdots\}$ 看成是 $G$ 的一个子集族，那么每一个独立集都是一个 set packing。





### Traveling Salesman Problem





