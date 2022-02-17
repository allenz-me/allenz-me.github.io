---
title: "Multi-armed Bandits (1)"
date: 2022-02-15
draft: false
slug: none
categories: ["运筹与优化", "MAB"]
tags: ["MAB"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

多臂老虎机问题（multi-armed bandits）是一类重要的在线学习问题。

## 问题简述

带有不确定性的序贯决策问题：有 $N$ 种行为，每次选择一种，收到回报（reward）；目标是最大化 $T$ 轮的总回报。
    
根据历史回报选择下一步行为的方法称为算法。

**应用场景：**
+ 在线广告投放：每次推荐给用户一个广告，用户点击则收到回报。
+ 商品推荐：每次推荐给用户一件商品，用户点击或购买则收到回报。
+ 资产投资：对多类资产进行配置，赚取收益。

**问题分类：**

根据 Feedback：
+ bandit feedback: 做出选择之后只能得到该行为回报的信息。
+ partial feedback. 做出选择之后能得到该行为回报的信息，和其它行为回报的部分信息。
+ full feedback. 做出选择之后能得到全部行为的信息。


根据 Rewards:
+ IID rewards: 不同行为的回报相互独立且服从一个固定的概率分布。
+ Adversarial rewards: 对手可以随意更改回报。
+ Constrained adversary: 对手每轮只能有限制地更改回报。
+ Stochastic rewards: 回报服从一个随机过程。比如，两个行为的回报服从一个二维的布朗运动。

The simplest setting: bandit feedback + IID rewards.

