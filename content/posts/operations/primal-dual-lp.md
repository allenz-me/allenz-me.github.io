---
title: "线性规划的原始对偶算法"
date: 2022-03-19
draft: false
slug: primal-dual-lp
toc: false
categories: ["运筹与优化", "整数和组合优化"]
tags: ["线性规划"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


线性规划的原始-对偶方法 (primal-dual method) 是设计组合优化问题算法的标准工具，它由 Dantzig、Ford 和 Fulkerson 提出，是一种多项式时间的算法。

PD方法的思路是从一个对偶可行解出发，逐步找到满足互补松弛条件的一组解。
$$
(\mathbf{P})\left\{\begin{array} { l l } 
{ \underset { \mathbf { x } \in \mathbb { R } ^ { n } } {\operatorname {minimize}} } & { \mathbf { c } ^ { \top } \mathbf { x } } \\
{ \text {subject to} } & { A \mathbf { x } = \mathbf { b } } \geq \mathbf{0} \\
{ } & { \mathbf { x } \geq \mathbf { 0 } }
\end{array} \qquad ( \mathbf { D } ) \left\{\begin{array}{ll}
\underset{\mathbf{u} \in \mathbb{R}^{m}}{\operatorname{maximize}} & \mathbf{u}^{\top} \mathbf{b} \\
\text {subject to} & \mathbf{u}^{\top} A \leq \mathbf{c}^{\top} \\
& \mathbf{u} \text { unrestricted }
\end{array}\right.\right.
$$
给定如上的原问题和对偶问题，$\mathbf{b} \geq \mathbf{0}$ 是一个 WLOG 但是有意义的条件。

线性规划的 complementary slackness 给出了可行解 $(\bar{\mathbf{x}}, \bar{\mathbf{u}})$ 是一组最优解的充要条件：

$$
\begin{align}
\bar{\mathbf{u}}^\top (A\bar{\mathbf{x}} - \mathbf{b}) = 0  \tag{1} \\
(\mathbf{A}^\top \bar{\mathbf{u}} - \mathbf{c})^\top \bar{\mathbf{x}} = 0 \tag{2}
\end{align}
$$

(1)式由解的可行性自动满足，(2)式能够揭示 primal-dual 方法的一个思想：**对于一个对偶可行解，找到一个满足互补松弛条件、最接近可行的原始解**；如果能找到一个满足互补松弛条件的、可行的原始解，说明这两组解都是最优的。

以下阐述 primal-dual 方法的思路和步骤。

首先，从一个对偶可行解 $\mathbf{u}$ 出发，我们希望找到一个方向 $\mathbf{v}$，使得从 $\mathbf{u}$ 出发沿着 $\mathbf{v}$ 方向前进一定距离，目标函数值 $\mathbf{u}^T \mathbf{b}$ 能得到提升。

记指标集 $J = \{j : \mathbf{u}^\top A_j = c_j\}$ 表示紧的约束，用 $J^C$ 表示不紧的约束。

对于 $J$ 对应的约束，方向 $\mathbf{v}$ 必须满足 $\mathbf{v}^\top A_J \leq \mathbf{0}^\top$，这样才能保证存在 $t > 0$ 使得 $\mathbf{u} + t \mathbf{v}$ 依然是对偶可行的；对于其它约束，则并没有这样的限制。当然，必须谨记我们要找的是一个方向，此时 $\mathbf{v}$ 或者 $2 \mathbf{v}$ 都可以是我们的要的解，所以我们需要 normalize 一下。非线性规划里面，我们可以选择 $\| \mathbf{v} \|_2 \leq 1$ 作为 normalization constraint，但是在线性规划里面，选择 $\| \mathbf{v} \|_\infty \leq 1 \Rightarrow v_i \leq 1$ 是一个更好的选择！

由此我们得到寻找方向 $\mathbf{v}$ 的线性规划问题：
$$
\begin{array}{ll}
{\operatorname{maximize}} & \mathbf{v}^{\top} \mathbf{b} \\
\text {subject to } & \mathbf{v}^{\top} A_{J} \leq \mathbf{0}^{\top} \\
& v_{1}, \ldots, v_{m} \leq 1
\end{array} \tag{DRP}
$$
从这里可以看出 $\mathbf{b} \geq \mathbf{0}$ 的意义，normalization constraint $v_i \leq 1$ 是为了防止 $\mathbf{v}$ 无限增大，而那些小于0的 $v_i$ 趋于负无穷并不会增加目标函数值，所以没有必要添加相应的约束了。

这个问题我们把它叫做 dual restricted program (DRP)

+ 如果 DRP 的最优值是0，这意味着对偶问题(D)达到最优，因为沿着任何可行方向都不能增加目标函数值了。
+ 如果 DRP 的最优值大于0，这说明存在一个足够小的 $t>0$，使得 $\mathbf{u}$ 沿着 DRP 的解 $\mathbf{v}$ 前进一段距离能保持对偶可行性同时提升函数值！现在我们要找到最大的 $t$，$\mathbf{u} + t \mathbf{v}$ 必须要保证可行性，对于 指标集 $J$ 对应的约束，可行性是一定满足的。
  + 如果 $\mathbf{v}^\top A_j \leq 0 , \; \forall j \notin J$ ，那么 $\mathbf{u}$ 沿着 $\mathbf{v}$ 前进多少都不会违背可行性，这说明对偶问题(D)是无上界的，从而原问题没有可行解。
  + 如果 $\exists j \notin J, \;\mathbf{v}^\top A_j > 0$，那么可以选择的最大的 $t$ 是 $\min\limits_{j \notin J,\, \mathbf{v}^\top A_j > 0} \displaystyle\frac{c_j - \mathbf{u}^\top A_j}{\mathbf{v}^\top A_j}$



这样，我们可以更新对偶可行解 $\mathbf{u}_{\text{new}} = \mathbf{u} + t \mathbf{v}$ ，这就是一步迭代。

继续这么做，就能不断逼近最优解。**但是**，这么做是很费力的，因为要不断地解一个新的线性规划。

注意到(DRP)的对偶问题是：
$$
\begin{array}{ll}
\underset{\mathbf{x} \in \mathbb{R}^{n}, \mathbf{y} \in \mathbb{R}^{m}}{\operatorname{minimize}} & y_{1}+\cdots+y_{m} \\
\text {subject to } & A_{J} \mathbf{x}_J+\mathbf{I}\mathbf{y}=\mathbf{b} \\
& \mathbf{x}, \mathbf{y} \geq \mathbf{0}
\end{array} \tag{RP}
$$
我们把它称作是 restricted primal (RP)，它暗含了 $\mathbf{x}_{J^C} = \mathbf{0}$. (RP) 输出一个满足互补松弛条件、并把不可行性降到最低的 $\mathbf{x}$ .

(RP) 可以用单纯型法高效地求解，同时因为单纯型法的优点，我们同时还能得到 (DRP) 的解。

乍一看，求解 (RP) 跟求解 DRP 的计算量差不多啊，但是，**原始对偶算法的精髓就在于，在每一次迭代，都可以由前一次迭代得到的最优解开始求解 (RP)**，

令 $\mathcal{B}$ 是 (RP) 一步迭代中的最优基，$\mathcal{B}\subseteq J \cup [m]$，则 $\mathcal{B}\cap J \subseteq J_{\text{new}}$. 这意味着如果 $j \in \mathcal{B} \cap J$，那么 $j \subseteq J_{\text{new}}$. （证明是容易的，这里省略了）

在前一次迭代中非零的 $x, y$ ，可以直接放在下一次迭代的单纯型表中！如果我们用的是 revised simplex，那么直接拿之前的 $B^{-1}$ 作为下次迭代的 $B^{-1}$，**这就节省了大量的计算**！

> 值得一提的是根据单纯型法的理论，原问题最优解 $B^{-1} b$，对偶问题最优解 $c_B^T B^{-1}$，最优值 $c_B^T B^{-1}b$ .

让我们来总结一下 PD 算法的步骤：

1. 找到一个对偶可行解 $\mathbf{u}$，确定指标集 $J = \{j : \mathbf{u}^\top A_j = c_j\}$
2. 用单纯型法求解 RP，得到 RP 的最优基变量、最优解、最优值和 DRP 的最优解 $\mathbf{v}$
3. 如果 step2 的最优值等于0，说明达到最优，输出 RP 的最优解和对偶可行解 $\mathbf{u}$；如果 step2 的最优值大于0：
  + 如果 $\mathbf{v}^\top A_j \leq 0 , \; \forall j \notin J$ ，那么原问题没有可行解
  + 如果 $\exists j \notin J, \;\mathbf{v}^\top A_j > 0$，计算 $t=\min\limits_{j \notin J,\, \mathbf{v}^\top A_j > 0} \displaystyle\frac{c_j - \mathbf{u}^\top A_j}{\mathbf{v}^\top A_j}$，重新确定指标集 $J$，回到 step2，复用之前的最优基变量和最优解进行单纯型迭代。

---

最后，简单说明一下算法的有限终止性。假定问题是有解并且是非退化的 (nondegenerate)

假设第三步中 $j_0=\underset{{j \notin J,\, v_j^\top A > 0}}{\operatorname{argmin}}  \displaystyle\frac{c_j - u_j^\top A}{v_j^\top A}$，注意到 $j_0 \notin J$ 但是 $j_0 \in J_{\text{new}}$，在将要开始的 RP 的单纯型迭代中，$x_{j_0}$ 的 reduced cost 是 $\bar{c}_{j_0} = 0 - \mathbf{v}^\top A_{j_0} < 0$，这说明下一步迭代 RP 能有严格的提升(也就是说函数值会严格下降)，因为多面体的 extreme point 的个数是有限的，**我们至多解有限次RP（子问题）**，因此算法必然在有限步终止。

