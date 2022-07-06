# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : GrapBlibliVedio.py
@Project: WebGrap1
@Time   : 2022-06-13 20:17:32
@Desc   : The file is ...
@Version: v1.0
"""
import you_get
import sys




def getVedio(url):
    save_path = r"E:\vedio"
    sys.argv = ['you-get', '-o', save_path, url]
    you_get.main()


if __name__ == "__main__":
    url = 'https://tts.tmooc.cn/video/showVideo?menuId=773518&version=TSDTN202107'
    # url = "https://jx.parwix.com:4433/player/analysis.php?v=https://www.bilibili.com/bangumi/play/ep343154?from_spmid=666.25.episode.0"
    getVedio(url)

