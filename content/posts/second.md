---
title: "SECOND"
date: 2022-01-26T13:55:14+08:00
draft: false
slug: "om"
# mathjax: true
tags: ["线性规划", "运营管理"]
---

预测总是错的！

预测总在变化！

时间段越长，预测越不准确！

整体预测比局部预测更可靠！

信息越充分，预测越准确！

因此，要做短期、整体的预测，并且尽量获取更多的信息。

## 报童模型



### 存在供应量不确定性的报童模型



## 经济批量订货模型（EOQ）

Economic order quantity (EOQ) 的基本假设：

+ 需求确定，单位时间内的需求是 $\lambda $
+ 不允许缺货
+ 固定成本 $K$，单位采购成本 $c$，单位货物单位时间的存储成本 $h$

目标：最小化单位时间内的订货和库存成本。

> $Q$ 的最优值不取决于 $c$，因此在分析中忽略。

设每次采购数量 $Q$，则平均存货量是 $\displaystyle\frac{Q}{2}$，订货周期 $T=\displaystyle\frac{Q}{\lambda}$，则单位时间内总费用是：

$$
g(Q) = \frac{K\lambda}{Q} + \frac{hQ}{2}
$$

于是最佳订货批量$Q^{*}=\sqrt{\displaystyle\frac{2K\lambda}{h}}$，最优成本 $g(Q^{*}) = \sqrt{2K\lambda h}$，最优订货周期 $T^\*=\sqrt{\displaystyle\frac{2K}{h\lambda}}$。

灵敏度分析：

$$
\forall Q > 0, \quad \frac{g(Q)}{g\left(Q^{\*}\right)}=\frac{1}{2}\left(\frac{Q^{*}}{Q}+\frac{Q}{Q^{\*}}\right)
$$

这表明平均成本对 $Q$ 的灵敏度不高。取 $Q = 2 Q^\star$，有 $g(2Q^\star)=\displaystyle\frac{5}{4} g(Q^\star)$，也就是说，哪怕订货量是最优订货量的两倍，平均成本也只增加 $25\%$.



### 存在供应量不确定的EOQ模型







---




+ $p$：售价
+ $c$：成本
+ $s$：残值
+ $C_u = p-c, C_o = c-s$

## 一些常用的函数式

令随机变量 $D$ 表示需求，$\mu$ 为其均值，$F$ 为其分布函数，$q$ 表示订货量。记：

+ $S(q) = \mathrm{E} \min\{q, D\}$ 表示期望的销售量
+ $I(q) = \mathrm{E}\,(q - D)^+$  表示期望的剩余库存
+ $L(q) = \mathrm{E}\,(D-q)^+$ 表示期望的因订货不足而导致的销量损失

有下列关系式：

+ $I(q) = q - S(q)$
+ $S^\prime(q) = 1 - F(q) = \bar{F}(q)$
+ $L(q) = \mu - S(q)$



## 报童模型

利润：
$$
\pi(q) = p S(q) + sI(q) -c q = (p-s) S(q) - (c-s)q
$$
最优订货量满足：
$$
\frac{d \pi}{d q} = (p-s)(1-F(q)) - (c-s) = 0 \Rightarrow F(q) = \frac{p-c}{p-s}
$$





## 供应链协调

假设供应链上有一个供应商（manufacturer）和一个零售商（retailer）。加入批发价为 $w$.

零售商的利润函数是：

$$
\pi_{R}(x)=p E \min (D, x)-w x
$$

而如果我们把供应商和零售商看做是一个整体，供应链的利润函数是：

$$
\pi_S(x) = p E \min (D, x)-c x
$$

注意到，零售商的最优订货量会低于使整个供应链利润最大化的订货量。这个现象叫做双边际效应（double marginalization）。回购和收益分享是最经典的两个用于促进协调的供应链合同。

一般我们认为**供应链协调 当且仅当 去中心化的供应链总利润等于中心化的供应链总利润**。

> Coordination: decentralized control yields centralize profi level.



### 回购协议（buy-back）

现在假设供应商对零售商未售出的部分以价格 $b$ 进行回购，则零售商、供应商和整个供应链的利润为：
$$
\begin{aligned}
& \pi_R = p S(q) + bI(q) - wq = (p-b)S(q) - (w-b)q \\\\
& \pi_M = wq - bI(q) - cq = (w-b)q + bS(q) - cq \\\\
& \pi_S = pS(q) - cq
\end{aligned}
$$
对于零售商来说，它的最优订货量满足：
$$
\frac{d \pi_R}{dq} = 0 \Rightarrow F(q_R^\*) = \frac{p-w}{p-b}
$$
而对供应链来说，零售商最优的订货量满足：
$$
F(q_S^\*) = \frac{p-c}{p}
$$
如果要使供应链达到协调，即 $q_R^* = q_S^*$，必须满足：
$$
\frac{p-w}{p-b} = \frac{p-c}{p}
$$
引入参数 $\lambda \in [0, 1]$，使 $b = (1-\lambda)p, w = (1-\lambda)p+\lambda c$ 且上述等式成立。注意到这时候：
$$
\pi_R = \lambda \pi_S 
$$
即零售商的总利润等于整个供应链的总利润的某个比例，此时零售商有足够的动力使整个供应链的利润最大化！




### 利润分享（revenue-sharing）

零售商每卖出一件商品，给予供应商 $r$ 的利润分享。此时利润为：
$$
\begin{aligned}
& \pi_R = (p-r) S(q)  - wq \\\\
& \pi_M = (w-c)q + r S(q)  \\\\
& \pi_S = pS(q) - cq
\end{aligned}
$$



小结：可以发现，供应链想要达到协调，需要使每个成员的利润是供应链总利润的一个比例，这样每个成员才会有充足的动力最大化整个供应链的利润。

### 需求预测









## 应对需求风险

供应链上的企业做出生产、订购决定的时候，实际上并不完全清楚到时候的需求是什么样子的。

【补充叙述】


上图展示了两种应对需求风险的思路





## 牛鞭效应

牛鞭效应（bullship effect）指需求信息以订单的方式从零售端沿供应链的环节向上游传递时，产生的逐级放大的波动现象。

### 产生原因



demand forecasting

inventory rationing due to supply constraints

order batching

price ﬂuctuations

### 配给博弈

供给有限，多订



### 批量订货



### 价格投机



### 减小牛鞭效应



VMI（供应商管理库存）

信息共享








