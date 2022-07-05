---
title: "Large-Scale Linear Optimization"
date: 2022-01-26
draft: false
slug: "large-scale-linear-opt"
tags: ["线性规划", "随机规划"]
categories: ["运筹与优化"]
---


本文介绍大规模线性规划问题的求解思想。内容主要来源自 《Introduction to Linear Optimization》Chapter 6.

## Delayed column generation

考虑一个非退化的线性规划的标准问题：

$$
\\begin{array}{cl}
 \\min  & c^T x \\\\
 \\text{s.t.} & Ax = b, x \\geq 0
\\end{array}\\tag{1}
$$

假如说矩阵 $A\\in \\mathrm{R}^{m \\times n}$ 的列数非常大，即 $n \\gg m$，这时候我们无法把所有的列都放入内存执行计算。但是，注意到问题只有 $m$ 个基变量，也就是说我们只需要找到 $n$ 列中特定的 $m$ 列，就可以完成单纯型法的迭代，找到最优解了！

我们可以先随便选取一组基变量进行计算， 接着我们就要去找 entering variable，找进基变量的准则是 reduced cost $\\bar{c}\_j = c\_j \- c\_B^T B^{\-1} A\_j < 0$。当然，一般会选择 $\\bar{c}\_j$ 最小的指标 $j$ 进基，这就归结于问题：

$$
\\min \\;\\bar{c}\_j = c\_j \- c\_B^T B^{\-1} A\_j
$$

对于一些具有特殊结构的线性规划，只要如上的问题可以轻松解决，即找到进基指标 $j$ 和相应的列 $A\_j$，那么原问题就可以得到高效地求解！

> 注：矩阵 $B$ 可以借助 revised simplex 方法进行迭代，因此计算量也是小的。

下料问题是一个经典的、可以使用列生成算法来求解的问题。

## Cutting-stock problem

下料问题由Kantorovich在1939年提出，是一个 NP-Hard 问题。

假设一个造纸厂生产长度为 $W$ 的纸，然而，$m$ 个顾客需要的是 $b\_i$ 卷长度为 $w\_i < W$ 的纸（$i=1, \\dots, m$）。那么，造纸厂最少需要多少卷纸来满足顾客的需求呢？

为了解决这个问题，用一个列向量 $A\_j = [a\_{ij}]\_{m \\times 1}$ 表示一卷长度为 $W$ 的纸是如何切割成若干个长度为 $w\_i$ 的纸的，其中 $a\_{ij}$ 表示第 $j$ 种切法中切出长度为 $w\_i$ 的纸的数量。这样的话，对于一个向量 $[a\_{1j}, a\_{2j}, \\dots, a\_{mj}]^T$ ，它成为一种可行的切法的充要条件是满足：

$$
A\_j^T  {w} =\\sum\_{i=1}^m a\_{ij} w\_i \\leq W, \\quad a\_{ij} \\in \\mathrm{N}
$$

令矩阵 $A=[A\_j]\_{1\\times n} \\in \\mathrm{R}^{m\\times n}$ 表示所有可行的切割方法，注意到 $n$ 可能非常大，这会给问题带来困难。

下料问题归结为一下优化问题：

$$
\\begin{aligned}
\\min \\;& \\sum\_{j=1}^n x\_j \\\\
\\text{s.t.} \\;& \\sum\_{j=1}^n a\_{ij}x\_j \\geq b\_i, \\;\\; i =1, 2, \\dots, m \\\\
 & \\: x\_j \\geq 0, \\;\\; x\_j \\in \\mathbb{N},  \\;\\; j = 1, 2, \\dots, n
\\end{aligned}
$$

决策变量 $x\_j$ 表示第 $j$ 种切割方法执行的数量。这是一个整数规划问题，把整数条件放松掉，我们求解一个线性规划问题能轻松得到原整数规划问题的一个上界。（向上取整即可），于是其线性松弛可以表示为：

$$
\\begin{aligned}
\\min \\;& \\sum\_{j=1}^n x\_j \\\\
\\text{s.t.} \\;& \\sum\_{j=1}^n a\_{ij}x\_j = b\_i, \\;\\; i =1, 2, \\dots, m \\\\
 & \\: x\_j \\geq 0,  \\;\\; j = 1, 2, \\dots, n
\\end{aligned}
$$

注意到 $n \\gg m$，可行的切割方案数是非常大的，所以，这里可以使用 delayed column generation 的思想。不妨初始化设置 $B = I\_{m\\times m}$，接下来解优化问题：

