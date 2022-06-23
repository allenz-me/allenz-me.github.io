---
title: "4. Random matrices"
date: 2021-01-01
draft: false
slug: hdp4
categories: ["分析与概率", "高维概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

本书第四章的研究对象是随机矩阵。

## Preliminaries on matrices

这一部分回顾了算子范数和奇异值分解的内容。

### Singular value decomposition

对于 $m \times n$ 的矩阵 $A$，它的 singular value decomposition (SVD) 是：
$$
A=\sum_{i=1}^{r} s_{i} u_{i} v_{i}^{\top} = U\Sigma V^T, \quad \text {where} \;\; r=\operatorname{rank}(A)
$$
$u_i$ 是 $AA^T$ 的正交的特征向量，$v_i$ 是 $A^TA$ 的正交的特征向量；$s_{i}(A)=\sqrt{\lambda_{i}\left(A A^{\top}\right)}=\sqrt{\lambda_{i}\left(A^{\top} A\right)}$

把奇异值从大到小排序，$s_1(A)$ 是 $A$ 最大的奇异值，$s_r(A)$ 是 $A$ 最小的非零奇异值。

> $\text{rank}(A) = \text{rank}(AA^T) = \text{rank}(A^T A)$
>
> $AA^T$ 同 $A^T A$ 有相同的非零特征值

### spectral norm





###  

定义矩阵 $A, B \in \mathbb{R}^{m \times n}$ 的内积为
$$
\langle A,  B \rangle = \operatorname{tr}(A^TB) = \sum_{i=1}^m \sum_{j=1}^n A_{ij}B_{ij}
$$
由内积诱导的范数叫做 Frobenius 范数：
$$
\|A\|_{F}=\sqrt{\langle A, A \rangle }=\left(\sum_{i=1}^{m} \sum_{j=1}^{n}\left|A_{i j}\right|^{2}\right)^{1 / 2}
$$
用奇异值来表示的话：
$$
\|A\|_{F}=\left(\sum_{i=1}^{r} s_{i}(A)^{2}\right)^{1 / 2} .
$$


### Low-rank approximation



### Approximate isometries





## Nets, covering numbers and packing numbers

令 $(T, d)$ 是一个度量空间，$K \subset T, \epsilon > 0$

$K$ 的一个 $\epsilon$-net 指的是子集 $N \subseteq K$，使得以 $N$ 中的点为圆心，$\epsilon$ 为半径的若干个圆能覆盖 $K$，也就是说：
$$
\forall x \in K, \;\;\; \exists x_{0} \in \mathcal{N} \quad \text{s.t.} \;\; d\left(x, x_{0}\right) \leq \varepsilon
$$
$K$ 的一个 $\epsilon$-separated 指的是子集 $P \subseteq K$，使得以 $P$ 中的点为圆心，$\epsilon/2$ 为半径的若干个圆不相交，也就是说：
$$
\forall x, y \in P \subseteq K \;\;\; \text{s.t.} \;\; d(x, y) > \epsilon
$$

> 以上定义基于 $(T, d)$ 是一个赋范线性空间

一般地，选度量 $d$ 为欧式空间的二范数。

基数最小的 $\epsilon$-net 的基数记为 $N(K, \epsilon)$，基数最大的 $\epsilon$-separated 的基数记为 $P(K, \epsilon)$；分别称作 covering number 和 packing number。

**Equivalence of covering and packing numbers**

成立下述关系：
$$
P(K, 2\epsilon) \leq N(K, \epsilon) \leq P(K, \epsilon)
$$
**Covering numbers and volume**

记 $B_2^n$ 为 $n$ 为欧几里得球，则：
$$
\frac{|K|}{\left|\varepsilon B_{2}^{n}\right|} \leq {N}(K, \epsilon) \leq {P}(K, \epsilon) \leq \frac{\left|\left(K+(\varepsilon / 2) B_{2}^{n}\right)\right|}{\left|(\varepsilon / 2) B_{2}^{n}\right|}
$$
$| \cdot |$ 表示 volume。

**Covering numbers of the Euclidean ball**
$$
\left(\frac{1}{\epsilon}\right)^{n} \leq {N}\left(B_{2}^{n}, \epsilon\right) \leq\left(\frac{2}{\varepsilon}+1\right)^{n}
$$


### Hamming distance

令 $H = \{0, 1\}^n$ 表示所有0-1组成的序列，在其上定义度量：
$$
d_H(x, y) = \# \{i : x(i) \neq y(i)\}
$$
这构成了一个度量空间 $(H, d_H)$

**Covering and packing numbers of the Hamming cube**

令 $K = \{0, 1\}^n, m \in [0, n]$ 则：
$$
\left. {2^{n}} \middle /  {\displaystyle\sum_{k=0}^{m}\left(\begin{array}{c}
n \\
k
\end{array}\right)} \right. \leq \mathcal{N}\left(K, d_{H}, m\right) \leq \mathcal{P}\left(K, d_{H}, m\right) \leq \left. {2^{n}} \middle/ {\displaystyle\sum_{k=0}^{[m / 2\rfloor}\left(\begin{array}{l}
n \\
k
\end{array}\right)} \right.
$$




## Application: error correcting codes



### Metric entropy

记 $(T, d)$ 是一个度量空间，$K \subset T$，令 $C(K, \epsilon)$ 为编码 $K$ 达到精度 $\epsilon$ 所需要的最少的 bit 数，则：
$$
\log _{2} {N}(K, \epsilon) \leq {C}(K, \epsilon) \leq \log _{2} {N}(K,\epsilon / 2)
$$



**Error correcting code**

给定整数 $k, n, r$，两个映射：
$$
E: \{0, 1\}^k \to \{0, 1\}^n \quad \text{and} \quad D:\{0, 1\}^n \to  \{0, 1\}^k
$$
称为能改正 $r$ 个 bit 错误的 encoding 和 decoding maps，如果
$$
D(y) = x \;\; \text{ for } y \text{ differs from } E(x) \text{ in at most } r \text{ bits}
$$


> 例：如果 $x:= fill \; the \; glass$
>
> $r=2$，假设有 $y:=bill \; the \; class$ 是错误信息
>
> 一种简单的做法是使用冗余(redundancy)
>
> 如 $E(x):= fill \; the \; glass\;fill \; the \; glass\;fill \; the \; glass\;fill \; the \; glass\;fill \; the \; glass\;$
>
> 采用多数规则，如果原始信息 $x$ 重复 $2r+1$ 次，那么至多可以抗击 $r$ 个字符的错误
>
> 但是这样做的效率非常低，它用 $n=(2r+1)k$ 个字符去编码长度为 $k$ 的原始字符




$$
\log _{2} {P}\left(\{0,1\}^{n}, d_{H}, 2 r\right) \geq k
$$




定义 $R:=k/n, \delta := r/n$，则：
$$
1 - f(2 \delta) \leq R \leq 1 - f(\delta) , \quad f(t) = t \log_2(e/t)
$$



### Application: community detection in networks





### Application: covariance estimation and clustering

对于一个**零均值**的次高斯随机向量 $X$，我们想通过样本 $(X_1, X_2, \dots, X_m)$ 来估计协方差矩阵 $\Sigma = \mathbb{E} XX^T$，要达到一定的精确度，$m$ 至少应为多大呢？

样本协方差矩阵是：
$$
\Sigma_{m}=\frac{1}{m} \sum_{i=1}^{m} X_{i} X_{i}^{\top}
$$
因为知道均值，所以分母是 $m$ 而不是 $m-1$；$\Sigma_m$ 是一个 unbiased estimator，即 $\mathbb{E}\, \Sigma_m = \Sigma$ .



#### Covariance estimation

令 $X$ 是一个次高斯随机向量，记存在 $K > 0$ 使得

$$
\|\langle X, x\rangle\|_{\psi_{2}} \leq K\|\langle X, x\rangle\|_{L^{2}} \;\;\text { for any } x \in \mathbb{R}^{n}
$$

则对任意的正整数 $m$，成立：

$$
\mathbb{E}\left\|\Sigma_{m}-\Sigma\right\| \leq C K^{2}\left(\sqrt{\frac{n}{m}}+\frac{n}{m}\right)\|\Sigma\|
$$
这说明，要使平均相对误差小于 $\epsilon$
$$
\mathbb{E}\left\|\Sigma_{m}-\Sigma\right\| \leq \varepsilon\|\Sigma\|
$$
$m$ 的大小应该是
$$
m \asymp \varepsilon^{-2} n
$$


#### Application: clustering of point sets
