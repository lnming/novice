### 说明
  一个很简单的脚本，可以爬取haopic网页上的图片信息．该脚本主要用于技术实践练习： 使用 requests 抓取， bs4 解析， peewee 作为 orm 框架存储．

### 各文件说明：
  * schema.sql: 数据库的sql文件；
  * haopic.py: 使用 python -m pwiz -e sqlite haopic.db > haopic.py 自动生成的数据模型；
  * main.py: 包括网页抓取，页面解析，信息存储功能；
