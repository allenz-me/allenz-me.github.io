---
title: "Java 流的妙用"
date: 2019-11-15
draft: false
slug: java-stream
categories: ["算法与程序设计"]
tags: ["Java"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


1. 求数组的最大值、最小值、和... 等

在Java中，基本类型流只支持 `int、long、double` 三种类型。一是可以通过 `IntSream.range` 方法创建；二是通过 `Arrays.stream( )` 中传入一个基本类型的数组进行创建

```java
int[] nums = {1, 2, 3};
int max = Arrays.stream(nums).max().getAsInt();
int sum = Arrays.stream(nums).sum();
// 类似于python的reduce函数，提供一个二元运算符
int reduce = Arrays.stream(nums).reduce(1, (x, y) -> x * y);  // 6，所有数之积
int orelse = Arrays.stream(nums).reduce((x, y) -> x * y).orElse(0);
```

`Arrays.stream(nums).max()` 返回的是一个 `Optinal<int>` 对象，因为流可能是空的，所以 `getAsInt` 方法可能会报错，因此 `Optinal<int>` 对象提供了一个 `orElse(int default)` 方法去处理这种情况。类似于 Python 的 `max(nums, default=0)`。而流是空的时候 `sum` 方法不会出现问题。

**如果 `Optional` 装载的泛型类不是基本类型，那么就通过 `get` 方法去获得变量的值。**

2. 列表筛选

```java
List<String> ss = new ArrayList<String>(Arrays.asList("ab", "bb"));
ss = ss.stream().filter(s -> s.startsWith("a")).collect(Collectors.toList());
List<Boolean> tt = ss.stream().map(String::isEmpty).collect(Collectors.toList());
ist<Integer> ll = ss.stream().map(String::length).collect(Collectors.toList());
// collect() 方法接受stream数据并转换类型
```