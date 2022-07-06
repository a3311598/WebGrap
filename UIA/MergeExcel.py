# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : MergeExcel.py
@Project: WebGrap1
@Time   : 2022-06-19 14:02:43
@Desc   : The file is ...
@Version: v1.0
"""
import pandas as pd
import os

Folder_Path = r'D:\code\WebGrap1\UIA\mergetest'  # 要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path = r'D:\code\WebGrap1\UIA\test'  # 拼接后要保存的文件路径
SaveFile_Name = r'all.xlsx'  # 合并后要保存的文件名

# 修改当前工作目录
os.chdir(Folder_Path)
# 将该文件夹下的所有文件名存入一个列表
file_list = os.listdir()

# 读取第一个Excel文件并包含表头
df = pd.read_excel(Folder_Path + '\\' + file_list[0])  # 编码默认UTF-8，若乱码自行更改

# 循环遍历列表中各个Excel文件名，并追加到合并后的文件
# columns = ["Name", "Acronym", "Founded", "City HQ", "Country/Territory HQ", "Type I", "Type II", "UIA Org ID"]
# df_res = pd.DataFrame([], columns=columns)
save_path = SaveFile_Path + '\\' + SaveFile_Name

for i in range(1, len(file_list)):
    filename = Folder_Path + '\\' + file_list[i]
    df_temp = pd.read_excel(filename)
    df = pd.concat([df, df_temp])
df.to_excel(save_path, sheet_name="Sheet1")

