---
title: "泛函分析小结（二）"
date: 2022-03-11
draft: true
toc: false
slug: functional-2
categories: ["分析与概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


<!-- 这一节应该包括巴拿赫空间中的有界线性算子的基本理论 -->


### Operator Topologies

在算子空间上可以定义不同强弱的拓扑

- 一致收敛：If $\left\|T_{n}-T\right\| \rightarrow 0$, that is, the operator norm of $T_{n}-T$ converges to 0 , we say that $T_{n} \rightarrow T$ in the **uniform operator topology**
- 强收敛：If $T_{n} x \rightarrow T x$ for all $x \in X$, then we say $T_{n} \rightarrow T$ in the **strong operator topology**
- 弱收敛：Suppose that for all $x \in X$ we have $T_{n} x \rightarrow T x$ in the weak topology of $X$. This means that $F\left(T_{n} x\right) \rightarrow F(T x)$ for all linear functionals $F$ on $X$. In this case we say that $T_{n} \rightarrow T$ in the **weak operator topology**



在 Banach 空间里，单位球都不一定是紧集，因此 Weierstrass 极值定理都不一定成立，也就是说，单位球上的连续函数都不一定存在最值。

但是，如果我们把拓扑放弱，选取更少的集合作为开集，这意味着一个集合更容易是紧的，当然，相反的，连续函数会变少。

令 $X$ 是一个线性空间，$\Phi$ 是它的对偶空间。定义一族开集：

$$
V(x, \varphi, r)=\{y \in X:|\varphi(y-x)|<r\}, \text { where } x \in X, \varphi \in \Phi, r>0
$$

记 $\sigma(X, \Phi)$ 是这族开集生成的拓扑。容易发现，它是使所有的线性泛函都连续的最弱的拓扑。



