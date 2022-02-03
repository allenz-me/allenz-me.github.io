---
title: "Convex Optimization Problem"
date: 2022-02-05
draft: true
slug: convex-opt-problem
categories: ["运筹与优化"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


# Convex optimization problem

凸集和凸函数，都是为了解决凸优化问题做的铺垫。当然，在这之前，我们还应当对整个优化问题的概念体系有一个大致的了解。

## 优化问题

### 基本术语


一个标准的优化问题，通常都由：优化变量、目标函数、不等式约束、等式约束组成：

> *optimization variable, objective function, inequality constraints, equality constraints.*

$$
\begin{array}{ll}
\operatorname{minimize} & f_{0}(x) \\
\text {subject to } & f_{i}(x) \leq 0, \quad i=1, \ldots, m \\
& h_{i}(x)=0, \quad i=1, \ldots, p
\end{array}\tag{1}
$$

满足等式约束和不等式约束的值叫做优化问题的**可行域（feasible set）**。可行域也要包含在所有函数的定义域内。

如果优化问题没有约束条件，就说这个问题是无约束的（unconstrained）。

我们将可行域内 $f_0(x)$ 的**下确界**定义为问题的 *optimal value*。

$$
p^{*}=\inf_{x\in D} f_0(x)
$$

我们允许 $p^*$ 取值为 $\pm \infty$。如果可行域是空集，我们取 $p^*=+\infty$；如果存在点列 $x_k$ 使得 $f_0(x_k) \to -\infty \;(k\to \infty)$，就取 $p^* = -\infty$，并称这个问题是无界的（unbounded below）。

如果 *optimal value* 在问题的可行域内可以取到，即 $f_0(x^*)=p^*$，就称 $x^*$ 是问题的**最优解（optimal point）**，注意不是所有问题都能取到最优解。所有的 optimal point 构成 **最优集（optimal set）**。

如果该优化问题的最优集不为空，那么就算这个问题是**可解的（solvable）**，容易看到，并不是所有的可行域非空的优化问题都是可解的。大多数不可解的问题都是无界的问题。

> 约束优化问题 $\displaystyle\min_{x\in \mathrm{R}_{+}}f_0(x) = \displaystyle\frac{1}{x}$ 的最优值 $p^*=0$，但是最优集为空，因此它是不可解的。

虽然有时候最优解不存在或者很难计算，但我们可以引入 $\epsilon$-*suboptimal* 的解。使得 $f_0(x) \leq p^* + \epsilon$ 的 $x$ 可以作为一个 $\epsilon$ 近似的解。

除去以上所说的全局最优（globally optimal）解的概念，还可以引入一种局部最优（locally optimal）的概念。$x$ 是局部最优仅需要它在一个足够小的领域内是最优的。

对于不等式约束条件，如果 $f_i(x)<0$，我们就说约束条件 $f_i(x)\leq 0$ 在 $x$ 处是 *inactive* 的。不等式约束条件到底有没有起作用，在优化理论中被广泛研究。

如果令优化问题的目标函数恒等于0，那么这个问题的最优解要么是0，要么是 $+\infty$。研究类似的优化的问题的意义是，最优解可以揭示问题的可行域是否非空。
$$
\begin{array}{ll}
\operatorname{minimize} & 0 \\
\text {subject to } & f_{i}(x) \leq 0, \quad i=1, \ldots, m \\
& h_{i}(x)=0, \quad i=1, \ldots, p
\end{array}
$$

### 优化问题的标准形式

优化问题的标准形式如本文式(1)。事实上，很多实际问题被提出的时候并不是标准形式，但是我们总能够将它们化为标准形式。

比如最大值问题添加一个负号就能变成最小值问题。因为凸函数具有全局的最小值点，所以习惯上我们还是考虑最小值问题。


### 问题的等价形式（equivalent problems）

通过一定的变换，我们可以把一个优化问题变成与它等价的另一个优化问题。有时候，这样的操作可以帮助我们简化问题的求解。我们称两个优化问题等价，当且仅当解决其中一个问题能够立马得到另一个问题的最优解。

+ 变量代换

如果现在有一个 $\mathrm{R}^n \to \mathrm{R}^n$ 的双射 $\phi$，将 $x=\phi(z)$ 代入标准形式(1)得到的另一个关于 $z$ 的优化问题仍然与原问题等价。

+ 对目标函数或约束函数做变换

设 $\psi_0(x)$ 是单调递增的函数，那么 $\displaystyle\min_{x \in \mathcal{D}} f_0(x)$ 等价于 $\displaystyle\min_{x \in \mathcal{D}} \psi_0(f_0(x))$。

例：

$\min \|A x - b\|_2$ 等价于 $\min \|A x - b \|_2^2 = (Ax - b)^T (Ax - b)$

对约束条件做类似的等价变换也是可行的。

+ 松弛变量

比如，在线性规划的单纯形法中，我们通过添加松弛变量将问题化为线性规划的标准形式。添加松弛变量得到的新问题仍然与原问题等价。
$$
f_i(x) \leq 0 \Leftrightarrow f_i(x) + s_i = 0,\; s_i \geq 0
$$

+ Epigraph 形式

引入新变量 $t \in \mathrm{R}$，优化问题(1)可等价地转换为：
$$
\begin{aligned}
&\text {minimize  }\;\;\quad t\\
&\begin{array}{ll}
\text {subject to } & f_{0}(x)-t \leq 0 \\
& f_{i}(x) \leq 0, \quad i=1, \ldots, m \\
& h_{i}(x)=0, \quad i=1, \ldots, p
\end{array}
\end{aligned}
$$

许多优化问题都会使用这种处理方式。

> 一点点欠缺



### 黑盒式优化问题（oracle model）

教科书上的优化问题往往都是参数式的优化问题，目标函数 $f_0(x)$ 有一个给定的形式。但也有时候，目标函数会是一个黑盒子（black box），它由一个程序给出，我们输入一个 $x$，程序返回 $f_0(x)$。

二次规划、二阶锥规划，它们有明确的形式，因此可以对此设计高效的算法；而一些形式不特殊或者是黑盒式的目标函数（比如神经网络），就很难为此设计独特的解法。如求解神经网络的梯度下降法，就是一种通用型的方法。



### 最优性条件

#### 可行方向

对于给定的 $x \in \mathcal{D}$，如果存在 $\bar{\alpha}$，使得 $\forall \alpha\; (0 \leq \alpha \leq \bar{\alpha})$，都有 $x + \alpha d \in \mathcal{D}$，就称向量 $d$ 是在 $x$ 处的可行方向（feasible direction）。

以下条件都假设目标函数二次可微。

#### 一阶必要条件

 如果 $x^*$ 是 $f(x)$ 在 $\mathcal{D}$ 上的局部极小值，那么对于 $x^*$ 处任意一个可行方向 $d$ ，都有 $\nabla f(x^*) ^T d \geq 0$。这意味着沿着 $x^*$ 的任意一个可行方向，函数值都是上升的。

一个重要的特殊情形是 $x^*$ 位于 $\mathcal{D}$ 内部时，此时所有的方向都是可行方向，所以必须成立 $\nabla f(x^*) = 0$。这也是无约束最优化局部极小值的必要条件。

#### 二阶必要条件

 如果 $x^*$ 是 $f(x)$ 在 $\mathcal{D}$ 上的局部极小值，那么对于 $x^*$ 处任意一个可行方向 $d$ ，有：

1. $\nabla f(x^*)^T d \geq 0$
2. 如果 $\nabla f(x^*)^T d = 0$，那么 $d^T \nabla^2 f(x^*) d \geq 0$

二阶条件是通过 Taylor 展开来证明的。对应的无约束或内点情形，就是 $\nabla f(x^*) = 0, \nabla^2 f(x^*) \succeq 0$。即梯度为0，Hessian 矩阵半正定。

#### 二阶充分条件

极小点在可行域边界处达到的充分条件较难刻画。

但如果 $x^*$ 是 $\mathcal{D}$ 的内点，只要 $\nabla f(x^*) = 0, \nabla^2 f(x^*) \succ 0$，即可保证 $x^*$ 是局部极小点。





## 凸优化

通俗地说，凸优化问题，就是目标函数是凸函数，并且可行域是凸集的优化问题。

$$
\begin{array}{ll}
\operatorname{minimize} & f_{0}(x) \\
\text {subject to } & f_{i}(x) \leq 0, \quad i=1, \ldots, m \\
& a_{i}^{T} x=b_{i}, \quad i=1, \ldots, p
\end{array}
$$

凸优化问题的标准形式，与一般优化问题的相比，**要求目标函数 $f_0(x)$ 和不等式约束函数 $f_1(x), ..., f_m(x)$ 都是凸函数，并且等式约束都是线性的。** 

这样的约束条件，保证了**问题的可行域是凸集**！

如果目标函数不是凸的，是拟凸的，那么这个问题就是一个拟凸优化问题（*quasiconvex optimization problem*）

当目标函数和不等式约束都变成凹函数并且是求最大值，这个问题叫做凹优化问题。凹优化问题和凸优化问题本质是一样的。

### 凸优化的最优性

凸优化，相比与一般的优化问题，有一个非常好的性质，那就是：**任何一个局部最优点（locally optimal）都是全局最优点（globally optimal）**。

> 对于拟凸优化问题而言，局部最优不一定导致全局最优。





如果目标函数是可微的，那么还有一个判断最优点的准则：
**设 $X$ 是可行域，$x$ 最优 $\Longleftrightarrow\nabla f_{0}(x)^{T}(y-x) \geq 0\;\;, \forall y \in X$。**

这个命题有着非常好的几何解释：$-\nabla f$ 与 $y-x$ 成钝角
同时 **$\nabla f$ 定义了一个过点 $x$ 的对可行域的支撑超平面。**

验证 $x^*$ 是 $f_0(x)$ 的最优值，只需要再做一个优化问题 $ \min \nabla f_0 (x^*)^T (x - x^*)$ 即可。

如果问题仅包含等式约束 $Ax=b$，那么 $x$ 最优 $\Longleftrightarrow \nabla f\left(x\right)+A^{T} \mu=0, A x=b$。这个可以用之后介绍的KKT条件进行证明。

如果问题只是变量的非负约束，那么 $x$ 最优 $\Longleftrightarrow \nabla f\left(x\right)_{i} x_{i}=0, x \geq 0, \nabla f\left(x\right) \geq 0$

如果凸优化问题没有约束条件（Unconstrained problems），那么上面的命题，归结为一个广为人知的充分条件：

$$
\nabla f_0(x)=0
$$

### 常见的凸问题

很多实际问题都可以归结于或者转化为几类经典的凸优化问题。包括**线性规划（LP）、二次规划（QP）、二次约束二次规划（QCQP）、二阶锥规划（SOCP）、几何规划（GP）**，接下来依次介绍它们。

#### 线性规划（Linear Program）

线性规划应该是最简单、人们最熟悉的一种凸优化问题了。线性规划问题具有如下的典型形式：

$$
\begin{array}{ll}
\operatorname{minimize} & c^{T} x+d \\
\text {subject to } & G x \preceq h \\
& A x=b
\end{array}
$$

通过一些变换，如添加松弛变量，引入正部、负部等方法，可以化为**标准形式**：

$$
\begin{array}{cl}
\operatorname{minimize} & c^{T} x \\
\;\text { subject to } & A x=b \\
& x \succeq 0
\end{array}
$$

对于标准形式的线性规划问题，本科的运筹学课程应当会介绍**单纯形法**。这是根据线性规划可行域的特点提出的一种求解方法，因为线性规划的最优值如果存在那么必然取在可行域的极点上。

> 线性规划的单纯形法并不是一个最坏时间复杂度在多项式级别的算法，在历史上椭球法第一次证明了线性规划的存在时间复杂度为多项式级别，单纯形法只是在**平均时间复杂度**上具有优势。

有几类问题可以转化为LP问题。

###### 多面体的 Chebyshev 中心

给定一个多面体

$$
\mathcal{P}=\left\{x \in \mathbf{R}^{n} | a_{i}^{T} x \leq b_{i}, i=1, \dots, m\right\}
$$

我们想知道这个多面体能包含的最大球的半径和球心。这个球心我们叫做该多面体的 chebyshev 中心。

我们假设这个球是 $\mathcal{B}=\{x_c+u|\; \lVert u\rVert_2 \leq r\}$，如果这个球在半平面 $a_i^T x\leq b_i$ 内，那么一定有：

$$
\sup_{\lVert u\rVert_2\leq r} a_i^T (x_c+u)=a_i^T x_c + r\lVert a_i\rVert_2\leq b_i
$$

最后我们得到相应的LP问题：

$$
\begin{array}{ll}
\text { maximize } & r \\
\text { subject to } & a_{i}^{T} x_{c}+r\left\|a_{i}\right\|_{2} \leq b_{i}, \quad i=1, \ldots, m
\end{array}
$$

$\vec{x_c}， r$ 是LP问题的变量。

##### Linear-fractional programming

如果线性规划的目标函数不是线性函数，而是一个线性分式函数，这个问题就成了线性分式规划。它也可以转化成线性规划。

$$
f_{0}(x)=\frac{c^{T} x+d}{e^{T} x+f}, \quad \operatorname{dom} f_{0}=\left\{x | e^{T} x+f>0\right\}
$$

先做一个换元：

$$
y=\frac{x}{e^{T} x+f}, \quad z=\frac{1}{e^{T} x+f}>0,\quad x=y/z
$$

将上式代入约束条件，就顺利转化成线性规划了。

#### 二次规划（QP）和 二次约束二次规划（QCQP）

当LP中的目标函数是一个二次函数的时候，这个问题就成了**二次规划（quadratic program）**。注意这个时候，约束条件仍然要求是线性的。
如果不等式约束条件中的函数再变成二次函数，那么这就是**二次约束二次规划（quadratically constrained quadratic program ）**。
它们分别具有标准形式：

$$
\begin{array}{ll}
\operatorname{minimize} & (1 / 2) x^{T} P x+q^{T} x+r \\
\text {subject to } & G x \preceq h \\
& A x=b
\end{array}
$$

和：

$$
\begin{array}{ll}
\operatorname{minimize} & (1 / 2) x^{T} P_{0} x+q_{0}^{T} x+r_{0} \\
\text {subject to } & (1 / 2) x^{T} P_{i} x+q_{i}^{T} x+r_{i} \leq 0, \quad i=1, \ldots, m \\
& A x=b
\end{array}
$$

需要注意，这样的二次规划问题，都需要矩阵$P\in S_+^n$至少是半正定的。

有一些问题可以利用QP进行求解：

###### 最小二乘法系数的确定

$$
\min_{x} \;\|A x-b\|_{2}^{2}=x^{T} A^{T} A x-2 b^{T} A x+b^{T} b
$$

$A^TA$ 一定是半正定的。这是一个无约束的QP问题。

##### 两个多面体之间的距离

两个多面体 $\mathcal{P}_{1}=\left\{x | A_{1} x \preceq b_{1}\right\}$ 和$\mathcal{P}_{2}=\left\{x | A_{1} x \preceq b_{2}\right\}$，想要找到它们之间的最小距离

$$
\begin{array}{ll}
\operatorname{minimize} & \left\|x_{1}-x_{2}\right\|_{2}^{2} \\
\text {subject to } & A_{1} x_{1} \preceq b_{1}, \quad A_{2} x_{2} \preceq b_{2},
\end{array}
$$
这也是一个QP问题。

##### Markowitz 投资组合

这也是一个经典的QP问题，在此从略。

#### 二阶锥规划（SOCP）

**二阶锥规划（second-order cone program）** 具有典型形式：

$$
\begin{array}{ll}
\operatorname{minimize} & f^{T} x \\
\text {subject to } & \left\|A_{i} x+b_{i}\right\|_{2} \leq c_{i}^{T} x+d_{i}, \quad i=1, \ldots, m \\
& F x=g
\end{array}
$$

乍一看，不等式约束两边同时平方一下，就能变成QCQP了。确实如此，SOCP可以看做是QCQP的推广。

椭球不确定集上的鲁棒线性优化，和高斯分布的线性机会约束，最后都转化成了一个SOCP。

##### 几何规划（GP）

**几何规划（geometric program）**是一类**可以转化成凸优化问题**的非凸问题。在引入GP之前，我们还需要厘清一些概念。我们称$$f(x)=cx^{\alpha_1}x^{\alpha_2}\cdots x^{\alpha_n}, x\succeq 0, c>0$$是一个单项式（monomial），几个单项式的和，叫做正项式（posynomial）。

> 尽管我的初中课本把若干个单项式的和叫做多项式，但是一般来说多项式特制未知数的指数是非负整数的情况，而且多项式的英文是 polynomial。

一个标准的GP问题具有如下形式：

$$
\begin{array}{ll}
\operatorname{minimize} & f_{0}(x) \\
\text {subject to } & f_{i}(x) \leq 1, \quad i=1, \ldots, m \\
& h_{i}(x)=1, \quad i=1, \ldots, p
\end{array}
$$

其中 $f_i, h_i$ 都定义在 $x\succeq 0$ 上。很显然，单项式并不一定是凸的，这并不是一个凸优化问题。作换元 $y_i=\log x_i, x_i=e^{y_i}$，对于新元 $y$，原问题具有如下形式：

$$
\begin{aligned}
\operatorname{ minimize} & \sum_{k=1}^{K_{0}} e^{a_{0 k}^{T} y+b_{0 k}} \\
\text { subject to } & \sum_{k=1}^{K_{i}} e^{a_{i k} y+b_{i k}} \leq 1, \quad i=1, \ldots, m \\
& e^{g_{i}^{T} y+h_{i}}=1, \quad i=1, \ldots, p
\end{aligned}
$$

如果GP的目标函数和不等式约束都是单项式的话，我们还可以通过换元将它变成LP。所以LP也可以看做是GP的一种特殊情况。

### 广义不等式下的凸优化问题

在前一章凸函数的末尾，我们通过广义不等式成功将凸函数推广到向量值函数。我们称：

$$
\begin{array}{ll}
\operatorname{minimize} & f_{0}(x) \\
\text {subject to } & f_{i}(x) \preceq_{K_{i}} 0, \quad i=1, \ldots, m \\
& A x=b
\end{array}
$$

为广义不等式约束下的凸优化问题的标准形式。正如一般凸优化问题的要求，这里还要求 $f_i$ 在 $K_i$ 上是 $K-convex$ 的。

数学的美，在于它能用精妙的理论，将许多看似没有关联的问题抽象地统一在一起。正如我们即将看到的，proper cone 的概念仿佛神来之笔，将整个优化理论的问题统一起来了。

#### Conic form problems

锥形式的优化问题是一种很 general 的情况。在数学里面，我们认为一般性的结论是要好于特殊性的结论的。锥规划就是把很多经典的优化问题的形式抽象出来的一种表示方法。

锥规划一般都具有如下的典型形式：

$$
\begin{array}{ll}
\operatorname{minimize} & c^{T} x \\
\text {subject to } & F x+g \preceq_{K} 0 \\
& A x=b
\end{array}
$$

线性规划显然是锥规划的一种特殊情况。

###### SOCP

SOCP可以用锥规划的形式表示：

$$
\begin{array}{ll}
\operatorname{minimize} & c^{T} x \\
\text {subject to } & -\left(A_{i} x+b_{i}, c_{i}^{T} x+d_{i}\right) \preceq_{K_{i}} 0, \quad i=1, \ldots, m \\
& F x=g
\end{array}
$$

其中 $K_i$ 是一个二阶锥：$K_{i}=\left\{(y, t) \in \mathbf{R}^{k_{i}+1} \mid\|y\|_{2} \leq t\right\}$。

###### 半定规划（semidefinite programming）

半定规划（SDP）是一类非常非常重要的凸优化问题！在 Conic form problems 的基础上，令$K=\mathrm{S}^n_+$为半正定矩阵锥，因为 $\operatorname{tr}(C X)=\sum_{i, j=1}^{n} C_{i j} X_{i j}$，可以将 $\operatorname{tr}(C X)$ 看做 $X\in \mathrm{S}^n$ 的线性函数。继而，我们有

$$
\begin{array}{ll}
\operatorname{minimize} & \operatorname{tr}(C X) \\
\text {subject to } & \operatorname{tr}\left(A_{i} X\right)=b_{i}, \quad i=1, \ldots, p \\
& X \succeq 0
\end{array}
$$

这称为SDP的**标准形式**。SDP也有如下的形式：

$$
\begin{array}{ll}
\operatorname{minimize} & c^{T} x \\
\text {subject to } & x_{1} F_{1}+\cdots+x_{n} F_{n}+G \preceq 0 \\
& A x=b
\end{array}
$$

关于矩阵的线性不等式我们叫做 **linear matrix inequality**，在很多文献上简写为 **LMI**。

> 二阶锥规划和半定规划都属于锥线性规划，其标准形式和典型形式的联系见：[Conic Linear Programming](https://www.jianshu.com/p/172a08ca86dd)

---

广义不等式不仅可以作用在约束条件上，还能作用在目标函数上。令 $f_0: \mathrm{R}^n \to \mathrm{R}^p$ 是一个多元向量值函数，在 $\mathrm{R}^n$的一个凸集上$C$，我们希望找到在一个广义不等式下的 $C$ 的最小值/极小值。

$$
\begin{array}{ll}
\operatorname{minimize}(\text { with respect to } K) & f_{0}(x) \\
\text {subject to } & f_{i}(x) \leq 0, \quad i=1, \ldots, m \\
& h_{i}(x)=0, \quad i=1, \ldots, p
\end{array}
$$

这样的问题叫做向量优化问题。这样子的目的就在于，如果目标是多维的，可以通过定义一个 proper cone $K$，来表达 $f_0(x) \preceq f_0(y)$，$x$ 至少不比 $y$ 差。


