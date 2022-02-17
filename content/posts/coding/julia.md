---
title: "Julia 的函数"
date: 2020-10-12
draft: false
slug: julia-function
categories: ["算法与程序设计"]
tags: ["Julia"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


## 函数定义

Julia定义函数的方式非常灵活。标准的定义方式类似于MATLAB：
```julia
function f(x,y)
  x + y  # 等价于 return x + y
end
```
**Julia默认把最后一行的内容作为返回值**，但如果有`return`句，则会立刻返回`return`语句后面的值。

此外，也可以用一行来定义简单的函数：
```julia
f(x, y) = x + y
```
此外，由于Julia无缝支持各类unicode，还可以使用特殊字符：
```julia
Σ(x, y) = x + y  # Σ = \Sigma + <Tab>
```

函数的调用方法非常直接：
```julia
f(2,3)
# 5
```

可以用符号`::`来指定返回值类型，程序会再返回时做一个类型转换。（如果转换失败，则会报错）

```julia
function g(x, y)::Int8
  return x * y
end

Σ(x, y)::Int8 = x + y
typeof(Σ(2, 3))    # Int8
```

如果不希望函数有返回值，那么就`return nothing`，这里跟Python的`return None`比较类似，`return`后的`nothing`是可以被省略的。值得注意的是，`nothing`是一个单例。

## 匿名函数


在Julia中函数是一等公民，即意味着函数可以作为另一个函数的参数。

可以通过以下方式定义一个匿名函数：
```julia
x -> x^2 + 2x - 1
map(x -> x^2 + 2x - 1, [1, 3, -1])
```
匿名函数适合在`map`等函数中使用。

同样，匿名函数也可以有多个参数：
```julia
(x,y,z) -> 2x + y - z
```

## 函数的多个返回值

**Julia使用`Tuple`这一数据结构来实现返回多个值的功能。**

```julia
x = (0.0, "hello", 6*7)
typeof(x)  # Tuple{Float64,String,Int64}
```

一个tuple可以有多种数据类型。跟Python一样，元组并不需要显式地用括号括起来。

Julia还支持具名元组：
```julia
x = (a=2, b=1+2)
x.a  # 2
```

想要让一个函数返回多个值，那么就用一个元组来包含它们就好了：
```julia
function foo(a,b)
  a+b, a*b
end
```

Julia对元组有着类似Python的支持，比如：
```julia
x, y = foo(2,3)
```

> 暂时没看到有讲Julia支持序列解包的。

元组可以作为返回值，也可以作为函数的参数。

因为元组的存在，所以Julia支持简介的变量交换写法：
```julia
x, y = y, x
```

## 函数的参数

Julia支持变长参数：
```julia
bar(a,b,x...) = (a,b,x)
bar(1,2,3)  # (1, 2, (3,))
```
函数`bar`第三个及以后的参数会变成一个元组。

同时，Julia支持把元组中的元素逐个作为函数参数：
```julia
x = (2, 3, 4)  # x 也可以是其它序列类型
bar(1, x...)  # (1, 2, (3, 4))
```

Julia还支持默认值参数和关键词参数：
```julia
f(x, y=1) = x + y
f(x; y=1) = x + y  # 参数y必须以关键词参数的形式传递，; 类比python的 *
```

## 函数的复合

在Julia中函数的复合有着非常优美的形式！
```julia
a(x) = x ^ 2
b(x) = x + 2
a(b(2))  # 16
```
我们可以使用上面这个方式来计算函数的复合，但是为了得到复合函数的指针，我们可以使用：`f ∘ g`，其中`∘`符号用`\circ`+`<Tab>`打出。
```julia
map(a ∘ b, [1, 2])
```

此外，Julia还有类似shell中管道的功能，可以**把一个函数的输出作为另一个函数的输入**，使用符号`|>`，如果要广播，那么用`.|>`

```julia
1:10 |> sum |> sqrt  # 等价于 (sqrt ∘ sum)(1:10)
# 7.416198487095663
["a", "list", "of", "strings"] .|> [uppercase, reverse, titlecase, length]
```

## 函数的向量化

把一个单值函数变成一个可以作用在数组上的函数，只需要在调用的时候加`.`即可。（功能好比于被`np.vectorize`修饰）

```julia
f(x) = x + 2
A = [1.0, 2.0, 3.0]
sin.(A)
f.(A)
```

同样的功能也可以借助强大的Julia Macro来实现：
```julia
Y = [1.0, 2.0, 3.0, 4.0];
@. X = sin(cos(Y))  # 把该行的所有函数向量化
```

`f.(args...)`等价于`broadcast(f, args...)`，进行广播运算：
```julia
julia> f(x,y) = 3x + 4y; 
julia> A = [1.0, 2.0, 3.0]; 
julia> B = [4.0, 5.0, 6.0]; 
julia> f.(pi, A) 
3-element Vector{Float64}: 
13.42477796076938 
17.42477796076938 
21.42477796076938 
julia> f.(A, B) 
3-element Vector{Float64}: 
19.0 
26.0 
33.0
```
这种向量化的函数会把运算融合起来，`sin.(cos.(X))`只会有一个循环，而不是先计算`cos(X)`再计算`sin(X)`（这样就有两重循环并且有中间变量需要存储）。

## 变量的作用域
Julia的函数，同其它语言一样，有自己的一个作用域。可以通过`global`关键词来修改外部的作用域。
```julia
a = 2
s = 0
function updateS()
    global s = 1
    println(a)
    return
end
updateS()  # 2
println(s)  # 1; 如果上面函数中没有global，输出的是0
```