$$
\\begin{aligned}
\\min \\;& 1 \- c\_B^T B^{\-1} A\_j \\\\
\\text{s.t.} \\;& [w\_1, \\dots, w\_m] A\_j \\leq W, \\quad a\_{ij} \\in \\mathbb{N} \\\\
\\end{aligned}
$$

找到合适的进基变量和对应的列 $A\_j$. 这里的目标函数是变量 $x\_j$ 在单纯型表中的系数。

> 注意到这里是一个整数规划问题，但是可以用动态规划算法以伪多项式的时间内求解。

接下来用 revised simplex 更新矩阵 $B$. 迭代到上述问题的最优值大于等于0的时候，原问题达到最优，单纯型迭代停止。这样我们就解决了一个整数规划的线性松弛问题。

最后，对线性松弛最优解向上取证，可得： IP-optimal cost $\\leq$ LP-optimal cost + $m$. 在 $m$ 较小的时候，这是一个良好的近似解。



## Cutting-plane method

列生成算法针对的是线性规划中列数特别多的情况，而切平面方法针对的是约束条件特别多的情况。这两种方法的联系可以理解为，列生成针对的是原问题，而切平面解决的是对偶问题：

$$
\\begin{array}{cl}
 \\max  & p^T b \\\\
 \\text{s.t.} & p^T A \\leq c^T
\\end{array} \\tag{2}
$$

注意到，如果 $A\_{m\\times n}$ 的列数 $n$ 非常大时，上述问题的约束条件非常之多，使得单纯型法的基变量个数也非常多。

类似地，我们没有必要同时考虑所有的约束条件，如果我们考虑一个子集上的：

$$
\\begin{array}{cl}
 \\max  & p^T b \\\\
 \\text{s.t.} & p^T A\_i \\leq c\_i , \\;\\; i \\in I
\\end{array}
$$

计算出的最优值 $\\bar{p}$ 是问题(2)的可行解，那么 $\\bar{p}$ 就一定是(2)的最优解！

如果不可行，那么，求解

$$
\\min \\;c\_i \- p^T A\_i
$$

找到一组使 $\\bar{p}$ 不可行的约束条件和对应的 $A\_i$ ，继续迭代就可以了。因此，cutting-plane method 能否应用归结于如上问题是否能高效求解！

> 加入新的约束条件时，用对偶单纯型法继续迭代。

对原问题执行列生成等价于对对偶问题执行切平面！



## Dantzig-Wolfe decomposition

考虑如下的线性规划：

$$
\\begin{aligned}
\\min \\; &  {c}\_{1}^{\\prime}  {x}\_{1}\+ {c}\_{2}^{\\prime}  {x}\_{2} \\\\
\\text { s.t. } &  {D}\_{1}  {x}\_{1}\+ {D}\_{2}  {x}\_{2}= {b}\_{0} \\\\
&  {F}\_{1}  {x}\_{1}= {b}\_{1} \\\\
&  {F}\_{2}  {x}\_{2}= {b}\_{2} \\\\
&  {x}\_{1},  {x}\_{2} \\geq  {0}
\\end{aligned} \\tag{3}
$$

假设 $b\_0, b\_1, b\_2$ 的维度分别是 $m\_0, m\_1, m\_2$，对于 $m\_1, m\_2 \\gg m\_0$ 的情况，可以设计恰当的分解算法来高效求解。

定义多面体

$$
P\_i = \\{x \\mid F\_i x = b\_i\\}
$$

于是原问题可以写成：

$$
\\begin{aligned}
\\min \\; &  {c}\_{1}^{\\prime}  {x}\_{1}\+ {c}\_{2}^{\\prime}  {x}\_{2} \\\\
\\text { s.t. } &  {D}\_{1}  {x}\_{1}\+ {D}\_{2}  {x}\_{2}= {b}\_{0} \\\\
 & x\_1 \\in P\_1, \\;\\; x\_2 \\in P\_2
\\end{aligned} \\tag{4}
$$

根据 Minkowski-Weyl 定理，一个 polyhedron 可以由若干个极点和极线构成，于是可以把 $x\_1, x\_2$ 改写成：

$$
 {x}\_{i}=\\sum\_{j \\in J\_{i}} \\lambda\_{i}^{j}  {x}\_{i}^{j}\+\\sum\_{k \\in K\_{i}} \\theta\_{i}^{k}  {w}\_{i}^{k}, \\qquad \\sum\_{j \\in J\_{i}} \\lambda\_{i}^{j}=1, \\;\\; \\lambda\_i^j , \\theta\_i^k \\geq 0 \\quad i=1,2
