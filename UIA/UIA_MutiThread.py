#!/usr/bin/env python
# coding: utf-8
import json
import re
import sys
import threading

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_html(url):
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

    r = requests.get(url, headers=headers,timeout=60)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text



def get_cols_data(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    # soup = BeautifulSoup(html, features="html5lib")
    if soup is not None and len(soup) > 0:
        table = soup.find('div', class_='view-content').find('table')
        ths = table.find('thead').find('tr')
        cols = []
        for th in ths:
            text = th.text.strip()
            cols.append(text)
        trs = table.find('tbody').find_all('tr')
        data = []
        for tr in trs:
            tds = tr.find_all('td')
            info = []
            for td in tds:
                text = td.text.strip()
                info.append(text)
            if info is not None and len(info) > 0:
                data.append(info)
    return cols, data


# def get_df(url):
#     cols, data = get_cols_data(url)
#     if len(cols) < 1 or len(data) < 1:
#         return
#     print(cols, data)
#     new_cols = []
#     for col in cols:
#         if len(col.strip()) > 0:
#             new_cols.append(col)
#     df = pd.DataFrame(data)
#     df.columns = new_cols
#     return df


def write_to_excel(result_all):
    if result_all is not None and len(result_all) > 0:
        columns = ["Name","Acronym","Founded","City HQ","Country/Territory HQ","Type I","Type II","UIA Org ID"]
        df = pd.DataFrame(result_all, columns=columns)
        df.to_excel(f'UIA_page1-{str(total_page)}.xlsx', index=None)
        print(f'写入成功')
        sys.exit()
# write_to_excel()
class ThreadFactory(threading.Thread):
    def __init__(self, url, page):
        threading.Thread.__init__(self)
        self.url = url
        self.page = page


    def run(self):
        time.sleep(1)
        print(f'正在爬取第{str(self.page)}页')

        cols, data = get_cols_data(url)
        if data is not None and len(data) > 0:
            result_all.extend(data)
        if int(self.page) == total_page - 1:
            write_to_excel(result_all)


if __name__=='__main__':
    url_index = 'https://uia.org/ybio'
    total_page = int(input('请输入想爬取的页数：'))  # 3020,75490
    result_all = []
    while 1 == 1:

        try:
            url_list = []
            for page in range(total_page):  # 前两页
                url = f"{url_index}?page={str(page)}"
                url_list.append(url)
        except ValueError:
            print("获取失败")
            time.sleep(1)
            continue
        else:
            threads = []
            for url in url_list:
                reg = re.compile(r'page=(\d+)')
                page = reg.findall(url)
                threads.append(ThreadFactory(url,''.join(page)))
            for t in threads:  # 开启线程
                t.start()
                time.sleep(0.01)
            for t in threads:  # 阻塞线程
                t.join()
            # break
        time.sleep(1)