---
title: "Basic Polyhedron Theory (1)"
date: 2022-03-07
draft: false
toc: false
slug: polyhedron-theory
categories: ["运筹与优化"]
tags: ["Polyhedron"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

多面体与线性不等式 $Ax \leq b$ 有着紧密的联系，围绕这它们，主要有两个研究问题：

1. 系统 $Ax \leq b$ 是否有解
2. 系统 $Ax \leq b$ 的几何性质

### Fourier Elimination

Fourier 最先设计了一种类似高斯消元的方法来研究 $Ax\leq b$ 的有解性。

它的思想可以理解为：给出 $(\bar{x}_1, \bar{x}_2, \dots, \bar{x}_{n-1})$，我们是否能找到一个 $\bar{x}_n$ ，使得 $(\bar{x}_1, \dots, \bar{x}_n)$ 是 $Ax\leq b$ 的解 。

令 $I=\{1, \ldots, m\}$，引入记号：

$$
I^{+}:=\left\{i \in I: a_{i n}>0\right\}, \quad I^{-}:=\left\{i \in I: a_{i n}<0\right\}, \quad I^{0}:=\left\{i \in I: a_{i n}=0\right\}
$$

则：

$$
Ax \leq b \quad \Longleftrightarrow  \quad\begin{array}{llll}
\sum_{j=1}^{n-1} a_{i j}^{\prime} x_{j} & +x_{n} & \leq b_{i}^{\prime}, & i \in I^{+} \\
\sum_{j=1}^{n-1} a_{i j}^{\prime} x_{j} & -x_{n} & \leq b_{i}^{\prime}, & i \in I^{-} \\
\sum_{j=1}^{n-1} a_{i j} x_{j} & & \leq b_{i}, & i \in I^{0}
\end{array} \tag{1}
$$

其中 $a_{i j}^{\prime}=a_{i j} /\left|a_{i n}\right|, b_{i}^{\prime}=b_{i} /\left|a_{i n}\right|, i \in I^{+} \cup I^{-}$ .

$I^{+}, I^{-}$ 里的不等式分别相加，移去 $|I^{+}| + |I^{-}|$ 个并增加 $|I^+| \times |I^-|$ 个不等式，可以得到：

$$
\begin{array}{l}
\sum_{j=1}^{n-1}\left(a_{i j}^{\prime}+a_{k j}^{\prime}\right) x_{j} & \leq b_{i}^{\prime}+b_{k}^{\prime}, & i \in I^{+}, k \in I^{-} \\
\sum_{j=1}^{n-1} a_{i j} x_{j} & \leq b_{i}, & i \in I^{0}
\end{array} \tag{2}
$$

现在我们可以回答上面那个问题了，$(\bar{x}_1, \bar{x}_2, \dots, \bar{x}_{n-1})$ 满足(2) 当且仅当 存在 $\bar{x}_n$，使得 $(\bar{x}_1, \dots, \bar{x}_n)$ 是 $Ax\leq b$ 的解。

令 

$$
l= \begin{cases} \displaystyle\max _{k \in I^{-}}\left\{\sum_{j=1}^{n-1} a_{k j}^{\prime} \bar{x}_{j}-b_{k}^{\prime}\right\},  & I^- \neq \emptyset  \\
- \infty  , & I^- = \emptyset
\end{cases}\;\, \qquad 
u= \begin{cases} \displaystyle\min _{i \in I^{+}}\left\{b_{i}^{\prime}-\sum_{j=1}^{n-1} a_{i j}^{\prime} \bar{x}_{j}\right\}, & I^+ \neq \emptyset \\ 
+ \infty,   & I^+ = \emptyset
\end{cases}
$$

$l \leq \bar{x}_n \leq u$ 就是满足条件的数！

这意味着 $n$ 个线性不等式组 $A^n x \leq b^n$ 的有解性可以等价于一个 $n-1$ 个线性不等式组 $A^{n-1}x \leq b^{n-1}$ 的有解性。所以 Fourier elimination 的思路就是不断递推到 $A^1 x \leq b^1$ ，但是每一次迭代都有可能加入非常多的新的不等式，算法执行起来可能需要指数时间。

实际上，这种算法也可以看成是投影，多面体 $P$ 非空，当且仅当它在一个低一维的子空间上的投影非空。

<img src="../figures/polyhedron-theory/image-20220402141107763.png" alt="image-20220402141107763" style="zoom:55%;" />

### Polyhedron

线性规划的可行域 $P$ 是一个多面体，混合整数线性规划有时候可以转换成多面体上的线性优化。因此，多面体组合学是线性规划，包括整数线性规划在内的组合优化的一个重要理论。

**Polyhedron**
$$
P:=\left\{x \in \mathbb{R}^{n}: A x \leq b\right\}
$$

polyhedron 的复数形式是 polyhedra，bounded polyhedron 称为 polytope。

**Rational polyhedron**

如果 $A \in \mathbb{Q}^{m\times n}, b \in \mathbb{Q}^m$ 都是有理数。

**Polyhedral cone**

$$
C:=\left\{x \in \mathbb{R}^{n}: A x \leq 0\right\}
$$

既是多面体又是锥。


### Minkowski–Weyl Theorem

Minkowski–Weyl 定理给出了多面体的一个刻画。

一个集合 $C$ 是有限生成的 (finitely generated)，如果它是有限个点的凸锥包。

+ **A subset of $\mathbb{R}^n$ is a ﬁnitely generated cone if and only if it is a polyhedral cone**

这句话说明 polyhedral cone 有两种表示方法：

$$
C = \left\{x \mid A x \leq 0\right\} = \{By \mid y \geq 0\}
$$

+ **A subset $P$ of $\mathbb{R}^{n}$ is a polyhedron if and only if $P=Q+C$ for some polytope $Q \subset \mathbb{R}^{n}$ and finitely generated cone $C \subseteq \mathbb{R}^{n}$.**

这句话说明了一个 polyhedron 的表达方式：

$$
P=\operatorname{conv}\left(v^{1}, \ldots, v^{p}\right)+\operatorname{cone}\left(r^{1}, \ldots, r^{q}\right)
$$

> 参考：https://scaron.info/robotics/polyhedra-and-polytopes.html

图示如下：

<img src="../figures/polyhedron-theory/image-20220320151845791.png" alt="" style="zoom:67%;" />

一个多面体 = 极点的凸包 + 极线的锥包

### Lineality Space and Recession Cone

定义 polyhedron $P$ 的 recession cone 是：

$$
\operatorname{rec}(P):=\left\{r \in \mathbb{R}^{n}: x+\lambda r \in P \text { for all } x \in P \text { and } \lambda \in \mathbb{R}_{+}\right\}
$$

定义 polyhedron $P$ 的 lineality space 是：

$$
\operatorname{lin}(P):=\left\{r \in \mathbb{R}^{n}: x+\lambda r \in P \text { for all } x \in P \text { and } \lambda \in \mathbb{R}\right\} \text {. }
$$

注意到 $\operatorname{lin}(P)=\operatorname{rec}(P) \cap-\operatorname{rec}(P)$，当 $\operatorname{lin}(P)=\{0\}$ 时，称多面体 $P$ 是 pointed.

直观上看，a nonempty polyhedron is pointed when it does not contain any line.

如果 $P:=\left\{x \in \mathbb{R}^{n}: A x \leq b\right\}=\operatorname{conv}\left(v^{1}, \ldots, v^{p}\right)+ \operatorname{cone}\left(r^{1}, \ldots, r^{q}\right)$ 非空，那么

$$
\begin{aligned}
\operatorname{rec}(P)&=\left\{r \in \mathbb{R}^{n}: A r \leq 0\right\}=\operatorname{cone}\left(r^{1}, \ldots, r^{q}\right) \\
\operatorname{lin}(P)&=\left\{r \in \mathbb{R}^{n}: A r=0\right\} = \operatorname{ker}(A) \\
\end{aligned}
$$

### Implicit Equalities

多面体 $P=\left\{x \in \mathbb{R}^{n}: A x \leq b\right\}$ 是由一组不等式系统 $a_i^T x \leq b_i, \, i \in M$ 组成的，称不等式 $a_i^T x \leq b_i$ 是一个 implicit equality，如果 $P$ 被包含在超平面 $\{x \mid a_i^T x = b_i\}$ 中。

记  $M^{=}=\left\{i \in M \mid a^T_{i} x=b_{i},\, \forall x \in P\right\}$，$M^{<}=\left\{i \in M \mid a^T_{i} x<b_{i},\, \exists x \in P\right\}$，并引入记号 $(A^=, b^=), \, (A^<, b^<)$ 使得：

$$
P=\left\{x \in \mathbb{R}^{n}: A^{=} x \leq b^{=}, A^{<} x \leq b^{<}\right\}=\left\{x \in \mathbb{R}^{n}: A^{=} x=b^{=}, A^{<} x \leq b^{<}\right\}
$$

+ 称 $x$ 是 $P$ 的 *interior point*，如果 $a_i^T x < b_i \, \text{ for all }\, i \in M$

+ 称 $x$ 是 $P$ 的 *inner point*，如果 $a_i^T x < b_i \, \text{ for all }\, i \in M^{<}$

显然，一个多面体可能没有 interior point。但是，可以证明非空的多面体一定有 inner point。

根据 $M^{<}$ 的定义，$\forall i \in M^{<}$，都存在 $x_i \in P$ 使得 $a_i^T x_i < b_i$，由于多面体是凸集，不难发现 $\bar{x}:=\displaystyle\frac{1}{\left|M^{<}\right|} \sum_{i \in M^{<}} x_{i}$ 是一个满足条件的点。

由此不难证明：
$$
\operatorname{aff}(P)=\left\{x \in \mathbb{R}^{n}: A^{=} x=b^{=}\right\}=\left\{x \in \mathbb{R}^{n}: A^{=} x \leq b^{=}\right\}
$$
于是，我们有 $\operatorname{dim}(P)+\operatorname{rank}\left(A^{=}\right)=n$ .

称一个多面体 $P \subseteq \mathbb{R}^n$ full-dimensional，如果它有一个内点。这意味着 $\operatorname{dim} P=n$ ，也意味这 $P$ 没有 implicit equality。

例：
$$
P:= \left\{x \in \mathbb{R}^{n^2}: \quad \begin{aligned}
\sum_{j=1}^{n} x_{i j} &=1, \quad i=1, \ldots n \\
\sum_{i=1}^{n} x_{i j} &=1, \quad j=1, \ldots n \\
x_{i j} & \geq 0, \quad i, j=1, \ldots n
\end{aligned} \,\right\}
$$
的维数是 $n^2-2n+1$ .

### Faces

一个不等式 $c^T x \leq \delta$ 称作对 $P$ 有效 (valid)，如果 $c^T x \leq \delta, \, \forall x \in P$ .

有效性可以通过一组线性系统的有解性来判断：
$$
c^T x \leq \delta, \, \forall x \in P = \{x \mid Ax \leq b\} \Leftrightarrow \exists u \geq 0, \,\text{s.t.} \; u^TA=c^T, u^Tb \leq \delta
$$
上面的命题可以通过线性规划的对偶原理轻松证明。

多面体 $P$ 的一个 **face**，定义为：
$$
F:=P \cap\left\{x \in \mathbb{R}^{n}: c^Tx=\delta\right\}
$$
其中 $c^Tx \leq \delta$ 是一个 valid inequality for $P$ .

如果这样定义的 $F$ 非空，就称超平面 $\{x \mid c^T x = \delta\}$ 是 $P$ 的支撑超平面。

$\emptyset$ 和 $P$ 本身都是 $P$ 的 face，称 $P$ 的其它 face 都是 *proper* 的。

**直观上理解，face 就是多面体与它的一个支撑超平面的交。**


##### Characterization of the Faces

非空集合 $F$ 是 $P$ 的 face 当且仅当，对某个 $I \subseteq M$， $F$ 可以写成：

$$
F =\left\{x \in \mathbb{R}^{n}: a_{i}^T x=b_{i}, \,i \in I, a_{i}^T x \leq b_{i}, \,i \in M \backslash I\right\}
$$


多面体 $P$ 的 face 有以下性质：

+ face 的数量是有限的
+ $F$ 是 $P$ 的 face，那么 $\operatorname{lin}(F) = \operatorname{lin}(P)$
+ $P$ 的两个 face $F \neq F^\prime$ 当且仅当 $\operatorname{aff}(F) \neq \operatorname{aff}(F^\prime)$

### Facets

如果 $P$ 删去一个不等式仍然不变就说这个不等式是 ***redundant*** 的，一个多面体的各个约束可能都是多余的，比如一个不等式重复使用多次。

如果系统 $Ax \leq b$ 定义的多面体不包含任何多余的约束，那么就称这个系统是多面体的 *minimal representation* .

$P$ 的一个 face $F$ 称为 **facet**，如果 $F$  非空且 $\operatorname{dim} F = \operatorname{dim}P - 1$ .

比如说正方体的一条棱是 face，一个面就是 facet 。

### Minimal Faces

如果 $F$ 是 $P$ 的一个非空的 face，称 $F$ 是 $P$ 的一个 minimal face，如果 $F$ 不包含任何 $P$ 的 proper face。一个极小的 face 不一定是顶点。

**Hoﬀman and Kruskal**

如果 $F$ 是 $P$ 的非空的 face，那么 $\operatorname{dim}(\operatorname{lin}(P))  \leq \operatorname{dim}(F) \leq \operatorname{dim}(P)$ .

**Vectices**

多面体的0维的 face 称为 *vertex* 。

$P$ 存在顶点当且仅当 $\operatorname{lin}(P) = \{0\}$ ，即 $P$ is pointed.

$\bar{v}$ 是 $P$ 的顶点，当且仅当 $\bar{v}$ 是 $P$ 的极点 (extreme point)；当且仅当 $\bar{v}$ 满足 $Ax \leq b$ 中 $n$ 个线性无关的等式。

**Edges**

多面体的1维的 face 称为 *edge* 。

一个 edge 最多包含两个顶点，如果 $P$ 是 pointed 的，那么每个 edge 都至少会包含一个 vertex 。

**Extreme Rays**

一个 pointed polyhedral cone $C$ 的 *extreme ray* 指的是 $C$ 的 edge。

一个 pointed polyhedron $P$ 的 *extreme ray* 指的是它的 recession cone 的 extreme ray。

Extreme ray 的概念类似于 extreme point，它不能写成两条不同线的 conic combination。

<!-- ### Decomposition Theorem for Polyhedra -->

