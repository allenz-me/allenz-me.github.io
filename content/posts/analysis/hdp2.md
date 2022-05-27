---
title: "2. Concentration of sums of independent random variables"
date: 2021-01-01
draft: false
slug: hdp2
categories: ["分析与概率", "高维概率"]
tags: ["正态分布", "次高斯分布"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


<!-- #! https://zhuanlan.zhihu.com/p/413301756

# Concentration of sums of independent random variables -->

本文总结自 高维概率 第二章

<!-- 本书：

[HDP-book.pdf](https://uploader.shimo.im/f/CwR4dIKrjpcCDJgR.pdf?fileGuid=DGdRyQyhVkdyvcWd)

某大佬做的视频链接：

[https://www.bilibili.com/video/BV1gZ4y1W7ED](https://www.bilibili.com/video/BV1gZ4y1W7ED)

[https://www.bilibili.com/video/BV1kQ4y1P7y9](https://www.bilibili.com/video/BV1kQ4y1P7y9) -->


本书第二章主要讲的是多个独立随机变量的和，它们在均值附近的集中程度。

## Probability Concentration

现在我们要考虑的是一个probability concentration的问题，也可以说是去研究概率分布的尾巴，就像这样：

$$
\mathbb{P}\{|X-\mu|>t\} \leq \text { something small. }\\
$$

在随机变量方差存在的情况下，我们有切比雪夫不等式。它利用到了随机变量的方差，而且它的界是紧的，即我们总可以构造出一个随机变量使切比雪夫不等式取等号。但是，对于一些常见的概率分布而言，无论是正态分布还是指数分布等，切比雪夫不等式给出的界都显得太过粗糙。

最为经典的正态分布自然第一个成为我们的“靶子”，容易证明正态分布的尾巴是一个以指数速度 $\frac{1}{t}e^{-t^2/2}$ 收敛于 0 的。如果 $g \sim \mathcal{N}(0, 1)$，那么：

$$
\left(\frac{1}{t}-\frac{1}{t^{3}}\right) \cdot \frac{1}{\sqrt{2 \pi}} e^{-t^{2} / 2} \leq \mathbb{P}\{g \geq t\} \leq \frac{1}{t} \cdot \frac{1}{\sqrt{2 \pi}} e^{-t^{2} / 2}\\
$$

这不难从正态分布的CDF推出。虽然中心极限定理告诉我们任何分布的标准化都趋向于正态分布，但是 CLT 的误差界却是 $1/\sqrt{N}$ 的（Berry-Esseen CLT），能保证的收敛速度很慢，我们无法借助它来严格推导任意分布的尾巴，这逼迫我们寻找新的方法。

## Hoeffding Inequality

从对称伯努利分布的和出发，即设 $\mathbb{P}\{X=-1\}=\mathbb{P}\{X=1\}=\frac{1}{2}$，那么 $X$ 的矩母函数：

$$
\mathbb{E}[e^{\lambda X}] = \frac{e^\lambda + e^{-\lambda}}{2} \leq e^{\frac{\lambda^2}{2}}  \\
$$

从而：

$$
\mathbb{P}\left\{S_{n} = \sum_{i=1}^n X_i  \geq t\right\}=\mathbb{P} \left\{e^{\lambda S_{n}} \geq e^{\lambda t}\right\} \leq \frac{E\left[e^{\lambda S_{n}}\right]}{e^{\lambda t}} = \frac{ \prod_{i=1}^n E\left[e^{\lambda X_{i}}\right]}{e^{\lambda t}}  \leq e^{\frac{n}{2}\lambda^2 - \lambda t} \\
$$

取 $\lambda = \displaystyle\frac{t}{n}$，就有 $\mathbb{P}\{S_n \geq t \} \leq e^{-\frac{t^2}{2n}}$ ；同时不难得到 $\mathbb{P}\{S_n \geq \sqrt{-2n \ln \epsilon}\} \leq \epsilon$，即 $S_n \sim O(\sqrt{n})$。

我们借助矩母函数，说明了对称伯努利分布的和的尾巴是指数速度趋于0的。使用相同的方法，可以得到**针对有界随机变量的Hoeffding不等式**：

$$
\forall t > 0, \;\; X_i \in [m_i, M_i] \quad\Longrightarrow \quad\mathbb{P}\left\{\sum_{i=1}^{N}\left(X_{i}-\mathbb{E} X_{i}\right) \geq t\right\} \leq \exp \left(-\frac{2 t^{2}}{\sum_{i=1}^{N}\left(M_{i}-m_{i}\right)^{2}}\right)\\
$$

在推导的过程中，主要用到了 Hoeffding 引理 $\mathbb{E}[e^{\lambda (X - \mathbb{E}[X])}] \leq e^{\lambda^2(M-m)^2/8}$ 和技巧：

$$
\mathbb{P}(X \geq t) = \mathbb{P}(e^{\lambda X} \geq e^{\lambda t}) \leq \frac{\mathbb{E}[e^{\lambda X}]}{e^{\lambda t}}, \;\forall \lambda \geq 0 \Longrightarrow \mathbb{P}(X \geq t) \leq \min_{\lambda \geq 0} \frac{\mathbb{E}[e^{\lambda X}]}{e^{\lambda t}}\\
$$

$E[e^{\lambda X}]$ 是 $X$ 的矩母函数，独立随机变量和的矩母函数等于其矩母函数的乘积！

注意到正态分布也成立 Hoeffding 不等式，但正态分布并不是有界的，这说明 Hoeffding 不等式可以在某些条件下推广到无界的分布，这也是我们提出次高斯分布的原因。

通过 Hoeffding 不等式我们知道，有界随机变量的和，以及正态分布的尾巴是以 $e^{-t^2}$ 这一速度趋于0的，但并不是所有的分布都能达到这种速度。比如我们熟知的指数分布，它就是 $e^{-t}$ 级别的收敛速度。

Chernoff 不等式对于0-1伯努利分布的和给出了一个更好的界，由二项分布的泊松近似可知参数为 $\lambda$ 的泊松分布的右尾满足：$\forall t > \lambda, \; \mathbb{P}\{X \geq t\} \leq e^{-\lambda}\left(\frac{e \lambda}{t}\right)^{t}$，这说明泊松分布的尾的收敛速度是 $e^{-t \ln t}$ 级别的。这个尾巴也可以从上面提到的技巧来证明。

## Sub-gaussian Distribution

正态分布可能是以 $e^{-t^2}$ 为尾概率的最为典型的分布了，我们都知道正态分布出现均值外3个标准差的概率是很小的，它的集中度是很高的，这种良好性质又足以拓展到其它的分布，我想这也是次高斯分布提出的原因之一。

次高斯分布一般都是值零均值的分布，零均值也能方便我们讨论问题，它有若干条等价定义：

+ $X$ 的尾巴满足：

$$
\mathbb{P}\{|X| \geq t\} \leq 2 \exp \left(-t^{2} / K_{1}^{2}\right) \quad \text { for all } t \geq 0 \\
$$

+ $X$ 的矩满足：

$$
\|X\|_{L^{p}}=\left(\mathbb{E}|X|^{p}\right)^{1 / p} \leq K_{2} \sqrt{p} \quad \text { for all } p \geq 1 \\
$$

+ $X^2$ 的矩母函数满足：

$$
\mathbb{E} \exp \left(\lambda^{2} X^{2}\right) \leq \exp \left(K_{3}^{2} \lambda^{2}\right) \quad \text { for all } \lambda \text { such that }|\lambda| \leq \frac{1}{K_{3}} \\
$$

+ $X^2$ 的矩母函数在某一点有界：

$$
\mathbb{E} \exp \left(X^{2} / K_{4}^{2}\right) \leq 2 \\
$$

+ $X$ 的矩母函数满足：

$$
\mathbb{E} \exp (\lambda X) \leq \exp \left(K_{5}^{2} \lambda^{2}\right) \quad \text { for all } \lambda \in \mathbb{R} \\
$$

除去分布的尾巴，**矩母函数/高阶矩也能刻画分布的集中程度**。期望不存在的分布一定不是次高斯（次指数）分布！

对于次高斯分布还有次高斯模（sub-gaussian norm）的概念：

$$
\|X\|_{\psi_{2}}=\inf \left\{t>0: \mathbb{E} \exp \left(X^{2} / t^{2}\right) \leq 2\right\}\\
$$

次高斯模有界的分布都是次高斯分布。

>次高斯模和后面定义的次指数模都是相应函数族空间中的范数。

类似于正态分布方差具有可加性，次高斯随机变量的和的次高斯模满足：

$$
\left\|\sum_{i=1}^{N} X_{i}\right\|_{\psi_{2}}^{2} \leq C \sum_{i=1}^{N}\left\|X_{i}\right\|_{\psi_{2}}^{2}\\
$$

这个性质使得我们可以推出次高斯分布和的**广义Hoeffding不等式**：

$$
\mathbb{P}\left\{\left|\sum_{i=1}^{N} X_{i}\right| \geq t\right\} \leq 2 \exp \left(-\frac{c t^{2}}{\sum_{i=1}^{N}\left\|X_{i}\right\|_{\psi_{2}}^{2}}\right)\\
$$

这就是说，次高斯分布和次高斯分布的和，它们的尾巴都具有以 $e^{-t^2}$ 的速度趋近于0的良好性质！

另外，对于非零均值的分布，因为

$$
\|X-\mathbb{E} X\|_{\psi_{2}} \leq\|X\|_{\psi_{2}}+\|\mathbb{E} X\|_{\psi_{2}} \Rightarrow \|X-\mathbb{E} X\|_{\psi_{2}} \leq C\|X\|_{\psi_{2}}\\
$$

一样可以写出其零均值化后的形式。于是，广义的Hoeffding不等式与之前针对有界随机变量的Hoeffding不等式实现了优美的统一。

***McDiarmid 1998***

*注：有界随机变量的 Hoeffding 不等式的另一种推广是 McDiarmid’s inequality，如果* $f:\mathrm{R}^n \to \mathrm{R}$ *是可测函数，* $X$ *是* $n$ *维随机向量，并且：*
$$
\left|f\left(x_{1}, \ldots, x_{i}, \ldots, x_{n}\right)-f\left(x_{1}, \ldots, x_{i}^{\prime}, \ldots, x_{n}\right)\right| \leq c_{i}, \forall i =1, 2, ..., n\\
$$

*那么：*

$$
\mathbb{P}\{f(X)-\mathbb{E} f(X) \geq t\} \leq \exp \left(-\frac{2 t^{2}}{\sum_{i=1}^{n} c_{i}^{2}}\right)\\
$$

*注意到取* $f(X)=\sum_{i=1}^n X_i$ *就刚好是 Hoeffding 不等式。*

## Sub-exponential Distributions

次高斯分布拓展了高斯分布的尾概率的性质，但它还不够广泛，并不是所有的分布都有那么细的尾巴。比如说，正态分布的平方和，卡方分布，和指数分布等，它们的尾巴就只是 $e^{-t}$ 阶的。

仿照次高斯分布，我们不难定义次指数分布，我觉得指数分布可以说是这类分布中最典型的了，

同样地，还有次指数模的概念：

$$
\|X\|_{\psi_{1}}=\inf \,\{t>0: \mathbb{E} \exp (|X| / t) \leq 2\}\\
$$

结合两个定义，**次高斯分布的平方恰好就是次指数分布**，并且$\left\|X^{2}\right\|_{\psi_{1}}=\|X\|_{\psi_{2}}^{2}$。两个次高斯分布的积是次指数的，并且$\|X Y\|_{\psi_{1}} \leq\|X\|_{\psi_{2}}\|Y\|_{\psi_{2}}$。

次指数分布有Bernstein不等式来刻画它的集中程度：

$$
\mathbb{P}\left\{\left|\sum_{i=1}^{N} X_{i}\right| \geq t\right\} \leq 2 \exp \left[-c \min \left(\frac{t^{2}}{\sum_{i=1}^{N}\left\|X_{i}\right\|_{\psi_{1}}^{2}}, \frac{t}{\max _{i}\left\|X_{i}\right\|_{\psi_{1}}}\right)\right]\\
$$

该不等式也容易由$\|X-\mathbb{E} X\|_{\psi_{1}} \leq C\|X\|_{\psi_{1}}$推广到非零均值随机变量。

Bernstein不等式的意思是，在均值附近，衰减速度接近高斯分布的衰减速度，远离均值的部分，则是以指数分布的尾巴衰减的，这与泊松分布（二项分布的极限）是类似的。Bernstein不等式下面这种形式反映了该思想：

$$
\mathbb{P}\left\{\left|\frac{1}{\sqrt{N}} \sum_{i=1}^{N} X_{i}\right| \geq t\right\} \leq\left\{\begin{array}{ll}2 \exp \left(-c t^{2}\right), & t \leq C \sqrt{N} \\2 \exp (-t \sqrt{N}), & t \geq C \sqrt{N}\end{array}\right.\\
$$

当$|X| \leq K$是有界随机变量的时候，Bernstein不等式还可以写为如下的形式：

$$
\mathbb{P}\left\{\left|\sum_{i=1}^{N} X_{i}\right| \geq t\right\} \leq 2 \exp \left(-\frac{t^{2} / 2}{\sigma^{2}+K t / 3}\right)\\
$$

本章的最后一节还提到了两个重要的不等式，其中一个是 McDiarmid 不等式，已经介绍过了，另一个是 Bennett 不等式：

$$
\mathbb{P}\left\{\sum_{i=1}^{N}\left(X_{i}-\mathbb{E} X_{i}\right) \geq t\right\} \leq \exp \left(-\frac{\sigma^{2}}{K^{2}} h\left(\frac{K t}{\sigma^{2}}\right)\right)\\
$$

其中 $| X_i - \mathbb{E}[X_i] | \leq K$，$\sigma^2 = \sum_{i=1}^N \operatorname{var}(X_i), \; h(u) = (1 + u) \ln (1 + u) - u.$ 

## Further Thoughts

本章主要讲的是如何去刻画随机变量的集中程度，由此提出了次高斯分布和次指数分布的这两个概念，它们是我们熟悉的正态分布和指数分布的推广。

如果一个分布的尾巴比指数分布还要厚，比如它是多项式速度 $t^{-k}$ 衰减到0的，统计学上称它为重尾分布（heavy-tail）。比如柯西分布、对数正态分布、某些帕累托分布。


（离散）鞅可以由一串零均值独立随机变量相加而得，如果 $X_0=0$，那么鞅差序列 $\{X_n - X_{n-1}, n \geq 1\}$是互不相关的（而不是独立的）。在此基础上有 Azuma 不等式：

如果 $| X_i - X_{i-1} | \leq c_i$，那么成立：

$$
P(|X_n - X_0 | \geq a) \leq 2e^{-a^2 / (2 \sum_i c_i^2)}\\
$$

