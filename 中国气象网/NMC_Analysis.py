# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : NMC_Analysis.py
@Project: WebGrap1
@Time   : 2022-06-16 10:50:32
@Desc   : The file is ...
@Version: v1.0
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def to_barogram(data):
    df.filter(["月份", "降水量"])
    plt.bar(df["月份"], df["降水量"], color=['g'], width=0.5)
    plt.title("（1981年-2010年）全国月度累计降水", fontsize=22)
    plt.ylabel("降水（mm）", fontproperties="SimSun")  # 宋体
    plt.show()


def to_broken_line(data):
    df.filter(["月份", "最大温度", "最小温度"])
    max_temp = data["最大温度"]
    min_temp = data["最小温度"]
    plt.plot(max_temp, color='r', linewidth=1, linestyle='-', label='平均最高温度')  # color指定线条颜色，labeL标签内容
    plt.plot(min_temp, color='b', linewidth=1, linestyle='-', label='平均最低温度')  #  color指定线条颜色，labeL标签内容
    plt.legend(loc=2)  # 标签展示位置，数字代表标签具位置，1右，2左
    plt.xlabel('月份')
    plt.ylabel('温度(°C)')
    plt.title('（1981年-2010年）全国月度平均温度')
    # 显示x轴的刻标以及对应的标签
    months = (str(i) + "月" for i in df["月份"])
    plt.xticks(df["月份"], months)
    plt.xlim(1, 12)   # X轴标签范围为1-12
    plt.ylim(-5, 36)  # Y轴标签范围为-5到36
    plt.rcParams['axes.unicode_minus']=False
    plt.show()

def to_muti_gram(data, city_filter):

    # 构建数据
    x = np.arange(1, 13)
    y = data["降水量"]
    z = data["最大温度"]
    u = data["最小温度"]

    # 绘柱状图
    plt.bar(x=x, height=y, label='降水量', color='g', alpha=0.8)
    # 在左侧显示图例
    plt.legend(loc="upper left")

    # 设置标题
    plt.title(f"1981年-2010年（{city_filter}）月平均气温和降水")

    # 为两条坐标轴设置名称
    plt.xlabel("月份")
    plt.ylabel("降水（mm）")

    # 画折线图
    ax2 = plt.twinx()
    ax2.set_ylabel("温度(°C)")
    # 设置坐标轴范围
    ax2.set_ylim([0, 36]);
    plt.plot(x, z, "r", marker='.', ms=5, linewidth='1', label="平均最高气温")
    plt.plot(x, u, "b", marker='.', ms=5, linewidth='1', label="平均最低气温")
    # 显示数字
    for a, b in zip(x, z):
        plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=12)
    for a, b in zip(x, u):
        plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=12)
    # 在右侧显示图例
    plt.legend(loc="upper right")
    # plt.savefig("recall.jpg")

    # 显示x轴的刻标以及对应的标签
    months = (str(i)+"月" for i in df["月份"])
    plt.xticks(df["月份"], months)
    plt.xlim(1, 12)  # X轴标签范围为1-12
    plt.ylim(-5, 36)  # Y轴标签范围为-5到36
    plt.rcParams['axes.unicode_minus'] = False
    plt.show()

if __name__ == '__main__':
    # 设置全局字体样式
    font = {
        'family': 'SimHei'
    }
    plt.rc('font', **font)

    while True:
        # 加载数据
        o = open('NMC_Data.csv')
        df = pd.read_csv(o)
        # 过滤数据
        city = str(input("请输入被统计城市,按回车键执行："))
        df = df.filter(["时间段", "省份", "城市", "月份", "最大温度", "最小温度", "降水量"])
        df = df.query("时间段=='1981年-2010年'")
        if city != "全国":
            df = df.query(f"城市=='{city}'")
            if df is None or len(df) == 0:
                print("输入的数据有误，请重新输入！")
                continue
        # 分组聚合
        df = df.groupby(['月份']).agg({'最大温度': np.mean, '最小温度': np.mean, '降水量': np.sum})
        df = df.reset_index()
        # 绘制全国12个月累计降水量柱形图
        # to_barogram(df)
        # 绘制全国12个月平均最高温度、最小温度折线图
        # to_broken_line(df)
        to_muti_gram(df, city)
        y_or_n = input("Enter 'q' to quit and any key to continue: ")
        if y_or_n == 'q':  # 退出循环
            break