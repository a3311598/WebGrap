# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : DataToNeo4jClass.py
@Project: WebGrap1
@Time   : 2022-06-22 18:51:30
@Desc   : The file is ...
@Version: v1.0
"""
# -*- coding: utf-8 -*-
from py2neo import Node, Graph, Relationship, NodeMatcher


class DataToNeo4j(object):
    """将excel中数据存入neo4j"""

    def __init__(self):
        """建立连接"""
        # self.g = Graph("http://localhost:7474/browser/", auth=("neo4j", "3322996"))
        # link = Graph("http://localhost:7474", username="neo4j", password="3322996")
        link = Graph("http://localhost:7474/browser/", auth=("neo4j", "3322996"))
        self.graph = link
        # self.graph = NodeMatcher(link)
        # 定义label
        self.service = 'service'
        self.func = 'func'
        self.module = 'module'
        self.graph.delete_all()
        self.matcher = NodeMatcher(link)

        """
        node3 = Node('animal' , name = 'cat')
        node4 = Node('animal' , name = 'dog')  
        node2 = Node('Person' , name = 'Alice')
        node1 = Node('Person' , name = 'Bob')  
        r1 = Relationship(node2 , 'know' , node1)    
        r2 = Relationship(node1 , 'know' , node3) 
        r3 = Relationship(node2 , 'has' , node3) 
        r4 = Relationship(node4 , 'has' , node2)    
        self.graph.create(node1)
        self.graph.create(node2)
        self.graph.create(node3)
        self.graph.create(node4)
        self.graph.create(r1)
        self.graph.create(r2)
        self.graph.create(r3)
        self.graph.create(r4)
        """

    def create_node(self, node_service_key, node_func_key, node_module_key):
        """建立节点"""
        # , node_module_key
        for name in node_service_key:
            service_node = Node(self.service, name=name)
            self.graph.create(service_node)
        for name1 in node_func_key:
            func_node = Node(self.func, name=name1)
            self.graph.create(func_node)
        for name2 in node_module_key:
            module_node = Node(self.module, name=name2)
            self.graph.create(module_node)

    def create_relation(self, df_data):
        """建立联系"""
        m = 0
        for m in range(0, len(df_data)):
            try:
                print(list(self.matcher.match(self.service).where("_.name=" + "'" + df_data['service'][m] + "'")))
                print(list(self.matcher.match(self.func).where("_.name=" + "'" + df_data['func'][m] + "'")))
                print(list(self.matcher.match(self.module).where("_.name=" + "'" + df_data['module'][m] + "'")))
                rel = Relationship(
                    self.matcher.match(self.service).where("_.name=" + "'" + df_data['service'][m] + "'").first(),
                    "belong to",
                    self.matcher.match(self.func).where("_.name=" + "'" + df_data['func'][m] + "'").first())
                rel1 = Relationship(
                    self.matcher.match(self.func).where("_.name=" + "'" + df_data['func'][m] + "'").first(),
                    "belong to",
                    self.matcher.match(self.module).where("_.name=" + "'" + df_data['module'][m] + "'").first())

                self.graph.create(rel, rel1)
            except AttributeError as e:
                print(e, m)
