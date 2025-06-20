# aust_RM_git_train
git是一个很好用的代码管理工具，适合团队共同开发项目，学习git对rm或者对以后的工作都会很有帮助
# 简单的使用说明

## 连接仓库

`git remote add origin https://github.com/wxm-aust/aust_RM_git_train.git`

或者

`git remote add origin git@github.com:wxm-aust/aust_RM_git_train.git`

## 拉取代码

`git pull origin main`

## 创建分支

`git branch dev`

## 切换分支

`git checkout dev`

## ~~修改代码~~

## 提交修改

```
git add *
git commit -m "优化了一些功能"
```

## 推送修改
```
git checkout main
git merge dev
git push origin main
```

命令参数具体含义查看[改变了世界的软件！程序员的基本功，_Git_ 应该如何使用？](https://www.bilibili.com/video/BV1u94y1n73L/?spm_id_from=333.1387.search.video_card.click)和[人人都能看懂的_Git_教程！_Git_如何和 _Git_Hub、_Git_Lab 交互？团队如何用 _Git_ 协作开发？小白也能看懂的_Git_教程！](https://www.bilibili.com/video/BV1d6XVYqEuy/?spm_id_from=333.1387.search.video_card.click)以及善用百度和AI