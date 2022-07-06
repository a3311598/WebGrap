# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : DataToNeo4jClass1.py
@Project: WebGrap1
@Time   : 2022-06-22 15:45:39
@Desc   : The file is ...
@Version: v1.0
"""
# -*- coding: utf-8 -*-
from py2neo import Node, Graph, Relationship


class DataToNeo4j(object):
    """将excel中数据存入neo4j"""

    # 初始化
    def __init__(self):
        """建立连接"""
        # link = Graph("http://localhost:7474", username="neo4j", password="3322996")
        link = Graph("http://localhost:7474/browser/", auth=("neo4j", "3322996"))
        self.graph = link
        # 定义label
        self.invoice_name = '名称'
        self.invoice_value = '值'
        self.graph.delete_all()  # 从中删除所有节点和关系Graph。

    # 创建实体(节点)
    def create_node(self, node_list_key, node_list_value):
        """建立节点"""
        for name in node_list_key:
            name_node = Node(self.invoice_name, name=name)
            self.graph.create(name_node)
        for name in node_list_value:
            value_node = Node(self.invoice_value, name=name)
            self.graph.create(value_node)  #建立实体

    # 创建关系  df_data 就是实体1——关系——实体2的DataFrame
    def create_relation(self, df_data):
        """建立联系"""

        m = 0
        for m in range(0, len(df_data)):
            try:
                #实体——关系——实体
                # user = graph.nodes.match("User", self.username).first()
                # rel = Relationship(self.graph.match(label=self.invoice_name, property_key='name',
                #                                        property_value=df_data['name'][m]),
                #                    df_data['relation'][m],
                #                    self.graph.match(label=self.invoice_value, property_key='name',
                #                                        property_value=df_data['name2'][m])).first()

                rel = Relationship(self.graph.find_one(label=self.invoice_name, property_key='name',
                                                       property_value=df_data['name'][m]),
                                   df_data['relation'][m],
                                   self.graph.find_one(label=self.invoice_value, property_key='name',
                                                       property_value=df_data['name2'][m]))
                self.graph.create(rel) #建立关系
            except AttributeError as e:
                print(e, m)

