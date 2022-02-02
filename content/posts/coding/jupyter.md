---
title: "在 Jupyter 中安装 R 和 Julia"
date: 2022-01-01
draft: false
slug: jupyter-r-julia
categories: ["算法与程序设计"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

**R**


安装如下包

```r
install.packages(c('rzmq','repr','IRkernel','IRdisplay'),
                 repos = c('http://irkernel.github.io/', getOption('repos')))

IRkernel::installspec()
```

参见：[https://irkernel.github.io/installation/](https://irkernel.github.io/installation/)



**Julia**

首先确保 `jupyter` 命令在当前环境变量下。

安装1.5以上版本后，在julia终端中，依次执行：`import Pkg`、`Pkg.add("IJulia")`、`Pkg.build("IJulia")`。

如果遇到联网或者下载速度的问题，考虑设置国内的镜像源，依次执行：`Pkg.add("JuliaZH")`、`using JuliaZH`、`JuliaZH.set_mirror("BFSU")`。

执行 `versioninfo()` 命令，如果观察到 `JULIA_PKG_SERVER` 的地址是BFSU的镜像源，就代表配置成功了。


##### Jupyter

查看Jupyter当前支持的kernel：`jupyter kernelspec list`

```bash
Available kernels:
  julia-1.0    /home/user/.local/share/jupyter/kernels/julia-1.0
  julia-1.1    /home/user/.local/share/jupyter/kernels/julia-1.1
  python3      /home/user/anaconda3/share/jupyter/kernels/python3
```

接着执行 `jupyter kernelspec uninstall julia-1.0` 即可删去不用的kernel。


参考：
+ https://stackoverflow.com/questions/44914176/how-to-remove-previous-version-from-jupyter/45211705