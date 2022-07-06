# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : test.py
@Project: WebGrap1
@Time   : 2022-06-10 15:31:24
@Desc   : The file is ...
@Version: v1.0
"""
import re
import this
import time
import urllib

import numpy as np
import requests
import pandas as pd
from flask import json
import math

from numpy.random import randint

user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
]

# with open(r"D:\Program Files\SoftWare\木头超级字典生成器 V6.20\mutou.txt") as f:
#     rows = f.readlines()
#     for r in rows:
#         print(r)
def sort_n_rmDup(s):
    s = set(s)
    s = list(s)
    s.sort()
    new_s = ''
    for ele in s:
        new_s = ','.join(s)
    return new_s



# def fn(n):
#   if n <= 1:
#     return False
#   i = 2
#   while i*i <= n:
#     if n % i == 0:
#       return False
#     i += 1
#   return True
# s = 0
# for i in range(100, 201):
#     if fn(i):
#         s += 1
# print(s)
# result = 0
# n = input("请输入一个三位数的正整数：")
# while True:
#     # 只能输入三位长度
#     if len(n) != 3:
#         n = input('不是三位数，请重新输入: ')
#         continue
#
#     # 只能输入整数
#     try:
#         for i in range(len(n)):
#             int(n[i])
#     except:
#         n = input('只能输入三位正整数，请重新输入: ')
#
#     else:
#         # 百分位
#         n1 = eval(n) // 100
#         # 十位
#         n2 = eval(n) // 10 % 10
#         # 个位
#         n3 = eval(n)  % 10
#         result += n1 ** 2 + n2 ** 2 + n3 ** 2
#         print('各个数字的平方和是 %d' % result)
#         break



    # x = np.random.random((2, 3))
    # y = np.random.randint(0, 2, (2, 2))
    # print(x,y)
    # with open("mtest.json", 'r') as f:
    #     dict = json.load(f)
    #     for item in dict["data"]:
    #         print(item["_id"])
    #         print(item["name"])
    #         print(item["module"])
    #         print(item["func"])
    #         print(item["system"])
    #         print(item["bank"])
    #         print(item["phase"])
    #         print(item["staff"])
    #         print(item["book"])
    #         print(item["bank"])
if __name__ == "__main__":
    a = [1,2,3]
    print(11)