$$

其中 $J\_i, K\_i$ 分别表示 $P\_1, P\_2$ 的极点集，极线集。代入原问题，可得：

$$
\\begin{aligned}
\\min \\;  & \\sum\_{j \\in J\_{1}} \\lambda\_{1}^{j}  {c}\_{1}^{\\prime}  {x}\_{1}^{j}\+\\sum\_{k \\in K\_{1}} \\theta\_{1}^{k}  {c}\_{1}^{\\prime}  {w}\_{1}^{k}\+\\sum\_{j \\in J\_{2}} \\lambda\_{2}^{j}  {c}\_{2}^{\\prime}  {x}\_{2}^{j}\+\\sum\_{k \\in K\_{2}} \\theta\_{2}^{k}  {c}\_{2}^{\\prime}  {w}\_{2}^{k} \\\\
\\text { s.t. } & \\sum\_{j \\in J\_{1}} \\lambda\_{1}^{j}  {D}\_{1}  {x}\_{1}^{j}\+\\sum\_{k \\in K\_{1}} \\theta\_{1}^{k}  {D}\_{1}  {w}\_{1}^{k}\+\\sum\_{j \\in J\_{2}} \\lambda\_{2}^{j}  {D}\_{2}  {x}\_{2}^{j}  \+ \\sum\_{k\\in K\_2}\\theta\_{2}^{k}  {D}\_{2}  {w}\_{2}^{k}= {b}\_{0} \\\\
& \\sum\_{j \\in J\_{1}} \\lambda\_{1}^{j}=1 \\\\
& \\sum\_{j \\in J\_{2}} \\lambda\_{2}^{j}=1 \\\\
& \\lambda\_{i}^{j} \\geq 0, \\theta\_{i}^{k} \\geq 0, \\quad \\forall i, j, k .
\\end{aligned} \\tag{DW\-MP}
$$

这个问题叫做 Dantzig-Wolfe master problem。注意到这个等价的问题只有 $m\_0 \+ 2$ 个约束条件，当 $m\_1, m\_2$ 比较大的时候，它很好地降低了单纯型法的存储规模！但是呢，它的列数非常大（变量个数很多），一个多面体的极点、极线的个数是阶乘级别的；幸运的是，我们能够使用列生成的思想去解决它。

首先我们没有必要同时考虑那么多个极点和极限，先只取一个很小的子集，构成一个 restricted master problem（RMP）。

设 DW-RMP 的**对偶最优解**是 $p = c\_B^T B^{\-1} = \\begin{bmatrix} q & r\_1 & r\_2 \\end{bmatrix}$，变量 $\\lambda\_1^j$ 的 reduced cost 是 $\\left( {c}\_{1}^{\\prime}\- {q}^{\\prime}  {D}\_{1}\\right)  {x}\_{1}^{j}\-r\_{1}$，变量 $\\theta\_1^k$ 的 reduced cost 是 $\\left( {c}\_{1}^{\\prime}\- {q}^{\\prime}  {D}\_{1}\\right)  {w}\_{1}^{k}$. 接下来我们要去检验这些变量的检验数是否小于0，这归结于一个**更小规模**的线性规划问题：

$$
\\begin{aligned}
\\min\\; & \\left( {c}\_{1}^{\\prime}\- {q}^{\\prime}  {D}\_{1}\\right)  {x}\_{1} \\\\ 
\\text { s.t. }  &  {x}\_{1} \\in P\_{1} 
\\end{aligned} \\tag{DW\-SP}
$$

这个问题叫做 Dantzig-Wolfe subproblem （DW-SP），**子问题用来检验最优性**！

如果最优值是 $\-\\infty$，我们能找到一条极线使得 $\\left( {c}\_{1}^{\\prime}\- {q}^{\\prime}  {D}\_{1}\\right)  {w}\_{i}^{k} < 0$，这说明 $\\theta\_i^k$ 应该进基。

又或者最优值小于 $r\_1$ ，也就是能找到一个极点 $x\_i^j$ 使得 $\\left( {c}\_{1}^{\\prime}\- {q}^{\\prime}  {D}\_{1}\\right)  {x}\_{1}^{j}\-r\_{1} < 0$，这说明 $\\lambda\_i^j$ 应该进基。如果算出的最优值不小于 $r\_1$，说明达到最优了~~！

对另一组问题也是类似的：

