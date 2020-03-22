#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : running_fish
# @Time     : 2020/3/16 0016 下午 22:16
# @File     : day09_pyMySQL.py
# @Software : PyCharm
'''存储方式：MySQL'''

import pymysql

'''
1、创建数据库student_list："CREATE DATABASE student_list DEFAULT CHARACTER SET utf8"
2、创建表并指定字段信息;'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
3、插入数据：INSERT INTO students(id, name, age) value (%s, %s, %s)
4、用字典构建动态插入数据：
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

5、插入不重复的数据：
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
update = ','.join([' {key}=%s'.format(key=key) for key in data])
sql += update

6、更新数据：'UPDATE students SET age=%s WHERE name=%s'
7、删除数据：'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
8、查询数据：'SELECT * FROM students WHERE age>= 20'
      
'''



# 建立连接，并创建数据库student_list
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()  # 获得MySQL的操作游标
cursor.execute('SELECT VERSION()')  # 执行SQL语句
data = cursor.fetchone()  # 获取第一条数据
print('Database.version:', data)
cursor.execute("CREATE DATABASE student_list DEFAULT CHARACTER SET utf8")  # 创建student_list数据库
db.close()

# 创建表
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='student_list')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, ' \
      'age INT NOT NULL,PRIMARY KEY (id))'
cursor.execute(sql)
# 断开连接，避免一直占用内存
db.close()

# 插入数据
id = '1001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='student_list')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) value (%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()

# 用字典动态构建通用的插入方式
data = {"id": "1004", "name": "pigs", "age": 21}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()


# 更新数据
sql = 'UPDATE students SET age=%s WHERE name=%s'
try:
    cursor.execute(sql, (25, 'pig'))
    db.commit()
    print('ok')
except :
    db.rollback()
    print('not ok')
db.close()

# 存储不重复的数据
data = {"id": "1001", "name": "big_pigs", "age": 30}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
update = ','.join([' {key}=%s'.format(key=key) for key in data])
sql += update

try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('ok')
        db.commit()
except :
    print('not ok')
    db.rollback()
db.close()


# 删除数据
table = 'students'
condition = 'age > 29'

sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except :
    db.rollback()
db.close()
# 删除条件有多种多样，运算符有大于，小于，等于，LIKE等，条件链接符有AND,OR等
# 所以不再继续构造复制的判断条件，直接将条件当作字符串传递，以实现删除操作


# 查询数据
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='student_list')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age>= 20'

try:
    cursor.execute(sql)
    print('count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('results:', results)
    print('results type:', type(results))
    for row in results:
        print(row)
except :
    print('Error')

# 用while循环加fetchone()方法来获取所有数据，会更高效
sql = 'SELECT * FROM students WHERE age>= 20'
try:
    cursor.execute(sql)
    print('count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print("row:", row)
        row = cursor.fetchone()
except :
    print('not ok')