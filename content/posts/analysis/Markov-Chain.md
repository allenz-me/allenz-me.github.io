---
title: "Markov Chain"
date: 2021-12-21
draft: false
toc: true
slug: lecture4-cont
categories: ["分析与概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


## 离散时间的 Markov 链

记 $\\mathcal{F}\_n = \\sigma(X\_1, X\_2, \\dots, X\_n)$，定义满足如下条件的随机过程 $\\{X\_n, \\, n\\geq 1\\}$ 为离散时间的 Markov 链：

$$
P(X\_{n\+1} \\in B \\mid \\mathcal{F}\_n) = P(X\_{n\+1} \\in B \\mid \\sigma(X\_n)) \\quad a.s.
$$

更为通俗的定义是：
$$
P(X\_{n\+1}=j \\mid X\_{n}=i, \\cdots, X\_{1}=i\_{1}, X\_{0}=i\_{0})=P(X\_{n\+1}=j \\mid X\_{n}=i)
$$
即 $n\+1$ 时刻的状态分布只跟 $n$ 时刻的状态有关，而与 $n\-1$ 时刻之前的状态无关。



一般都会假定状态转移的概率与时间无关，如果 Markov 链只有可列个（countable）状态，就可以用 $p\_{ij}$ 来表示从 $i$ 转移到 $j$ 的概率。对于有限个状态，我们能得到一个 Markov 矩阵。



### Chapman-Kolmogorov 方程


$$
p\_{i j}^{(n\+m)}=\\sum\_{l \\in \\mathcal{S}} p\_{i l}^{(n)} \\times p\_{l j}^{(m)}, \\forall n, m \\in \\mathbb{Z}\_{\+}
$$





### 状态类

如果对某个 $n\\geq0$，有 $p\_{ij}^n > 0$，则说 $j$ 是可从 $i$ 到达的（accessible），可相互到达的两个状态称为互通的（communicate）。

**互通是一个等价关系**，由此，状态集 $\\mathcal{S}$ 可以划分为几个等价类（商集）。

如果 Markov 链只有一个类，就说它是**不可约**的（irreducible）。



#### 周期性

状态 $i$ 称为具有周期 $d$，若只要 $n$ 不能被 $d$ 整除时就有 $P^n\_{ii}=0$，且 $d$ 是具有此性质的最大整数。

周期为1的状态称为非周期的（aperiodic）。

例如：对于一维的 random walk，所有的类都是互通的，并且有周期为 2.

周期性也是等价类的一个性质！


#### 常返性

状态 $i$ 是常返的（recurrent state），如果从 $i$ 出发的过程以概率 1 的会返回 $i$， 否则就说它是暂态的（transient state）。

> 如果 $p\_{ii}=1$，则 $i$ 是吸收态（absorbing state），这是一种特殊的 recurrent state. 这个类只有一个元素

记 $f\_{ij}^n$ 为开始处在 $i$ 而转移到 $j$ 在时刻 $n$ 首次发生的概率，$f\_{ij} = \\sum\_{n=1}^{\\infty} f\_{ij}^n$ 是从 $i$ 迟早转移到 $j$ 的概率。从而，$i$ 是常返当且仅当 $f\_{ii}=1$.



状态 $j$ 是常返的，当且仅当：
$$
\\sum\_{n=1}^\\infty P^n\_{jj} = \\infty
$$
这意味着 $X\_0 = j$ 下，访问 $j$ 的次数的期望是 $\\infty$.

另一方面，假设 $j$ 是暂态的，则返回次数是以均值为 $1/(1\-f\_{jj})$ 为均值的几何随机变量。



依旧考虑一维的随机徘徊：$P\_{i, i\+1} = 1 \- P\_{i, i\-1}= p$. 

显然所有的状态都互通，所以要么都是暂态，要么都是常返，所以只考虑状态 $0$.

对此，有：
$$
P\_{00}^{2n\+1} = 0, \\quad P\_{00}^{2n} = \\frac{(2n)!}{n!n!} p^n(1\-p)^n
$$
欲判断 $\\sum\_{n=1}^{\\infty} P\_{00}^{2n}$ 这个级数的收敛性

...



进一步，定义 $\\mu\_{jj} = \\sum\_{n=1}^\\infty n f\_{ii}^n$ ，易知如果 $j$ 是暂态，那么 $\\mu\_{jj} = \\infty$. 

现在，如果 $j$ 是常返且 $\\mu\_{jj}  < \\infty$ 就说 $j$ 是正常返（positive recurrent），否则就称为零常返（null recurrent）。



暂态、正常返和零常返都是等价类的性质。





### 极限定理

正常返的非周期状态称为遍历的（ergodic）。



一个不可约的非周期的 Markov 链必属于下列两类之一：

1. 一切状态或都是暂态，或都是零常返。此时 $\\displaystyle\\lim\_{n \\to \\infty} P\_{ij}^n = 0$，且不存在平稳分布。
2. 一切状态都是正常返，且 $\\pi\_j = \\displaystyle \\lim\_{n \\to \\infty} P\_{ij}^n > 0$，是唯一的平稳分布。

对于第2类我们称这样的 Markov 链为遍历链。

注意到第1类必然存在无穷多个状态，比如1维随机徘徊就是一个典型的例子。









### 类之间的转移

常返类是一个封闭的类，即，如果 $R$ 是一个常返类，且 $i \\in R, j \\notin R$，则 $P\_{ij} = 0$.

根据定义，这个命题是好理解的。**在一个 Markov 链，只可能出现暂态转移到常返，不可能出现常返转移到暂态。**





### 分支过程




## 连续时间的 Markov 链

定义在 $(\\Omega, \\mathcal{F}, \\mathbb{P}, (\\mathcal{F\_t})\_{t\\in T})$ 的连续时间随机过程 $X\_t$ 是 Markov 过程，如果：

$$
P(X\_{t\+s} \\in B \\mid \\mathcal{F}\_t) = P(X\_{t\+s} \\in B \\mid \\sigma(X\_t)) \\quad a.s.
$$

更为通俗的形式是：
$$
{P}(X(t\+s)=j \\mid X(s)=i, X(u)=x(u), 0 \\leqslant u<s)={P}(X(t\+s)=j \\mid X(s)=i)
$$
在专门研究连续时间 Markov 链的时候，依然会假定至多只有可数多个状态，

> 布朗运动是一种连续时间的 Markov 链，但是状态数量有不可数个。



### 转移速率

以 $T\_i$ 记一个 Markov 链进入状态 $i$ 且在离开之前所经历的时间，根据 Markov 性质，易知：
$$
{P}\\left(T\_{i}>s\+t \\mid T\_{i}>s\\right)={P}\\left(T\_{i}>t\\right)
$$
这说明 $T\_i$ 具有无记忆性，必须服从指数分布。

即，连续时间 Markov 链在每个状态 $i$ 停留的时间服从参数（速率）为 $v\_i$ 的指数分布。如果 $v\_i = 0$，则这个状态是吸收的。$v\_i$ 越大，则在状态 $i$ 停留的平均时间越短。如果 $v\_i = \\infty$，那么 $i$ 是一个瞬时状态。

称一个连续时间的 Markov 链是正则的（regular），如果它在任意有限长时间段内转移次数以概率1的有限。

例：$P\_{i, i\+1} = 1, v\_i = i^2$ 就是一个非正则的 Markov 链。



对 $i\\neq j$，定义 $q\_{ij} = v\_i P\_{ij}$ 为从 $i$ 转移到 $j$ 的速率。



### 生灭过程

用一个连续时间的 Markov 过程来表示一个群体的数量，如果状态 $i \\geq 0$ 只能转移到状态 $i\+1$ 或者 $i\-1$，这就是一个生灭过程（birth and death process）。

令：
$$
\\lambda\_i = q\_{i, i\+1}, \\quad \\mu\_i = q\_{i, i\-1}
$$
值 $\\lambda\_i, \\mu\_i$ 分别成为出生率、死亡率。易知：
$$
v\_i = \\lambda\_i \+ \\mu\_i, \\quad P\_{i, i\+1} = \\frac{\\lambda\_i}{\\lambda\_i \+ \\mu\_i} = 1 \- P\_{i, i\-1}
$$
如果 $\\mu\_i = 0, \\forall i$ 就说这是一个纯生过程（pure birth），Poisson 过程是最简单的纯生过程，它有常数的出生率 $\\lambda\_i = \\lambda$.

如果出生率正比于种群数量，即 $\\lambda\_i = i \\lambda$，这种纯生过程叫做 Yule 过程。



### Kolmogorov 微分方程

记：
$$
P\_{ij}(t) = P(X(t\+s) = j \\mid X(s) = i)
$$
为处于状态 $i$ 并在一个时间 $t$ 后处在状态 $j$ 的概率。