$$
\\begin{aligned}
\\min \\; &\\left( {c}\_{2}^{\\prime}\- {q}^{\\prime}  {D}\_{2}\\right)  {x}\_{2} \\\\
\\text { s.t. } &  {x}\_{2} \\in P\_{2},
\\end{aligned}\\tag{DW\-SP}
$$

列生成在 DW 分解中扮演着非常重要的作用，把求解一个大问题分解成若干个小问题，使计算得到了简化。

这个方法可以推广到多个可分离变量上：

$$
\\begin{aligned}
\\min \\;  &  {c}\_{1}^{\\prime}  {x}\_{1}\+ {c}\_{2}^{\\prime}  {x}\_{2}\+\\cdots\+ {c}\_{t}^{\\prime}  {x}\_{t} \\\\
\\text { s.t. } &  {D}\_{1}  {x}\_{1}\+ {D}\_{2}  {x}\_{2}\+\\cdots\+ {D}\_{t}  {x}\_{t}= {b}\_{0} \\\\
&  {F}\_{i}  {x}\_{i}= {b}\_{i}, \\quad i=1,2, \\ldots, t, \\\\
&  {x}\_{1},  {x}\_{2}, \\ldots,  {x}\_{t} \\geq  {0} .
\\end{aligned} 
$$

甚至当 $t=1$ 的时候：

$$
\\begin{aligned}
\\min \\;  &  {c}^{\\prime}  {x} \\\\
\\text { s.t. }  &  {D}  {x}= {b}\_{0} \\\\
&  {F x} =  {b} \\\\
&  {x} \\geq  {0}
\\end{aligned}
$$

依然可以定义 $P = \\{x \\mid Fx = b\\}$ ，再利用 $P$ 的极点、极线来简化问题。当然，DW 分解并不拘泥于等式约束，只要约束条件的“较难”的一部分能够表达成 polyhedron 的形式即可。

经验上，DW 分解在迭代的一开始效果比较好，但是最优值的提升可能逐渐变慢，所以经常提前终止并输出一个次优解。

此外，在迭代的过程中，我们还能逐步更新问题的上界和下界。

DW-RMP 输出原问题的一个上界。


## Stochastic programming and Benders decomposition

Benders 分解借用的是 cutting-plane 的思想。

对如下的优化问题：

$$
\\begin{aligned}
\\min \\;  & c^T x \+ f^T y \\\\
\\text { s.t. }  & Ax \+ By = b \\\\
 &  y \\geq 0,  x \\in X \\subseteq \\mathrm{R}^n
\\end{aligned} \\tag{5}
$$

其中 $X$ 是一个 polyhedron。鉴于 $x, y$ 是关联（coupling）着的，问题的难度会变大。如果确定了 $x$ 能方便地计算出 $y$，那么就可以用 Benders 分解来使问题得到简化。

> 这里的 $x$ 还可以是整数变量，$y$ 是连续取值的。$x$ 确定了，求 $y$ 就是一个简单的线性规划了。



首先，改写为关于 $x$ 的优化问题：

$$
\\begin{aligned}
\\min \\;  & c^T x \+ z \\\\
\\text { s.t. } &  x \\in X \\subseteq \\mathrm{R}^n
\\end{aligned} \\tag{6}
$$

式(6)称为 BD-Master Problem，其中：

$$
z = z(x)= \\left [ \\begin{aligned}
\\min \\;  &f^T y \\\\
\\text { s.t. }  & Ax \+ By = b,  y \\geq 0
\\end{aligned}\\right] = \\left[ 
\\begin{aligned}
\\max \\;  & \\;\\alpha^T (b\-Ax)\\\\
\\text { s.t. }  & B^T \\alpha \\leq f
\\end{aligned} \\right]
$$

根据假定（原问题关于 $x$ 困难而关于 $y$ 容易），给出 $x$，计算 $g(x)$ 是一件轻松的事情。但是，我们还得从对偶问题来计算 $g(x)$，**注意到右侧的对偶问题的可行域是与 $x$ 无关的**。记右侧这个对偶问题为 BD-Subproblem。

记多面体 $P = \\{\\alpha \\mid B^T \\alpha \\leq f\\}$，如果 $P$ 是空集，那么，由线性规划的弱对偶性，原问题无解（不可行）或者最优值无界。以下假设 $P$ 是非空的。

式(6)可以改写为：

