#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : running_fish
# @Time     : 2020/3/17 0017 下午 14:57
# @File     : day10_MongoDB.py
# @Software : PyCharm

import pymongo

# 1、创建MongoDB的链接对象
client = pymongo.MongoClient(host='0.0.0.0', port=27017)

# 也可以这样创建
client = pymongo.MongoClient('mongodb://localhost:27017/')

# 2、指定数据库：调用client的test属性即可返回test数据库
db = client.test
db = client['test']

# 3、指定集合
collection = db.students
collection = db['students']

# 4、插入数据
student = {
    'id': '1002',
    'name': 'Bob',
    'age': '20',
    'gender': 'male',
}

result = collection.insert_one(student)

print(result.text())
# 断开连接，将关闭连接池汇总的所有基础套接字，如果再次使用此实例，它将自动重新打开
client.close()
