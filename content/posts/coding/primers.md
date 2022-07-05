---
title: "给定自然数 N，如何快速分解质因数？"
date: 2019-10-27
draft: false
slug: primers
categories: ["算法与程序设计"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

> $120=2^3 \\times 3 \\times 5$

如上，对一个数分解质因数就是分解成若干个质数的乘积，如果这个数是质数，那么对它分解质因数就是这个数本身。

一个很朴素的想法是：

对于从 $2\\sim N$ 的每个自然数 $p$，去判断它是否是质数，如果 $p$ 整除 $N$，那么就可以求出 $p$ 在 $N$ 的质因数分解式里的指数

一个非常简单是实现是：

```python
def isprime(p:int) -> bool:
    if p == 2:
        return True
    elif p % 2 == 0 or p == 1:
        return False
    for i in range(3, int(pow(p, 1/2)) + 2, 2):
        if p % i == 0:
            return False
    return True

def factors(N:int) -> dict:
    res = {}
    for i in range(2, N + 1):
        if not isprime(i):
            continue
        k = 0
        while N % i ** (k + 1) == 0:
            k += 1
        if k > 0:
            res[i] = k
    return res

print(factors(120))  # {2: 3, 3: 1, 5: 1}
print(factors(97))  # {97: 1}
```

由于一个 `int` 表示的整数一般不会有超过30个不同的质因数（并且该质因数的指数也一般不超过30，想想这是为什么），因而可以认为空间复杂度是 $O(1)$。

接下来我们计算一下这种方法的时间复杂度。对于一个自然数 $p$，仅判断它是否是质数需要遍历从3到 $\\sqrt p$的所有奇数，用时 $\\sqrt p$ ，对于从 2 到 $N$ 的每个奇数都去判断一遍，共计 $O(n \\sqrt n)$。

显然这样做不是最优方法。因为一个数 $N$ 不可能有超过两个大于 $\\sqrt N$ 的质因数！！！

So, 我们只需要把 $N$ 在 $ \\sqrt N$ 内做质因数分解，剩下还没有分解掉的就是剩下的那个质因数了。（想想这个数为什么一定是质数）

还是贴python代码：

```python
def isprime(p:int) -> bool:
    # 跟上面一样，判断是否是质数
    if p == 2:
        return True
    elif p % 2 == 0:
        return False
    for i in range(3, int(pow(p, 1/2)) + 2, 2):
        if p % i == 0:
            return False
    return True

def factors(N:int) -> dict:
    res = {}
    sqrt = int(N ** 0.5) + 1
    for i in range(2, sqrt):
        if not isprime(i):
            continue
        while N % i == 0:
            res[i] = res.get(i, 0) + 1
            N //= i
    if N > 1:
        res[N] = 1
    return res
```

However，细心的你可能会发现，好像根本不需要判断质数这一步

因为有 `while` 循环，所以结果中根本不可能分解出非质数（想想这又是为什么）

所以代码可以简化到：

```python
def factors(N:int) -> dict:
    res = {}
    sqrt = int(N ** 0.5) + 1
    for i in range(2, sqrt + 1):
        while N % i == 0:
            res[i] = res.get(i, 0) + 1
            N //= i
    if N > 1:
        res[N] = 1
    return res
```

`while` 循环总的执行次数是有限的，因此总的时间复杂度就是 `for` 循环带来的 $O(\\sqrt n)$ 。

到这里，我也再想不出什么可以优化这个 `for` 循环的方法了。

最后贴一下C++的实现：

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_map>

using namespace std;

unordered_map<int, int> factors(int N) {
    unordered_map<int, int> res;
    const int sq = sqrt(N) + 1;
    for (int i = 2; i <= sq; i++) {
        while (N % i == 0) {
            res[i]++;
            N /= i;
        }
    }
    if (N > 1) res[N] = 1;
    return res;
}

int main() {
    unordered_map<int, int> res = factors(120);
    for (auto it = res.begin(); it != res.end(); it++) {
        cout << it->first << ": " << it->second << endl;
    }
}
// 结果：
// 5: 1
// 3: 1
// 2: 3
```