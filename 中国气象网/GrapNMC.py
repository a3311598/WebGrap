# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : GrapNMC.py
@Project: WebGrap1
@Time   : 2022-06-14 21:13:57
@Desc   : The file is ...
@Version: v1.0
"""
import time
import requests
import pandas as pd



def getProvince(url):
    resp = requests.get(url+'all', headers=hearders).json()
    list_provice_code = []
    for provice in resp:
        list_provice_code.append(provice['code'])
    return list_provice_code
    # print(resp)

def getCity(url, pcode):
    resp = requests.get(url+pcode, headers=hearders).json()
    list_city_code = []
    for city in resp:
        list_city_code.append(city['code'])
    return list_city_code
    # print(resp)

def getHistoryData(url, params):
    resp = requests.get(url, headers=hearders, params=params).json()  # 请求响应的数据
    station = ""
    if resp['data']['real'] != "":
        station = resp['data']['real']['station']
    elif resp['data']['predict'] != "":
        station = resp['data']['predict']['station']
    datas = resp['data']['climate']  # 历史气候数据
    if datas == "":
        return ""
    # print(datas["time"])
    # 构造二维数组
    list_months = []
    for months in datas["month"]:
        list_month = []
        period = datas["time"] #时间段
        province = station['province'] #省份
        city = station['city'] #城市
        month = months["month"]  # 月份
        maxTemp = months["maxTemp"]  # 最大温度
        minTemp = months["minTemp"]  # 最小温度
        precipitation = months["precipitation"]  # 降水量

        list_month.append(period)
        list_month.append(province)
        list_month.append(city)
        list_month.append(month)
        list_month.append(maxTemp)
        list_month.append(minTemp)
        list_month.append(precipitation)
        list_months.append(list_month)
        # print(month, maxTemp, minTemp, precipitation)
    return list_months


if __name__ == "__main__":
    hearders = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'content-type' : 'application/json;charset=UTF-8'
    }
    url_index = 'http://www.nmc.cn/'
    url_wheather = 'http://www.nmc.cn/rest/weather'
    url_province = 'http://www.nmc.cn/rest/province/'
    list_provice_code = getProvince(url_province)
    result_all = []
    for province_code in list_provice_code:
        list_city_code = getCity(url_province, province_code)
        time.sleep(1)
        for city_code in list_city_code:
            print(city_code)
            print(url_wheather+f'?stationid={city_code}')
            params ={'stationid': city_code}
            result = getHistoryData(url_wheather, params)
            if result != "":
                result_all.extend(result)
    df = pd.DataFrame(result_all, columns=['时间段', "省份", "城市", "月份", "最大温度", "最小温度", "降水量"])
    df.to_csv("NMC_Data.csv", index=None)
