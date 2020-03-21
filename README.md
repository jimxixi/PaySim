# PaySim

|文件名|说明|
|-|-|
|InitScript.sql|创建数据库的脚本|
|PaySim数据库设计.md|数据库表结构设计|
|PaySim.db|用上述脚本创建的数据库|
|PayLib.py|操作数据库的依赖库|
|paymentServer.py|依赖PayLib.py实现的服务端程序|
|test.py|无用的临时脚本|
|...|其它一些图示|

## 如何运行

- 依赖python3.8
- python3.7/python3.6也有可能运行，但没有测试过。
- pip install pymysql
- pip install tornado
- $ python3.8 paymentServer.py

## 如何接入

- 商户端使用PaySimTool.py提供的函数接入
- 散客端使用PaySimTool.js提供的函数接入


