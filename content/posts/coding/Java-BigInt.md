---
title: "Java BigInteger"
date: 2019-10-26
draft: false
slug: java-bigint
categories: ["算法与程序设计"]
tags: ["Java"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

在 C++ 中，没有超过 `long long` 以上的大整数类了，而 Java 就有大整数类

普通的 `int` 类型能表示的整数的绝对值上限是$2^{31} \simeq 10^{(\log_{10}2) \times 31} \simeq 10^{0.3 \times 31}$，其数量级在$10^{9}$

`long` 类型是 $2^{63} \simeq 10^{0.3\times 63}$，数量级不超过 $10^{19}$

> 比如对于Fibonacci数列，其增长速度是 $(\frac{1+\sqrt 5}{2})^n \simeq 1.618^n$，在 $n\ge \frac{19}{\log_{10}{1.618}}\simeq 91$ 时是无法用 `long` 类型来保存的

由此可见，学习 Java 的大整数类 `java.math.BigInteger` 是非常有必要的！

```java
import java.util.BigInteger;
import java.util.Scanner;

public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    BigInteger bi = in.nextBigInteger();
    BigInteger v0 = BigInteger.valueOf(0);
    BigInteger v1 = BigInteger("2");
    // 主要就是这两种构造方法，推荐使用字符串构造
}

// 下面是一些BigInteger的常用方法
BigInteger abs()  返回大整数的绝对值
BigInteger add(BigInteger val) 返回两个大整数的和
BigInteger and(BigInteger val)  返回两个大整数的按位与的结果
BigInteger andNot(BigInteger val) 返回两个大整数与非的结果
BigInteger divide(BigInteger val)  返回两个大整数的商
double doubleValue()   返回大整数的double类型的值
float floatValue()   返回大整数的float类型的值
BigInteger gcd(BigInteger val)  返回大整数的最大公约数
int intValue() 返回大整数的整型值
long longValue() 返回大整数的long型值
BigInteger max(BigInteger val) 返回两个大整数的最大者
BigInteger min(BigInteger val) 返回两个大整数的最小者
BigInteger mod(BigInteger val) 用当前大整数对val求模
BigInteger multiply(BigInteger val) 返回两个大整数的积
BigInteger negate() 返回当前大整数的相反数
BigInteger not() 返回当前大整数的非
BigInteger or(BigInteger val) 返回两个大整数的按位或
BigInteger pow(int exponent) 返回当前大整数的exponent次方
BigInteger remainder(BigInteger val) 返回当前大整数除以val的余数
BigInteger leftShift(int n) 将当前大整数左移n位后返回
BigInteger rightShift(int n) 将当前大整数右移n位后返回
BigInteger subtract(BigInteger val)返回两个大整数相减的结果
byte[] toByteArray(BigInteger val)将大整数转换成二进制反码保存在byte数组中
String toString() 将当前大整数转换成十进制的字符串形式
BigInteger xor(BigInteger val) 返回两个大整数的异或
```
