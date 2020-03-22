#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : running_fish
# @Time     : 2020/3/13 0013 下午 16:49
# @File     : day07_txt.py
# @Software : PyCharm

'''
数据存储
1、txt
'''

import requests
from pyquery import PyQuery as pq
import chardet

url = 'http://www.quanben.co/sort/3_1.html'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/80.0.3987.132 Safari/537.36'}
res = requests.get(url=url, headers=headers).text
doc = pq(res)
div = doc('.Sum.Search_line')
for item in div.items():
    title = item.find('h2').text()
    author = item.find('.blue').text()
    content = pq(item.find('p')).text()
    print(title, author, content)
    with open('../requests_learning/result.txt', 'w', encoding="utf-8") as file:
        file.write('\n'.join([title, author, content]))
        file.write('\n'+'='*50 + '\n')
# TODO 保存的txt文档出现乱码

