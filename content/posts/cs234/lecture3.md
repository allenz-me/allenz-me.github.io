---
title: "Lecture 3: Model-Free Policy Evaluation: Policy Evaluation Without Knowing How the World Works"
date: 2022-02-04
draft: false
toc: false
slug: lecture3
categories: ["算法与程序设计", "cs234"]
tags: [""]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


Lecture3 主要介绍当我们不知道模型的各个参数的时候，如何评价一个 policy.


### Recall


+ Deﬁnition of Return
+ Deﬁnition of State Value Function
+ Deﬁnition of State-Action Value Function

Dynamic programming for policy evaluation

$$
V^{\pi}(s) \leftarrow \mathbb{E}_{\pi}\left[r_{t}+\gamma V_{k-1} \mid s_{t}=s\right]
$$

<img src="../figures/lecture3/bts.png" alt="" style="zoom: 50%;" />





## Policy Evaluation without a Model



### Monte Carlo Policy Evaluation



- If trajectories are all finite, sample set of trajectories \& average returns
- Does not require MDP dynamics/rewards
- No bootstrapping
- Does not assume state is Markov (handles non-Markovian domains)
- Can only be applied to episodic MDPs
- Averaging over returns from a complete episode
- Requires each episode to terminate

MC 方法适用于可以对轨道进行采样的MDP。



#### First-Visit





Unbiased

Consistent



#### Every-Visit



Biased

Consistent

Better MSE





#### Incremental Monte Carlo


$$
V^{\pi}(s)=V^{\pi}(s)+\alpha\left(G_{i, t}-V^{\pi}(s)\right)
$$




Monte Carlo (MC) Policy Evaluation Key Limitations



+ Generally high variance estimator
  + Reducing variance can require a lot of data
+ Requires episodic settings
  + Episode must end before data from that episode can be used to update the value function





### Temporal Difference Learning

> “If one had to identify one idea as central and novel to reinforcement learning, it would undoubtedly be temporal-difference (TD) learning.”   – Sutton and Barto 2017




$$
V^{\pi}(s)=V^{\pi}(s)+\alpha\left(G_{i, t}-V^{\pi}(s)\right)
$$
Replace $G_{i,t}$ by bootstraping $r_t + \gamma V^\pi(s_{t+1})$ .
$$
V^{\pi}\left(s_{t}\right)=V^{\pi}\left(s_{t}\right)+\alpha(\underbrace{\left[r_{t}+\gamma V^{\pi}\left(s_{t+1}\right)\right]}_{\text {TD target }}-V^{\pi}\left(s_{t}\right))
$$

+ TD error
  $$
  \delta_{t}=r_{t}+\gamma V^{\pi}\left(s_{t+1}\right)-V^{\pi}\left(s_{t}\right)
  $$

+ Can immediately update value estimate after $\left(s, a, r, s^{\prime}\right)$ tuple

+ Don't need episodic setting

+ Biased, but generally less high variance than MC

+ TD(0) converges to true value with tabular representation

+ TD(0) does not always converge with function approximation







TD(0) converges to DP policy $V^\pi$ for the MDP with the maximum likelihood model estimates



> Maximum likelihood Markov decision process model
> $$
\begin{gathered}
 \hat{P}\left(s^{\prime} \mid s, a\right)=\frac{1}{N(s, a)} \sum_{k=1}^{K} \sum_{t=1}^{L_{k}-1} \mathbb{1}\left(s_{k, t}=s, a_{k, t}=a, s_{k, t+1}=s^{\prime}\right) \\
 \hat{r}(s, a)=\frac{1}{N(s, a)} \sum_{k=1}^{K} \sum_{t=1}^{L_{k}-1} \mathbb{1}\left(s_{k, t}=s, a_{k, t}=a\right) r_{t, k}
\end{gathered}
> $$

TD exploits Markov structure.



