# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : invoice_neo4j.py
@Project: WebGrap1
@Time   : 2022-06-22 15:46:19
@Desc   : The file is ...
@Version: v1.0
"""
# -*- coding: utf-8 -*-
from DataToNeo4jClass import DataToNeo4j
import os
import pandas as pd


# 提取excel表格中数据，将其转换成dateframe类型
os.chdir('D:\\Example\\neo4j-python-pandas-py2neo-v3-master\\data')

#invoice_data = pd.read_excel('./Invoice_data_Demo.xls', header=0, encoding='utf8')
invoice_data = pd.read_excel('./Invoice_data_Demo.xls', header=0, encoding='utf8')
print(invoice_data)

#实体1放入一个列表中，实体2放入一个列表中
def data_extraction():
    """节点数据抽取"""

    # 取出名称到list
    node_list_key = []
    for i in range(0, len(invoice_data)):
        node_list_key.append(invoice_data['题名'][i])

    # 去除重复的名称
    node_list_key = list(set(node_list_key))

    # value抽出作node
    node_list_value = []
    for i in range(0, len(invoice_data)):
        for n in range(1, len(invoice_data.columns)):
            # 取出表头名称invoice_data.columns[i]  ,取出第一列第一行，第二列第一行....
            node_list_value.append(invoice_data[invoice_data.columns[n]][i])
    # 去重
    node_list_value = list(set(node_list_value))
    # 将list中浮点及整数类型全部转成string类型
    node_list_value = [str(i) for i in node_list_value]
    # print(node_list_value)
    return node_list_key, node_list_value

#建立成实体1——关系——实体2的DataFrame的表形式
def relation_extraction():
    """联系数据抽取"""

    links_dict = {}   # 存放下面三个
    name_list = []     # 存放实体
    relation_list = [] # 存放关系
    name2_list = []    # 存放实体

    for i in range(0, len(invoice_data)):
        m = 0
        name_node = invoice_data[invoice_data.columns[m]][i]
        while m < len(invoice_data.columns)-1:
            relation_list.append(invoice_data.columns[m+1])  # 存放列名称
            name2_list.append(invoice_data[invoice_data.columns[m+1]][i])
            name_list.append(name_node)
            m += 1

    # 将数据中int类型全部转成string
    name_list = [str(i) for i in name_list]
    name2_list = [str(i) for i in name2_list]

    # 整合数据，将三个list整合成一个dict
    links_dict['name'] = name_list   #实体
    links_dict['relation'] = relation_list  #关系(存放列名)
    links_dict['name2'] = name2_list   #实体
    # 将数据转成DataFrame
    df_data = pd.DataFrame(links_dict)
    return df_data


# 实例化对象
data_extraction()
relation_extraction()
create_data = DataToNeo4j()

create_data.create_node(data_extraction()[0], data_extraction()[1])  # 创建第一个实体和第二个实体
create_data.create_relation(relation_extraction())  # 建立关系
print(relation_extraction())

