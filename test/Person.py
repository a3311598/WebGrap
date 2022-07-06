# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : Person.py
@Project: WebGrap1
@Time   : 2022-06-14 12:23:17
@Desc   : The file is ...
@Version: v1.0
"""
class Person:
    num = 0
    __weight = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name}在吃饭")
    def sleep(self):
        print(f"{self.name}在睡觉")
    @classmethod
    def show_person_num(cls):
        Person.num += 1
        print(f"已经创建了{cls.num}个人")

class Student(Person):
    def __init__(self, name, place):
        self.name = name
        self.place = place
    def eat(self):
        print(f"{self.name}在{self.place}地方吃饭")
    Person.show_person_num()

class Teacher(Person):
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def sleep(self):
        print(f"{self.name}住在{self.address}地方。")
        super().sleep()
    Person.show_person_num()

if __name__ == "__main__":
    s1 = Student("小明", "饭店")
    t1 = Teacher("老师", "无人问津的")
    s1.eat()
    t1.sleep()