$$
\\begin{aligned}
\\min \\;  & c^T x \+ z \\\\
\\text { s.t. } &  x \\in X \\subseteq \\mathrm{R}^n \\\\
 & \\alpha^T\_i (b \- Ax) \\leq z,\\;\\; \\forall \\alpha\_i \\in J\_P \\\\
 & \\alpha\_j^T (b \- Ax) \\leq 0, \\;\\; \\forall \\alpha\_j \\in K\_P
\\end{aligned} \\tag{7}
$$

$J\_P, K\_P$ 分别表示 $P$ 的极点、极线组成的集合。注意到 Master Problem 的约束条件非常多。式(7)的最优值和式(5)是一样的。



令 $J\_P^\\prime =K\_P^\\prime = \\emptyset$，取一个 $x\_0$ 开始迭代，如果对偶子问题无上界，那么这意味着原问题无解，解对偶子问题能得到一条极线 $w\_0$，将   $w\_0$ 加入到 $K\_P^\\prime$，这样的 $x\_0$ 对于原始的问题(5)是不可行的！

> $w\_0$ 导致了一个 Benders feasibility cut.

现在假定对偶子问题是有界的，那么说明 $x\_0$ 是式(5)的可行解，于是我们能得到原始问题的一个上界 $\\mathrm{UB} = c^T x\_0 \+ z(x\_0)$；同时，解 relaxed master problem：

$$
\\begin{aligned}
\\min \\;  & c^T x \+ z \\\\
\\text { s.t. } &  x \\in X \\subseteq \\mathrm{R}^n \\\\
 & \\alpha^T\_i (b \- Ax) \\leq z,\\;\\; \\forall \\alpha\_i \\in J\_P^\\prime \\\\
 & \\alpha\_j^T (b \- Ax) \\leq 0, \\;\\; \\forall \\alpha\_j \\in K\_P^\\prime
\\end{aligned}
$$

可以得到一个下界 $\\mathrm{LB}$，如果 $\\mathrm{LB} = \\mathrm{UB}$，那么迭代停止，输出最优解。如果 $\\mathrm{UB} \\geq \\mathrm{LB}$，就要向 BD-RMP 添加 Benders optimality cut，在计算用对偶子问题计算 $z(x\_0)$ 的时候，得到的极点 $v\_0$ 加入到 $J\_P^\\prime$，继续迭代即可。


Benders 分解解决的是一类具有特殊形式的规划问题，大规模随机规划刚好具有这样的形式。
$$
\\begin{aligned}
\\min \\; &  c^T x &  \+ \\alpha\_1 f^T y\_1  & \+  \\alpha\_2 f^T y\_2 \+ \\dots & \+ \\alpha\_K f^T y\_K \\\\
\\text{ s.t. } & Ax &   &   &&=b \\\\
& B\_1 x  & \+ Dy\_1 &  & &=  d\_1 \\\\
& B\_2 x  &  & \+  D y\_2 & &  = d\_2 \\\\
& \\vdots &&&& \\vdots \\\\
& B\_K x  &&& \+ Dy\_K & = d\_K \\\\
& x, y\_1, \\dots, y\_k \\geq 0 \\\\
\\end{aligned}
$$


Scenario 的个数 $K$ 一般很大，而第一阶段的决策 $x$ 确定下来之后，每个 $y\_k$  的计算是若干个小的子问题。

令：

$$
\\begin{aligned}
z\_{\\omega}(  {x})=  \\left[
\\begin{aligned} 
\\min \\;&   {f}^{\\top}   {y}\_{\\omega} \\\\
\\text { s.t. } &   {B}\_{\\omega}   {x}\+  {D}   {y}\_{\\omega}=  {d}\_{\\omega} \\\\
&   {y}\_{\\omega} \\geq  {0} .
\\end{aligned}\\right]
\\end{aligned} = \\left[
\\begin{aligned}
\\max \\;\\; &   {p}\_{\\omega}^{\\top}\\left(  {d}\_{\\omega}\-  {B}\_{\\omega}   {x}\\right) \\\\
\\text { s.t. } &   {p}\_{\\omega}^{\\top}   {D} \\leq   {f}^{\\top}
\\end{aligned}
\\right]
$$

问题化为关于 $x$ 的：

$$
\\begin{array}{ll}
\\min &   {c}^{\\top}   {x}\+\\sum\_{w=1}^{K} \\alpha\_{\\omega} z\_{\\omega}(  {x}) \\\\
\\text { s.t. } &   {A x}=  {b} \\\\
&   {x} \\geq  {0} .
\\end{array}
$$


## Summary

本文总结了求解大规模线性规划问题的算法思路。
