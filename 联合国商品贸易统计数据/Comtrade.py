# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : Comtrade.py
@Project: WebGrap1
@Time   : 2022-06-19 12:01:24
@Desc   : The file is ...
@Version: v1.0
"""
import csv
import json
import time
from random import random, randint

import requests
import FakeUserAgent

proxies = FakeUserAgent.getProxies()
user_agents = FakeUserAgent.getUserAgent()


def getData(url, title):
    url_target = url+'&fmt=csv'

    resp = requests.get(url_target,headers=headers, timeout=60)
    time.sleep(1)
    error1 = 'USAGE LIMIT'
    error2 = 'No data matches your query or your query is too complex'
    # if resp.content.decode(encoding='utf-16 LE').__contains__(error1):
    #     print(resp.text)
    #     time.sleep(3600)
    if not resp.text.__contains__(error2) and len(resp.text) > 250:
        print(url_target)
        with open('save_url.txt', mode='w', encoding='utf-8') as f:
            f.write(url_target+'\n')
    else:
        return
    with open(f"comtrade_{title}.csv", "wb") as f:
        f.write(resp.content)
    time.sleep(36)
def getPatners():
    url3 = 'https://comtrade.un.org/Data/cache/partnerAreas.json'
    resp = requests.get(url3, headers=headers).text
    time.sleep(1)
    if resp.startswith(u'\ufeff'):
        resp = resp.encode('utf8')[3:].decode('utf8')
    json_dic = json.loads(resp)
    for i in json_dic["results"]:
        yield i['id']

def getClassificationHS():
    url1 = 'https://comtrade.un.org/Data/cache/classificationHS.json'
    resp = requests.get(url1, headers=headers).text
    time.sleep(1)
    if resp.startswith(u'\ufeff'):
        resp = resp.encode('utf8')[3:].decode('utf8')
    json_dic = json.loads(resp)
    for i in json_dic["results"]:
        yield i['id']


def getReports():
    url2 = 'https://comtrade.un.org/Data/cache/reporterAreas.json'
    resp = requests.get(url2, headers=headers).text
    time.sleep(1)
    if resp.startswith(u'\ufeff'):
        resp = resp.encode('utf8')[3:].decode('utf8')
    json_dic = json.loads(resp)
    for i in json_dic["results"]:
        yield i['id']
if __name__ == '__main__':
    years = [2022-i for i in range(1,21)]

    # url = 'http://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps=2013&r=826&p=0&rg=all&cc=ALL&fmt=csv&uitoken=6b98a54e3cad08911f027432fe20dfb5'
    # http: // comtrade.un.org / api // refs / da / bulk?ps = 2013

    # url = 'https://comtrade.un.org/api/refs/da/bulk?type=C&freq=A&px=HS&ps=2021&r=156&p=ALL&rg=1&cc=ALL&uitoken=6b98a54e3cad08911f027432fe20dfb5'
    random_agent = user_agents[randint(0,len(user_agents)-1)]
    headers = {
        "User-Agent": random_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br"
    }
    print(proxies)
    reports = getReports()
    for i in reports:
        if i.lower() != "all":
            for y in years:
                    cc = getClassificationHS()
                    for j in cc:
                        if j.lower() == 'all':
                            continue
                        p = getPatners()
                        for k in p:
                            if k.lower() == 'all':
                                continue
                            title = str(y)+"_"+'r'+str(i)+'p'+str(k)+'cc'+str(j)
                            url = f'https://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps={str(y)}&r={i}&p={k}&rg=1&cc={j}&uitoken=661f2ce8eb4ab0b3ef9fe2442febe938'
                            getData(url, title)
                            print(url)
                            time.sleep(1)
                    # time.sleep(37)
    # getReports()