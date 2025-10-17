---
layout: post
title: "个人博客的搭建"
subtitle: "基于Github Pages与Hux Blog进行搭建"
author: "Zihan Zhang"
header-style: text
tags:
  - 支线任务
  - 博客
  - 个人网站
---

### 0. 声明

由于本人能力问题，本文可能存在不严谨、不准确等问题，如有读者发现，欢迎发送邮件至zhangzihan.cs@gmail.com或在GitHub中对[本项目](https://github.com/zihan-zhang-cs/zihan-zhang-cs.github.io)发起issue。如果本篇文章帮助了你，欢迎点赞、收藏、star。

### 1. 前言

在Flink的相关学习中，发现现在的学习资料不多，因此我将我的学习过程和踩过的坑进行了记录，但是现在记录主要局限于私域中，对于开源社区并没有什么帮助，于是我现在将内容放出，希望能帮助到有需要的人们。第一篇博客就以搭建个人博客网站为内容，简单介绍一下基于Github Pages与Hux Blog的个人博客搭建方法。

### 2.项目Fork

点击[此处](https://github.com/Huxpro/huxpro.github.io)打开Hux Blog项目，点击Fork。Fork的仓库务必以```<本账户ID>.github.io```命名，如```zihan-zhang-cs.github.io```。

![image-20251017161146938](https://github.com/zihan-zhang-cs/zihan-zhang-cs.github.io/blob/master/_posts/assets/image-20251017161146938.png?raw=true)

你可以在此处查看你的ID

![image-20251017161524470](https://github.com/zihan-zhang-cs/zihan-zhang-cs.github.io/blob/master/_posts/assets/image-20251017161524470.png?raw=true)

打开你自己的仓库，依次点击这两个按钮获取项目的https地址。

![image-20251017162359841](https://github.com/zihan-zhang-cs/zihan-zhang-cs.github.io/blob/master/_posts/assets/image-20251017162359841.png?raw=true)

在本地执行```git clone <复制内容>```将代码拉取到本地。

### 3.个性化设置与文章发布

你可以修改项目中```_config.yml```文件来进行个性化设置，如修改网站标题等。

个人介绍部分的修改位于```_includes\about```目录下，分别是中文和英文的部分。

我写了一个自动化脚本：

```bash
@echo off
REM 自动提交并推送更改脚本

REM 添加所有更改
git add .

REM 提交更改
git commit -m "upload a blong"

REM 推送到远程仓库
git push origin master

REM 提示推送完成
echo push success!
pause

```

将其以bat格式保存到本地仓库的根目录下，发布博客后续只需要将md文件放到_post```目录下然后执行本脚本即可。