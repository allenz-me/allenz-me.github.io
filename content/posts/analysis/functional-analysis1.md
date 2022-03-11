---
title: "泛函分析小结（一）"
date: 2022-02-26
draft: true
toc: false
slug: functional-1
categories: ["分析与概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

<!-- 这一节主要应该涵盖度量空间的基本内容 -->

> There are only two kinds of math books: those you cannot read beyond the ﬁrst sentence, and those you cannot read beyond the ﬁrst page.
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

<br>

### 赋范线性空间 (normed vector space)

$X$ 上的函数 $p(\cdot)$ 成为一个**范数(norm)**的条件是：

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

#### 赋范线性空间的例子

+ 在所有 $[a, b]$ 上的连续函数 $C[a, b]$ 可定义范数：
$$
\|f\|=\max _{x \in[a, b]}|f(x)|
$$

+ 有界数列 $l^\infty$ 可定义范数：
$$
\|x\|_{\infty}:=\sup _{i \geqslant 1}\left|x_{i}\right|
$$



<!-- ## 一般拓扑 -->