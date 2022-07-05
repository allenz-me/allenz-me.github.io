---
title: "Lecture 4.5: n-step Bootstrapping"
date: 2022-02-12
draft: false
toc: false
slug: lecture4-cont
categories: ["算法与程序设计", "cs234"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---



### $n$-step TD Prediction

The idea of $n$-step TD

<img src="../../figures/lecture4.5/image-20220212161120843.png" alt="image-20220212161120843" style="zoom:67%;" />



Monte Carlo target
$$
G\_{t} \\doteq R\_{t\+1}\+\\gamma R\_{t\+2}\+\\gamma^{2} R\_{t\+3}\+\\cdots\+\\gamma^{T\-t\-1} R\_{T}
$$


1-step TD target
$$
G\_{t: t\+1} \\doteq R\_{t\+1}\+\\gamma V\_{t}\\left(S\_{t\+1}\\right)
$$
2-step TD target
$$
G\_{t: t\+2} \\doteq R\_{t\+1}\+\\gamma R\_{t\+2}\+\\gamma^{2} V\_{t\+1}\\left(S\_{t\+2}\\right)
$$
n-step TD target
$$
G\_{t: t\+n} \\doteq R\_{t\+1}\+\\gamma R\_{t\+2}\+\\cdots\+\\gamma^{n\-1} R\_{t\+n}\+\\gamma^{n} V\_{t\+n\-1}\\left(S\_{t\+n}\\right)
$$
State-value learning algorithm for using n-step returns is
$$
V\_{t\+n}\\left(S\_{t}\\right) \\doteq V\_{t\+n\-1}\\left(S\_{t}\\right)\+\\alpha\\left[G\_{t: t\+n}\-V\_{t\+n\-1}\\left(S\_{t}\\right)\\right], \\quad 0 \\leq t<T
$$


<img src="../../figures/lecture4.5/image-20220212162104250.png" alt="image-20220212162104250" style="zoom:67%;" />



The n-step TD methods thus form a family of sound methods, with one-step TD methods and Monte Carlo methods as extreme members.



### $n$-step Sarsa


$$
G\_{t: t\+n} \\doteq R\_{t\+1}\+\\gamma R\_{t\+2}\+\\cdots\+\\gamma^{n\-1} R\_{t\+n}\+\\gamma^{n} Q\_{t\+n\-1}\\left(S\_{t\+n}, A\_{t\+n}\\right), n \\geq 1,0 \\leq t<T\-n
$$

$$
Q\_{t\+n}\\left(S\_{t}, A\_{t}\\right) \\doteq Q\_{t\+n\-1}\\left(S\_{t}, A\_{t}\\right)\+\\alpha\\left[G\_{t: t\+n}\-Q\_{t\+n\-1}\\left(S\_{t}, A\_{t}\\right)\\right], \\quad 0 \\leq t<T
$$




### $n$-step Off-policy Learning







### $n$-step Tree Backup Algorithm



