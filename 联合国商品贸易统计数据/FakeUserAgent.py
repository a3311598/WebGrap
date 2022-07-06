# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : FakeUserAgent.py
@Project: WebGrap1
@Time   : 2022-06-20 12:42:05
@Desc   : The file is ...
@Version: v1.0
"""
import random
from random import randint

import json
import requests


def getUserAgent():
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
    return user_agents

def getProxies():
    api_url = 'http://api.proxy.ipidea.io/getProxyIp?num=100&return_type=txt&lb=1&sb=0&flow=1&regions=&protocol=http'
    user_agents = getUserAgent()
    random_agent = user_agents[randint(0, len(user_agents) - 1)]
    tunnel = randint(1, 10000)  # generate a
    headers = {
        # "Proxy-Tunnel": str(tunnel),
        "User-Agent": random_agent
    }
    res = requests.post(api_url, headers=headers, verify=True)
    proxie = "https://%s" % (res.text)
    json_str = json.dumps(res.text)
    list_ip = res.text.split("\r\n")

    i = random.choice(list_ip)
    proxies = {
        'http': f'{i}',
        # 'https': f'{i}'
    }
    # temp_proxies = {
    #     'http': '222.129.143.36:9000',
    #     'http': '101.34.55.147:8001',
    #     'http': '39.175.90.51:30001',
    #     'http': '120.42.46.226:6666',
    #     'http': '61.153.251.150:2222',
    #     'http': '124.205.155.155:9090',
    #     'http': '106.54.128.253:999',
    #     # 'http': '192.168.31.252:80',
    # }
    temp_proxies = {
        'http': list_ip[1],
        'http': list_ip[2],
        'http': list_ip[3],
        'http': list_ip[4],
        'http': list_ip[5],
        'http': list_ip[6],
        'http': list_ip[7],
        'http': list_ip[8],
        'http': list_ip[9],
        'http': list_ip[10],
        'http': list_ip[11],
        'http': list_ip[12],
        'http': list_ip[13],
        'http': list_ip[14],
        'http': list_ip[15],
        'http': list_ip[16],
        'http': list_ip[17],
        'http': list_ip[18],
        'http': list_ip[19],
        'http': list_ip[20],
        'http': list_ip[21],
        'http': list_ip[22],
        'http': list_ip[23],
        'http': list_ip[24],
        'http': list_ip[25],
        'http': list_ip[26],
        'http': list_ip[27],
        'http': list_ip[28],
        'http': list_ip[29],
        'http': list_ip[30],
        'http': list_ip[31],
        'http': list_ip[32],
        'http': list_ip[33],
        'http': list_ip[34],
        'http': list_ip[35],
        'http': list_ip[36],
        'http': list_ip[37],
        'http': list_ip[38],
        'http': list_ip[39],
        'http': list_ip[40],
        'http': list_ip[41],
        'http': list_ip[42],
        'http': list_ip[43],
        'http': list_ip[44],
        'http': list_ip[45],
        'http': list_ip[46],
        'http': list_ip[47],
        'http': list_ip[48],
        'http': list_ip[49],
        'http': list_ip[50],
        'http': list_ip[51],
        'http': list_ip[52],
        'http': list_ip[53],
        'http': list_ip[54],
        'http': list_ip[55],
        'http': list_ip[56],
        'http': list_ip[57],
        'http': list_ip[58],
        'http': list_ip[59],
        'http': list_ip[60],
        'http': list_ip[61],
        'http': list_ip[62],
        'http': list_ip[63],
        'http': list_ip[64],
        'http': list_ip[65],
        'http': list_ip[66],
        'http': list_ip[67],
    }
    return temp_proxies
if __name__ == '__main__':
    getProxies()