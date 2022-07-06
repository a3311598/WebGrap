#!/usr/bin/env python
# coding: utf-8
import json
import threading
# from lxml import etree
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_html(url):
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'uia.org',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/101.0.4951.54 Safari/537.36 '
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None


def get_cols_data(url):
    resp = get_html(url)
    # cols = []
    data = []
    if resp is None:
        return ""
    soup = BeautifulSoup(resp, features="html5lib")

    table = soup.find('div', class_='view-content').find('table')
    ths = table.find('thead').find('tr')


    # for th in ths:
    #     text = th.text.strip()
    #     cols.append(text)
    trs = table.find('tbody').find_all('tr')
    # if len(cols) < 1:
    #     return ""

    for tr in trs:
        tds = tr.find_all('td')
        info = []
        for td in tds:
            text = td.text.strip()
            info.append(text)
        if info is not None and len(info) > 0:
            data.append(info)
    if len(data) < 1:
        return ""
    return data


def write_to_excel(url_index, total_page):
    result = []
    start_page = 0
    substact_val = 200  # 打包数量
    for page in range(start_page, total_page):  # 前两页
        time.sleep(1)
        print('正在爬取第{}页'.format(page + 1))
        url = f"{url_index}?page={str(page)}"
        data = get_cols_data(url)
        # 每两百页保存一次
        if data == "":
            continue
        result.extend(data)
        if page - start_page + 1 == substact_val:
            columns = ["Name", "Acronym", "Founded", "City HQ", "Country/Territory HQ", "Type I", "Type II",
                       "UIA Org ID"]
            df_res = pd.DataFrame(result, columns=columns)
            df_res.to_excel(f'UIA_page{start_page + 1}-{str(page + 1)}.xlsx', index=None)
            print("数据保存成功～")
            result = []
            start_page = page
if __name__=='__main__':
    url_index = 'https://uia.org/ybio'
    total_page = int(input('请输入想爬取的页数：'))  # 3020,75490
    write_to_excel(url_index, total_page)