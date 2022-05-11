---
title: "泛函分析小结（一）"
date: 2022-02-26
draft: false
toc: false
slug: functional-1
categories: ["分析与概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

<!-- 这一节主要应该涵盖度量空间的基本内容 -->

> There are only two kinds of math books: those you cannot read beyond the first sentence, and those you cannot read beyond the first page.
> 
> —— C. N. Yang

<br>

### 度量空间 (Metric Space)

一个集合 $X$，在其上定义一个函数 $d$，满足：
+ $d(p, q)>0$ if $p \neq q ; d(p, p)=0$;
+ $d(p, q)=d(q, p)$;
+ $d(p, q) \leq d(p, r)+d(r, q)$, for any $r \in X$.
这时候 $d$ 是一个距离函数，$(X, d)$ 构成一个度量空间。


由度量可以引出一大串的拓扑性质。

邻域 (Neighborhood)

A **neighborhood** of a point $p \in X$ is a set $N_{r}(p)$ consisting of all points $q$ such that $d(p, q)<r .$ The number $r$ is called the radius of $N_{r}(p)$.

内点 (Interior Point)

A point $p$ is an **interior point** of $E$ if there is a neighborhood $N$ of $p$ such that $N \subset E$.

开集 (Open Set)

$E$ is **open** if every point of $E$ is an interior point of $E$.

聚点 (Limit Point)

A point $p$ is a **limit point** of the set $E$ if every neighborhood of $p$ contains a point $q \neq p$ such that $q \in E$.

这意味着极限点总能找到一串点列去逼近它。

闭集 (Closed Set)

$E$ is **closed** if every limit point of $E$ is a point of $E$.

一个集合是闭集当且仅当它的补集是开的。

闭包 (Closure)

If $X$ is a metric space, if $E \subset X$, and if $E^{\prime}$ denotes the set of all limit points of $E$ in $X$, then the closure of $E$ is the set $\bar{E}=E \cup E^{\prime}$.

一个集合的闭包是包含这个集合最小的闭集。


<!-- 紧集的闭子集是紧的。 -->


### 度量空间的例子

+ 离散度量
$$
\rho(x, y)= \begin{cases}0, & x=y \\ 1, & x \neq y\end{cases}
$$

+ 在 $\mathrm{R}$ 上定义度量
$$
\rho_{1}(x, y)=\frac{|x-y|}{1+|x-y|}
$$

+ 定义 $C^\infty[a, b]$ 为区间 $[a, b]$ 上无穷次可微的函数，定义度量
$$
\rho(f, g)=\sum_{\nu=0}^{\infty} \frac{1}{2^{\nu}} \max _{t \in[a, b]} \frac{\left|f^{(\nu)}(t)-g^{(\nu)}(t)\right|}{1+\left|f^{(\nu)}(t)-g^{(\nu)}(t)\right|}
$$

### 赋范线性空间 (normed vector space)

$X$ 上的函数 $p(\cdot)$ 成为一个 **范数(norm)** 的条件是：

1. $p(x) \geqslant 0 , \;\forall x \in X$ (positive semidefiniteness)
2. $p(\alpha x) = |\alpha| p(x), \;\forall x \in X$ (positive homogeneity)
3. $p(x) + p(y) \leqslant p(x + y), \; \forall x, y \in X$ (the triangle inequality)
4. $p(x) = 0 \Rightarrow x = 0$ (positive definiteness)

满足前三个条件的称为**半范数(seminorm)**，半范数可以为非零的向量赋予零长度。

赋范线性空间记为 $(X, \| \cdot \|)$。

当度量满足条件：

$$
\rho(x, y)=\rho(x-y, 0), \rho(\alpha x, 0)=|\alpha| \rho(x, 0)
$$

可定义范数 $\| x\| = \rho(x, 0)$，度量空间可以成为一个赋范线性空间。

### 赋范线性空间的例子

+ 在所有 $[a, b]$ 上的连续函数 $C[a, b]$ 可定义范数：
$$
\|f\|=\max _{x \in[a, b]}|f(x)|
$$

+ 有界数列 $l^\infty$ 可定义范数：
$$
\|x\|_{\infty}:=\sup _{i \geqslant 1}\left|x_{i}\right|
$$


### $L^p$ 空间

$L^p$空间是连接实变函数与泛函分析的钥匙。

任意给定一个 measure space $(X, \mathcal{B}, \mu)$，那些 $p$ 次幂 Lebesgue 可积的函数组成的全体就构成了 $L^p$ 空间。

因为

$$
|f+g|^{p} \leqslant(|f|+|g|)^{p} \leqslant 2^{p}\left(|f|^{p}+|g|^{p}\right)
$$

$L^p$ 空间可以成为一个线性空间。如果函数是实值函数那么对应的数域就是 $\mathrm{R}$；如果是复值函数，那么数域就是$\mathrm{C}$。

进一步我们可以定义这些函数的范数：

$$
\lVert f\rVert_p=\int_X |f|^p \mathrm{d}\mu \quad (p\geq 1)
$$

> 在证明范数的过程中，要用到 Hölder 不等式 $\|f g\|_{1} \leqslant\|f\|_{p}\|g\|_{q}$ 和 Minkowski 不等式 $\|f+g\|_{p} \leqslant\|f\|_{p}+\|g\|_{p}$

但这个范数只是半范数，几乎处处为0值的函数构成了 $L^p$ 的一个子空间，由此我们可以得到一个商空间，半范数也就成了范数。 $f$ 与 $g$ 几乎处处相等是这里的等价关系。

对 $p = \infty$，此时定义函数的本性上确界 $\mathrm{ess\,sup} f{}$ 为除去一个零测集外的最大的上确界

$$
\|f\|_{L^{\infty}}=\inf \{M:|f(x)| \leqslant M, x \in X\, \text { a.e. }\}
$$

这个空间记作 $L^\infty$ 。

特别地，取 $X=N$ 表示全体自然数，$\mu$ 是 counting measure，这样就得到了 $p$ 次幂有界数列空间 $l^p$。

有了范数之后就能够讨论收敛性了

$L^p$ 下的依范数收敛：$\int_X|f_n(x)-f(x)|^p\mathrm{d}\mu\to 0, \,\; \text{as} \;\;n \to \infty$，在概率论里面叫做 converges in the r-th mean.

> 特别地，令 $1 \leq r \leq s$，$X_{n} \stackrel{L^{s}}{\longrightarrow} X \Rightarrow X_{n} \stackrel{L^{r}}{\longrightarrow} X$.

$L^\infty$ 下的依范数收敛：$\sup\limits _{X-E,\, \mu(E)=0}\left|f_{n}(x)-f(x)\right| \rightarrow 0$，其实就是除去一个零测集外的一致收敛。

这两种意义下的收敛都要强于依测度收敛（依概率收敛 converge in probability）。

对于 $1 \leq p \leq \infty$ 的情况，$L^p$ 空间是完备的。

对于 $0 < p < 1$ 的情况，Minkowski 不等式不再成立，因此不能藉此定义范数。

> $L^p$ 空间是可分的

### 一般拓扑

$X$ 上的一个拓扑指的是满足如下条件的集类 $\mathcal{T} \subseteq 2^X$:
+ $\emptyset, X \in \mathcal{T}$
+ $\mathcal{T}$ 中任意个集合的并在 $\mathcal{T}$ 中
+ $\mathcal{T}$ 中有限个集合的交在 $\mathcal{T}$ 中

$(X, \mathcal{T})$ 成为拓扑空间，$\mathcal{T}$ 中的集合称为开集，$X$ 中的元素称为点，任何开集的补集称为闭集。

如果对任何 $x, y \in X$，都能找到开集 $U, V$ 使得：

$$
x \in U, y \in V, \, U \cap V = \emptyset
$$

则称 $(X, \mathcal{T})$ 为 Hausdorff 空间。

最简单的拓扑是 $\{\emptyset, X\}$，称为 discrete topology / trivial topology。当 $X$ 包含至少两点时，它不是 Hausdorff 的。

显然在一个集合上不止一种定义拓扑的方法，拓扑也有粗细之分，如果两个拓扑 $\mathcal{T}, \mathcal{T}^\prime$ 满足 $\mathcal{T} \subseteq \mathcal{T}^\prime$，就说 $\mathcal{T}$ 比 $\mathcal{T}^\prime$ 粗(coarser)，$\mathcal{T}^\prime$ 比 $\mathcal{T}$ 细(finer)。

在拓扑的这套框架下，可以定义内点集和闭包。

$$
A^\circ = \bigcup_{U \text{ is open}, \, U \subset A} U, \quad \bar{A} = \bigcap_{U \text{ is closed}, \, U \supset A} U
$$

根据定义可以得到关系：

$$
A^\circ \subseteq A \subseteq \bar{A}
$$

定义 $A$ 的极限点 $x$，如果任意一个 $x$ 的邻域交 $A$ 都包含至少两个点。$A$ 的极限点组成了 $A$ 的导集 $A^\prime$，且存在关系 $\bar{A} = A \cup A^\prime$。

在拓扑空间中，点列的收敛是用开集定义的。$\{x_n, n \geq 1\} \to x$ 的定义是，对于任意 $x$ 的邻域 $U$，都存在正整数 $N$，使得 $x_n \in U,\,  \forall n \geq N$。在一般的拓扑空间中，点列的极限可能是不唯一的，但是 Hausdorff 空间中点列的极限是唯一的！

> $T_1$ 公理 ($T_1$ axiom)
> 
> 有限点集是闭集

**Continuity**

拓扑空间上的连续性由开集的原像是开集来表述，当然也可以用闭集的原像是闭集。 **一个函数的连续性，不仅取决于这个函数本身，还取决于这个函数定义域和值域空间的拓扑！** 如果 $f: X \to Y$ 是连续函数，$Y$ 中的拓扑是 $\mathcal{B}$，那么只需要 $f^{-1}(B), \, \forall B \in \mathcal{B}$ 是开集即可保证 $f$ 的连续性。另外，连续性的一个等价条件是 $f(\bar{A}) \subset \overline{f(A)}$。

连续还有局部的定义：对 $f(x)$ 的每个邻域 $V$，都存在包含 $x$ 的开集 $U$ 使得 $f(U) \subset V$。

**Homeomorphsim**

同胚指的是连续并且逆映射也连续的双射。同胚保持拓扑性质。

**Compactness**

任意开覆盖都存在有限子覆盖的集合是紧集。(Every open covering contains a finite subcollection.)

紧集有非常多好的性质

+ Hausdorff 空间中的紧集是闭的。
+ 连续映射将紧集映成紧集。
+ 任意个紧空间的直积是紧的。

每一个点列都有极限点的集合是列紧的。在可度量化的拓扑空间里，紧性和列紧是等价的。


**Local Compactness**

$X$ 是局部紧的，如果对于任意的 $x \in X$，都存在一个包含了 $x$ 的一个邻域的紧集。比如 $(\mathrm{R}, |\cdot|)$ 就是局部紧的。

one-point compactification.


### 由度量诱导的拓扑

度量可以自然的诱导出拓扑。


### 不动点定理

