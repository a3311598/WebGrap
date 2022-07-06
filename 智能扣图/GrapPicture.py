# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : GrapPicture.py
@Project: WebGrap1
@Time   : 2022-06-12 20:18:40
@Desc   : The file is removed background of pictrue
@Version: v1.0
"""
import os
from removebg import RemoveBg


def rmbg(path):
    r = RemoveBg('jXYb1kkJDvTKX6LJrjHK8ox6', 'error.log')
    r.remove_background_from_img_file(path)
    print("移除图片背景成功！")
    os.system("pause")
if __name__ == "__main__":
    while True:
        try:
            pic_path = str(input("请选择图片本地路径,按回车键执行:"))
            rmbg(pic_path)
        except FileNotFoundError:
            print("图片路径不存在，请重新输入!")
            y_or_n = input("Enter 'q' to quit and any key to continue: ")
            if y_or_n == 'q':  # 退出循环
                break
