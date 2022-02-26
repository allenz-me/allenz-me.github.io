---
title: "泛函分析小结（一）"
date: 2022-02-26
draft: true
slug: functional-1
categories: ["分析与概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


## 点集拓扑

度量空间 (Metric Space)

一个集合 $X$，在其上定义一个函数 $d$，满足：
+ $d(p, q)>0$ if $p \neq q ; d(p, p)=0$;
+ $d(p, q)=d(q, p)$;
+ $d(p, q) \leq d(p, r)+d(r, q)$, for any $r \in X$.
这时候 $d$ 是一个距离函数，$(X, d)$ 构成一个度量空间。


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


紧集的闭子集是紧的。


