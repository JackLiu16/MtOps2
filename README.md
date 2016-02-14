# MtOps2
运维资产平台，针对公司业务特点开发的运维资产平台。

## 功能
1. 资产管理
2. 代码上线
3. 服务器登陆权限授权
4. 数据库建表、改表审核（对接 DBA 接口）

## 技术栈
####Web 端
Django 1.8.2＋Mysql＋sbadmin(基于 bootstrap 开发的管理系统模版）＋jQuery
####异步队列
celery + redis

####第三方app
grappelli＋guardian

## 项目截图
登录页示例截图
![登陆界面截图](https://github.com/chenxc86/MtOps2/raw/master/static/imgs/QQ20160214-3.png)

列表页示例截图
![列表页示例截图](https://github.com/chenxc86/MtOps2/raw/master/static/imgs/QQ20160214-2.png)

详情页示例截图
![详情页示例截图1](https://github.com/chenxc86/MtOps2/raw/master/static/imgs/QQ20160214-0.png)
![详情页示例截图2](https://github.com/chenxc86/MtOps2/raw/master/static/imgs/QQ20160214-1.png)

表单页示例截图
![详情页示例截图2](https://github.com/chenxc86/MtOps2/raw/master/static/imgs/QQ20160214-4.png)
