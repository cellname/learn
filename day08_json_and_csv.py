#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : running_fish
# @Time     : 2020/3/16 0016 下午 17:03
# @File     : day08_json_and_csv.py
# @Software : PyCharm


'''数据存储方式：json'''

import json

# 读取json  使用 loads （）方法将字符串转为 JSON 对象
obj = ''' [{"name": "Bob",
        "gender": "male",
        "birthday": "1992-10-28"
        }, {
        "name": "Selia",
        "gender": "female",
        "birthday": "1995-10-18"
        }]'''
print(type(obj))
data = json.loads(obj)  # loads的参数必须是str, bytes or bytearray
print(data, type(data))
print(data[0]["name"])  # 通过索引来取值
print(data[0].get('peter', None))  # get()方法可以传入第二个参数（默认值），避免键名不存在，报错 推荐使用
# 注意： 字典内的键和值必须使用双引号

with open('data.json', 'r') as file:
    obj = file.read()
    data = json.loads(obj)
    print(data, type(data))  # 输出的是list


# 输出json
data = [{
        "name": "Bob",
        "gender": "male",
        "birthday": "1992-10-28"
        }]
print(json.dumps(data), type(json.dumps(data)))  # dumps()输出的是str
with open('data1.json', 'w') as file:
    file.write(json.dumps(data))
    file.write(json.dumps(data, indent=2))  # 自动缩进
    file.write(json.dumps(data, indent=2, ensure_ascii=False))  # 避免中文乱码


'''存储方式：csv'''
# 写入数据
import csv
with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1001', 'wangxiaojian', '21'])
    writer.writerow(['1002', 'pig', '18'])

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['1001', 'wangxiaojian', '22'], ['1002', 'peter', '24']])
    # writerows同时写入多行数据，必须使用二维列表

# csv写入字典的方式
with open('data2.csv', 'w') as file:
    fieldnames = ['id', 'name', 'age']  # fieldnames 字段名
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # 写入表头信息
    writer.writerow({"id": "1001", "name": "wangxiaojian", "age": "22"})
    writer.writerow({"id": "1002", "name": "pig", "age": "23"})
    writer.writerow({"id": "1003", "name": "Bob", "age": "25"})

# 避免编码出错，可以指定编码方式 a表示追加写入
with open('data.csv3', 'a', encoding="utf-8") as f:
    pass


#  csv方式读取
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            print(row)


# 总结： txt, json在打开文件后，都是用文件本身的file.writer（写入）和file.read（读取）方法
# csv则是用csv.writer(写入)和csv.reader(读取)方法
