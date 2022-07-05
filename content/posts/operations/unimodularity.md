---
title: "Total Unimodularity"
date: 2022-04-20
draft: false
slug: total-unimodular
toc: false
categories: ["运筹与优化", "整数和组合优化"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

### Total Unimodularity

矩阵 $A$ 是全单位模 (**totally unimodular**) 矩阵，如果它的每一个方的子矩阵的行列式取值于 $\\{0, \\pm1\\}$. 这意味着 $A$ 的所有元素都是 $0$ 或者 $\\pm1$ .

单位模矩阵在整数规划起着非常重要的作用。

如果 $A$ 是 TUM (totally unimodular matrix)，对于 $b\\in \\mathbb{Z}^m$，多面体 $P=\\{x\\in \\mathbb{R}^n: Ax\\leq b\\}$ 的顶点都是整点！

多面体的每个顶点都是解 $n$ 个线性无关的方程组得来的，因此根据 Cramer 法则，容易得到上述结论。事实上这个结论反过来也是成立的，对于任意的 $b\\in \\mathbb{Z}^m$，多面体 $P=\\{x\\in \\mathbb{R}^n: Ax\\leq b\\}$ 的顶点都是整点，那么 $A$ 是 TUM。

以下结论是等价的：

+ $A$ 是 TUM
+ $A^T$ 是 TUM
+ $\-A$ 是 TUM
+ $\\begin{bmatrix} A & I \\end{bmatrix}$ 是 TUM
+ $\\begin{bmatrix} I & A & \-A \\end{bmatrix}$ 是 TUM

于是，如果 $A$ 是 TUM，只要其它向量都是整的，则下面的多面体都是整的：


+ $\\{x : Ax \\leq b\\}$
+ $\\{x : Ax = b\\}$
+ $\\{x : Ax \\leq b, x\\geq 0\\}$
+ $\\{x : Ax = b, x\\geq 0\\}$
+ $\\{ x : c \\leq Ax \\leq d, l \\leq x \\leq u \\}$

保持 TU 的运算：

+ 用 -1 乘它的一行或一列
+ 交换它的两行或两列
+ 将一行（列）从另外一行（列）中减去

保持 TU 的关键是不改变行列式的值。

**(Hoffman, Kruskal)**
$$
A \\text{ is total unimodular} \\Longleftrightarrow \\{x: Ax \\leq b, x\\geq 0, A \\text{ integral}\\} \\text{ is integral for every } b \\in \\mathbb{Z}^m
$$


【Seymour's Decomposition Theorem】

借助 total unimodularity，我们可以确定哪些整数规划问题可以直接等价于其线性松弛。



### TUM and Graphs

**(Ghouila-Houri,1962)**

$A\\in \\mathbb{R}^{m \\times n}$ 是 TUM 的充分必要条件是：对每一个 $R\\subseteq \\{1, \\dots, m\\}$，都有一个划分 $R=R\_1 \\cup R\_2, R\_1 \\cap R\_2 = \\emptyset$，使得对每一个 $j=1, \\dots, n$，都有：
$$
\\sum\_{i\\in R\_1} a\_{ij} \- \\sum\_{i \\in R\_2} a\_{ij} \\in \\{0, \\pm 1\\}
$$
这种性质也叫做 equitable row-bicoloring。

**无向图 $G(V, E)$ 的 incidence edge matrix 是 TUM，当且仅当 $G$ 是二分图，** 是上述定理的直接推论。

**有向图的 incidence arc matrix 是 TUM。**

#### Max Matching and Min Vertex Cover

图的最大基数匹配 (max matching) 问题是：
$$
\\begin{aligned}
\\max \\; & \\mathbf{1}^T x \\\\
\\text{s.t. } & A\_G x \\leq \\mathbf{1} \\\\
& x \\in \\{0, 1\\}^E
\\end{aligned}
$$
图的 vertex cover 指的的 $V$ 的一个子集，使得每一条边都至少包含这个子集的一个点。图的最小顶点覆盖 (min vertex cover) 问题是：
$$
\\begin{aligned}
\\min \\; & \\mathbf{1}^T y \\\\
\\text{s.t. } & y\_i \+ y\_j \\geq 1 \\quad \\forall (i, j) \\in E \\\\
& y \\in \\{0, 1\\}^V
\\end{aligned}
$$

**(König Theorem)**  二分图的最大基数匹配等于其最小顶点覆盖。



### Total Dual Integrality

有理系统 $Ax \\leq b$ 称作全对偶整的 (**TDI**, total dual integral)，如果对任意的整向量 $c$，只要 $\\max\\{c^T x: A x \\leq b\\}$ 有解，其对偶问题 $\\min \\{b^T y : A^Ty = c, y \\geq 0\\}$ 都存在整数最优解。（不一定所有的最优解都要是整数的）

TDI 是比 TU 更强的条件：$(A, b) \\text{ TDI }, b \\in \\mathbb{Z}^m \\Longrightarrow \\{x: Ax \\leq b\\} \\text{ is integral}$.

反过来是可能不成立的，存在整的多面体不是TDI的**。但是，任何整的多面体都可以被一个 TDI 系统表示。**

> However, any integral polyhedron can always be represented by a TDI system whose coeﬃcients are all integer.
>
> TDI is a representation, not a polytope.

比如 $P = \\{(x\_1, x\_2) : x\_1 \+ 2x\_2 \\leq 6, 2x\_2 \+ x\_1 \\leq 6, \\; x\_1, x\_2 \\geq 0\\}$ ，问题 $\\displaystyle\\max\_{(x\_1, x\_2) \\in P}\\, \\{x\_1 \+ x\_2\\}$ 的对偶问题无整数解。

但是，取 $P$ 的另一种表示：$P = \\{(x\_1, x\_2) : x\_1 \+ 2x\_2 \\leq 6, 2x\_2 \+ x\_1 \\leq 6, x\_1\+ x\_2 \\leq 4,  \\; x\_1, x\_2 \\geq 0\\}$，这时候问题 $\\displaystyle\\max\_{(x\_1, x\_2) \\in P}\\, \\{x\_1 \+ x\_2\\}$ 的对偶问题存在整数解。



【connection with Hilbert Basis】
