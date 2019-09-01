# PolarisHub (Flask Version)

[[EN]](README.md) **[中文版本]**

1. [PolarisHub简介](#intro)
2. [安装PolarisHub](#install)
3. [运行PolarisHub](#run)
4. [PolarisHub的优势](#advantage)
5. [PolarisHub的灵感来源](#inspiration)
6. [我们的计划](#plan)

<span id="intro">

## PolarisHub 简介

**PolarisHub**是一款**免费**，**极速**，**使用简便**以及**安全**的文件传输工具。基于*Flask(Python)*，当前版本的**PolariHub**通过*Python*几乎可以安装在所有的计算机上。您可以使用命令`phub`将其启动，并通过*浏览器*界面（GUI）来管理您的**PolarisHub**。 在您的使用过程中，您可以通过*url链接*或者*二维码*两种方式来共享文件，同一网络中的任何人都可以访问您的共享文件。

</span>

<span id="install">

## 安装PolarisHub 

PolarisHub共有两种安装方式：使用*pip*安装（推荐）或者在[github](git clone https://github.com/XieGuochao/polarishub_flask.git)上下载源代码

### 使用_pip_来安装PolarisHub

1. 确保你的电脑已经安装了*Python3*和*pip*，并请将*pip*更新至最新版本
2. 打开电脑终端（terminal），输入`$ pip install polarishub_flask`或者`pip install polarishub_flask==X.X.X（版本型号）`
3. PolarisHub会自动安装到你的电脑

### 下载PolarisHub的源代码

1. `git clone https://github.com/XieGuochao/polarishub_flask.git`

</span>

<span id="run">

## 运行PolarisHub

同样的，你可以通过两种方式来运行PolarisHub：

### 运行*pip*安装的PolarisHub

1. 打开电脑终端（terminal），输入`$ phub`
2. 如果你需要更多的信息或者帮助，可以输入`$ phub -h`来运行PolarisHub

### 运行PolarisHub源代码

1. 打开电脑终端（terminal），输入`$ cd /你的路径/polarishub_flask`去到你下载的PolarisHub所在位置
2. 输入`$ python3 fastrun.py`
3. 同样的，如果你需要更多的信息或者帮助，可以输入`$ python3 fastrun.py -h`来运行PolarisHub

</span>

<span id="advantage">

## PolarisHub的优势

### 与*OneDrive*， *iCloud* 或类似的云储存工具相比

1. **快速**。利用几乎无限带宽的局域网，使用**PolarisHub**的文件传输可以达到网络的速度限制，即X MB / s~XX MB / s。
2. **隐私**。**PolarisHub**是一个分散管理的平台，并没有提供一个集中的云文件中心。因此，您拥有文件**100%**的访问权限，没有人能够觉察您的文件传输。
3. **安全**。**PolarisHub**是一个开源项目，每个人都可以帮助修复潜在的错漏，并且不存在隐私泄露的问题

### 与*微信* 相比

1. **无限大小的文件**。和*微信*不同，在**PolarisHub**上的文件传输不用再担心文件的大小。
2. **快速**。详情请见上面。

### 与*AirDrop*相比

1. **跨平台**。没有Apple硬件的限制，我们正在构建一个每一台计算机都能使用的软件！
2. **更长的距离**。只要转移在局域网内，甚至可以在*上园* 和*下园* 之间以及每个教室或者建筑物之间进行文件传输！

### 其他优点

1. **易于安装和使用**。 ***PolarisHub **可以通过使用*Python*的*pip*安装在每台计算机上。它没有编译要求。

</span>

<span id="inspiration">

## PolarisHub的灵感来源

如上所述，**PolarisHub**的灵感来自当前文件传输工具（如*微信*，*百度网盘* 等）的不完美体验。因此，我们正在尝试构建一个能够克服其他工具所有缺点的软件，这是一款**免费**，**极速**，**使用简便**以及**安全**的工具。

</span>

<span id="plan">

## 我们的计划

我们欢迎所有对**PolarisHub**感兴趣的人加入我们：**Polaris Studio**！您可以在GitHub上找到我们https://github.com/XieGuochao/polarishub_flask 或通过电子邮件 st_polarisstudio@link.cuhk.edu.cn 联系我们。
[点击此处](https://mp.weixin.qq.com/s?__biz=MzU2NjUwMzk3Mw==&mid=2247483776&idx=1&sn=a248165c9f313f96b491c2550cc1df47&chksm=fcaa3ecacbddb7dc4f0b47e3c939d3ed8fe4590ba782a3ca616d28038eefeb27feefe49aa0ac&token=37640579&lang=zh_CN#rd)可获取关于**PolarisHub**的微信推送

1. **GO 版本**。我们将在*Golang*中重新构建**PolarisHub**，使其能够编译并安装在没有*Python*的每个平台上。
2. **公共的服务器**。我们将构建一个公共服务器，以便每个人都可以在上面共享文件的链接（在局域网中）。
3. **更强大的PolarisHub**。我们将为**PolarisHub**添加更多功能，如*访问密码*等。敬请期待。

</plan>
