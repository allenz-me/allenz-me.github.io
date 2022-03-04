---


title: "离散选择模型 Discrete Choice Models"
date: 2022-02-15
draft: false
slug: discrete-choice-models
categories: ["运筹与优化"]
tags: ["Choice Model"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

参考文献：Discrete Choice Models and Applications in Operations Management. In INFORMS TutORials in Operations Research. https://doi.org/10.1287/educ.2021.0229


## Discrete Choice Models

离散选择模型关注决策者如何在多个备选方案中做出选择，已成为研究消费者面对多种产品的购买行为的重要工具，并已广泛应用于经济、营销、交通和运营等多个领域。

### Luce Model

记 $q_i(S)$ 为选择 item $i \in S$ 的概率

**Regularity Condition**

the choice probability for any product in the offer set decreases as the offer set enlarges.

**choice axiom**
$$
q_i(S) = q_{S^\prime}(S) \cdot q_i (S^\prime) \quad \forall i \in S^\prime \subseteq S
$$
选择公理把选择一件商品分成了两步。


Luce 证明了满足 choice axiom 的 $q$ 一定有如下形式：

$$
q_{i}(S)= \frac{a_{i}}{\sum_{j \in S} a_{j}}
$$

上式也满足正则性条件。

### RUM framework

Random Utility Maximization Framework 假设顾客会选择效用最高的商品，效用是随机的：

$$
U_i = u_i + \xi_i
$$

其中 $u_i$ 是常数，$\xi_i$ 是 i.i.d. 参数为 $\mu$ 的 Gumbel 随机变量。

> $F_{\xi_i}(x)=\mathrm{P}\left(\xi_{i} \leq x\right)=\exp (-\exp (-(x / \mu+\gamma)))$，其中 $\gamma$ 是欧拉常数。

这时候就有：

$$
q_{i}(S)=\operatorname{Pr}\left(U_{i} \geq U_{j}, \forall j \in S, j \neq i\right), \text { for any } i \in S
$$

在这样一套理论框架下，Holman and Marley 给出了 multinominal logit 模型

$$
q_{i}(S)=\frac{\exp \left(u_{i} / \mu\right)}{\sum_{j \in S} \exp \left(u_{j} / \mu\right)}, \text { for any } i \in S
$$

容易看出 MNL 模型和 Luce 模型的等价性。

MNL/Luce 模型有一个局限性，那就是不能描述具有相关性商品的选择概率。问题就出现在它满足 IIA 这个性质。

> **IIA: independence of irrelevant alternatives.**
>
> The basic idea of IIA is that the ratio of any two products' shares should be independent of all other products.
>
> **“red bus/blue bus” paradox**
> 
>  {red bus, car} vs {red bus, blue bus, car}
> 
> 假设市场上有 cars 和 red buses 两种商品，各占50%市场份额，现在增加 blue buses 这种商品，它的效用跟 red buses 是一样的，MNL 模型会把 cars 的份额调低成 33%，但这很明显是不符合实际的。


**Substitution Effect**

The choice probability decreases as any other alternative becomes more appealing

MNL 也满足 substitution effect.


### Nested Logit Model

NL 将商品的相关性加入到 MNL 中。



### MNL with Network Effects

一个人的购买行为会受到身边的人的影响，这其实构成了一个网络。



## Pricing Optimization

价格影响顾客选择商品的概率，假定效用关于价格是线性的：
$$
u_i = \alpha_i - \beta_i p_i
$$
并令 no-purchase option $a_0=1$，这时候的选择模型：
$$
q_{i}\left(S^{+}, \mathbf{p}\right)=\frac{\exp \left(\alpha_{i}-\beta_{i} p_{i}\right)}{1+\sum_{j \in S} \exp \left(\alpha_{j}-\beta_{j} p_{j}\right)}, \quad \forall i \in S,  \quad (S^+ = S \cup \{0\})\quad
$$
以最大化期望收益为目标，多产品定价优化问题可表示为：

$$
\max _{\mathbf{p}} R(S, \mathbf{p}):=\sum_{i \in S}\left(p_{i}-c_{i}\right) \cdot q_{i}\left(S^{+}, \mathbf{p}\right)
$$




## Assortment Optimization

另一种零售策略，如果商品的价格是给定的，商家只能调整展示给顾客的商品种类。

这时候的优化目标变为：
$$
\max _{S \subseteq N} R(S):=\sum_{i \in S}\left(p_{i}-c_{i}\right) \cdot q_{i}\left(S^{+}\right)
$$

**Revenue-Ordered Assortment**

假定商品索引按利润排序，即 $p_{1}-c_{1} \geq p_{2}-c_{2} \geq \cdots \geq p_{n}-c_{n}$，则 $S_i = \{1, 2, \dots, i\}, i = 1, \dots n$ 被称为 *revenue-ordered assortment*



对 MNL 模型来说，最优的 assortment 在 revenue-ordered assortments 中取到。时间复杂度是 $O(n)$。

### Constrained Assortment Optimization

当可以展示的商品数量是有限的的情况下，问题变成：
$$
\begin{array}{ll}
\max\limits_{S \subseteq N} & R(S):=\displaystyle\sum_{i \in S}\left(p_{i}-c_{i}\right) \cdot \frac{a_{i}}{1+\sum_{j \in S} a_{j}} \\
\text { s.t. } & |S| \leq C
\end{array}
$$





更进一步地，如果商品种类和价格都是可以变化的，这时商家面临 Joint Assortment and Price Optimization。





## Summary

总的来说，对于 discrete choice model 的研究主要分为以下两块：

1. 如何从数据中拟合出一个好的选择模型
2. 给定一类选择模型，如何设计高效的算法解决 pricing / assortment 等问题






> **The Red-Bus/Blue-Bus Problem**
>
> 
>
> While choice simulators have proven eminently useful for simulating buyer behavior, one of the most common simulation models (the Logit or Share of Preference model) has displayed a problematic result often described as the *Red-Bus/Blue-Bus problem*.  The underlying property leading to this problem is termed IIA, which is shorthand for "Independence from Irrelevant Alternatives."  The basic idea of IIA is that the ratio of any two products' shares should be independent of all other products. This sounds like a good thing, and at first, IIA was regarded as a beneficial property.
>
> 
>
> However, another way to say the same thing is that an improved product gains share from all other products in proportion to their original shares; and when a product loses share, it loses to others in proportion to their shares.  Stated that way, it is easy to see that IIA implies an unrealistically simple model.  In the real world, products compete unequally with one another and when an existing product is improved, it usually gains most from a subset of products with which it competes most directly.
>
> 
>
> Imagine a transportation market with two products, cars and red buses, each having a market share of 50%.  Suppose we add a second bus, colored blue.  An IIA simulator would predict that the blue bus would take share equally from the car and red bus, so that the total bus share would become 67%.  But it's clearly more reasonable to expect that the blue bus would take share mostly from the red bus, and that total bus share would remain close to 50%.
>
> 
>
> It is important to note that some degree of IIA is appropriate and useful within market simulations.  In many markets, there is some degree of randomness to buyer behavior.  It is not that people are irrational, but that buyers must balance the costs of making a utility maximizing decision against the costs of taking the time to make perfect decisions.  It is quite reasonable for rational buyers to make what on the surface may seem as haphazard decisions — especially for low-involvement purchases.  A similar or even duplicate offering could thus be expected to capture more share in the real world than a rational simulation model might suggest.
>
> 
>
> In general, market simulation models based on disaggregate models of preference (utilities estimated at the individual level) are less subject to IIA difficulties than aggregate models of preference (aggregate logit, as offered by our CBC System).  However, IIA issues are worse as more product alternatives are added to the market simulation.  
>
> 
>
> In addition to modeling respondent preferences at the individual level, there are market simulation methods (such as Randomized First Choice, First Choice, and Share of Preference with Top N setting) that help deal with IIA.  These are described in the next sections.
>
> https://sawtoothsoftware.com/help/lighthouse-studio/manual/hid_thered-bus.html



