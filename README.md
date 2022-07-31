# 一个使用python编写的记账本

**简介**

这个项目是一个Python的图形化设计，名称为记账本

**开发工具及环境介绍**

PyCharm专业版，版本2020.2.2，Python版本3.10.2，连接的数据库SQL server2019

**使用的第三方库**

tkinter pymssql

**项目内容说明**

采用表格式布局，一共四个文件main.py table.sql unit.py dataBase.py，如果赖得倒入项目，可以直接下载那四个文件，关于最大化的布局没有进行适配

从main.py开始运行

main.py

存放的是所有界面的代码和页面对应的方法，每个界面都是一个类，绘制界面的代码放在了__init__方法里

table.sql

数据库建的表

一张T_information信息表，一张用户表T_user

用户表

username用户名，password密码，均为varchar非空

信息表

date nvarchar类型，记录花钱的日期

event nvarchar类型，记录花钱的事件

consumption 浮点数类型，记录花的钱数

dataBase.py

处理与数据库操作有关的函数，executeQuery处理查询操作，executeUpdate处理增删改操作，传入的参数都是sql语句

unit.py

负责数据库的连接
