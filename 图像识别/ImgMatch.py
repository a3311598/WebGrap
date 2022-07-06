# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : ImgMatch.py
@Project: WebGrap1
@Time   : 2022-06-12 22:03:07
@Desc   : The file is ...
@Version: v1.0
"""
import time

import numpy as np
import cv2

# 相关系数匹配方法: cv2.TM_CCOEFF
import pyautogui
from matplotlib import pyplot as plt
# from pygments.formatters import img

# template = "_20220613033552.jpg"
# template1 = "_20220613033724.jpg"
# img = "_20220613034352.png"
rows = []
with open(r"D:\Program Files\SoftWare\木头超级字典生成器 V6.20\mutou.txt", "r") as f:
    rows = f.read().splitlines()

for r in rows:
    pyautogui.click(x=1330, y=475)
    pyautogui.click(x=1245, y=475)
    pyautogui.typewrite(r)
    pyautogui.doubleClick(x=1275, y=530, duration=0.2)
    time.sleep(1)
    pyautogui.screenshot(r'img_screenshot.png', region=(1415, 520, 204, 56))
    img_rgb = cv2.imread('_20220613052224.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # template = cv2.imread('_20220613035243.png', 0)
    template = cv2.imread('img_screenshot.png', 0)

    # template = pyautogui.screenshot(region=[1415, 520, 40, 40])
    # template = cv2.cvtColor(np.asarray(template), cv2.COLOR_RGB2BGR)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF)
    h, w = template.shape[:2]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    # 取匹配程度大于%80的坐标
    if res.max() >= threshold:
        print("匹配成功")
        break
# loc = np.where(res >= threshold)
#np.where返回的坐标值(x,y)是(h,w)，注意h,w的顺序
# for pt in zip(*loc[::-1]):
#     bottom_right = (pt[0] + w, pt[1] + h)
#     cv2.rectangle(img_rgb, pt, bottom_right, (0, 0, 255), 2)
# cv2.imwrite("img.jpg",img_rgb)
# cv2.imshow('img', img_rgb)
# cv2.waitKey(0)



# plt.subplot(122), plt.imshow(img_gray, cmap='gray')
# plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
# plt.show()