# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : MusicDownloadTool_orign.py
@Project: WebGrap1
@Time   : 2022-06-01 10:35:36
@Desc   : The file is download VIP music
@Version: v1.0
"""
import os
import re
import sys
import time
import urllib
from wcwidth import wcswidth
import requests
# from urllib import request,parse
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
# options.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
options.add_argument('Connection=keep-alive')
from selenium.webdriver.chrome.service import Service
# 导入显性等待的API需要的模块
# 1> 等待对象模块
from selenium.webdriver.support.wait import WebDriverWait
# 2> 导入等待条件模块
from selenium.webdriver.support import expected_conditions as EC
# 3> 导入查询元素模块
from selenium.webdriver.common.by import By
import execjs
import wget


def ui():
    # 搭建界面
    # 1.创建画布
    root = Tk()
    # 2.添加标题
    root.title('音乐下载器')
    # 3.设置窗口大小
    root.geometry('845x500+400+200')

    # 4.标签控件
    label = Label(root, text='请输入歌曲名称，按回车键查询：', font=('华文行楷', 20))
    # 5.定位
    label.grid()
    # 6.
    global entry
    entry = Entry(root, font=('隶书', 20))

    entry.bind("<Return>", searchMusicByName)

    # 7.定位
    entry.grid(row=0, column=1)
    # 单选按钮***
    var = StringVar()
    r1 = Radiobutton(root, text="网易云", variable=var, value='netease')
    # r1.place(x=50, y=35)
    # r1.pack() #添加顺序排列组件
    r1.grid(row=1, column=0, sticky=W, padx=5)
    r2 = Radiobutton(root, text="QQ", variable=var, value='qq', state='disabled')
    # r2.place(x=150, y=35)
    # r2.pack()
    r2.grid(row=1, column=0, sticky=W, padx=75)
    r3 = Radiobutton(root, text="酷狗", variable=var, value='kugou', state='disabled')
    r3.grid(row=1, column=0, sticky=W, padx=120)
    # r3.pack()
    # 榜单批量下载
    global Btn_NewSongs, Btn_TopSongs
    Btn_NewSongs = Button(root, text="新歌榜下载", fg="green", command=downloadMusic)
    Btn_NewSongs.grid(row=2, column=0, sticky=W, padx=5)
    Btn_NewSongs.setvar("url", newSongUrl)
    Btn_TopSongs = Button(root, text="飙升榜下载", fg="blue", command=downloadMusic)
    Btn_TopSongs.grid(row=2, column=0, sticky=W, padx=80)
    # Btn_TopSongs.columnconfigure(1, weight=1)
    Btn_TopSongs.setvar("url", topUrl)
    # r3.place(x=250, y=35)
    # 默认选中网易云
    var.set('netease')
    # 文本框
    global lb
    # text = Text(root, font=('楷书', 16), width=50, heigh=15)
    # text.grid(row=2, columnspan=2)
    # 8.列表框
    frame = ttk.Frame(root, padding=(3, 3, 12, 12))
    frame.grid(row=3, columnspan=4, sticky=(N, S, E, W))
    lb = Listbox(frame, font=('楷书', 16), width=75, heigh=15, selectmode=MULTIPLE)
    # 9.定位 columnspan 组件横跨的列数
    lb.grid(row=3, columnspan=4)
    # 点击下载按钮
    button = Button(root, text='开始下载', bg="#58e311", font=('隶书', 15), command=downloadMusicByID)
    # 定位 sticky 对齐方式 W E N S  东南西北
    button.grid(row=4, column=0, sticky=W, padx=5)
    button = Button(root, text='歌曲详情', bg="#FAA90E", font=('隶书', 15), command=music_detail)
    # 定位 sticky 对齐方式 W E N S  东南西北
    button.grid(row=4, column=0, sticky=W, padx=120)
    # 退出程序的按钮
    button1 = Button(root, text='退出程序', font=('隶书', 15), command=root.quit)
    # 定位 sticky 对齐方式 W E N S  东南西北
    button1.grid(row=4, column=1, sticky=E)

    # 显示界面
    root.mainloop()

def getDriver():
    if getattr(sys, 'frozen', False):
        # 从exe包里找chromedriver依赖驱动的情况
        # chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
        chromedriver_path = "chromedriver.exe"
        s = Service(chromedriver_path)
        driver = webdriver.Chrome(service=s, options=options)
    # else:
    #     # 普通情况下从本地文件路径找依赖的情况
    #     driver = webdriver.Chromedriver(executable_path='本地chromedriver的路径')
    return  driver

def getDriverHttp(url):
    driver.get(url)
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup


def getMusicList(url):
    data = {
        "params": "FA90hTqq2dU1fImQj0Z2s3qcLpYWE8p3UYXwt8yGJNBN7cEfX30GvZrhhQTrxeRbe1VmmXn7awsciPNsO0Ox1Y4CofPdsw2zDh8LeyhzmhY=",
        "encSecKey": "ae6867c764f4a73a76dae37547934fa713ca616fbc7ce4b07237a9ff7a4e3d846c6117449db548046c65b5bbb2eca5a58171734f64c27ea0312f3bf85e300a8cc9aeae52da7daa4af1148e8868382bae69e844d82b5659633cfcfd7f4a3f63853e0f79028c7e3cfafbf1be56bb28acf048c153a09b2f3d42814e09eb1b468e8b"
    }
    requests.post(url, headers=headers, data=data)
    soup = getDriverHttp(url)
    soup = soup.find_all('a', href=re.compile('^/song'))
    for i in soup:
        id = i.get("href")[9:]
        name = i.find_next("b").get("title")

        yield id, name


def searchMusic(id):
    # for song in req['result']['songs']:
    #     name = song["name"]
    #     id = song["id"]
    #     url1 = "http://music.163.com/song/media/outer/url?id={}.mp3".format(id)
    #     mp3 = requests.get(url1).content
    url_music = "http://music.163.com/song/media/outer/url?id={}.mp3".format(id)
    print(url_music)
    mp3 = requests.get(url_music, headers=headers).content
    return mp3


def getEncryptparams(id):
    encrypt_js = open('encrypt.js', 'r', encoding='utf-8').read()
    ctx = execjs.compile(encrypt_js)
    res = ctx.call('getEncrypt', id)
    data = {
        "params": res["encText"],
        "encSecKey": res["encSecKey"]
    }
    return data


def searchMusicByName(self):
    # url = r'https://music.163.com/weapi/cloudsearch/get/web?csrf_token=
    name = entry.get()
    url = r'https://music.163.com/#/search/m/?s=' + name
    driver.get(url)
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    soup = soup.find_all('a', href=re.compile('^/song'))
    lb.delete(0, END)
    padx = " " * 8
    title = f"|歌曲ID|    |歌曲名称|{padx}|演唱者|{padx}|专辑|{padx}       |时长|        详情\n"
    lb.insert(END, title)
    for i in soup:
        id = i.get("href")[9:]
        name = i.find_next("b").get("title")
        autor = i.find_parent("div").find_parent("div").find_parent("div").nextSibling.nextSibling.get_text("")
        album = i.find_parent("div").find_parent("div").find_parent("div").nextSibling.nextSibling.nextSibling.get_text(
            "")
        duration = i.find_parent("div").find_parent("div").find_parent(
            "div").nextSibling.nextSibling.nextSibling.nextSibling.get_text("")
        print(id, name, autor, album, duration)
        music_info = f"{id}\n{name}\n{autor}\n{album}\n{duration}"
        padx1 = " " * 2
        if len(id) < 10:
            id = id + (10 - len(id)) * " "
        if wcswidth(name) > 8:
            name = name[0:6] + "..."
        # else:
        #     name = name.ljust(14 - len(name), " ")
        if wcswidth(autor) > 8:
            autor = autor[0:6] + "..."
        if wcswidth(album) > 8:
            album = album[0:6] + "..."

        str = f"|{id}|{' ' * (8 - len(id))}|{name}|{' ' * (16 - wcswidth(name))}|{autor}|{' ' * (14 - wcswidth(autor))}|{album}|{' ' * (14 - wcswidth(album))}     |{duration}|\n    {music_info}"
        lb.insert(END, str)


def downloadMusicByID():
    try:
        list_msg = []
        for i in lb.curselection():
            rows = lb.get(i)
            id = rows.split("|")[1].rstrip()
            name = rows.split("|")[3]
            data = getEncryptparams(id)
            resp = requests.post(url=url_p, headers=headers, data=data).json()
            musicUrl = resp["data"][0]["url"]

            print(resp)

            if musicUrl is not None:
                try:
                    save_path = filedialog.askdirectory()
                    print(save_path)
                    urllib.request.urlretrieve(musicUrl, f'{save_path}/{name}.mp3')
                    print(name, '下载完成～～～')
                    list_msg.append(f"{name}:  下载完成～～～")
                except urllib.error.ContentTooShortError:
                    pass
            else:
                # lb.delete(0, END)
                # lb.insert(END, "获取不到URL，重新查询，并下载其他歌曲！!")
                messagebox.showinfo('消息框', '获取不到URL，请下载其他歌曲！')
                return
            time.sleep(3)
        lb.delete(0, END)
        for msg in list_msg:
            lb.insert(END, msg)
    except:
        # lb.delete(0, END)
        # lb.insert(END,"参数错误，无法下载！")
        messagebox.showerror('消息框', '参数错误，无法下载！')


def downloadMusic():
    lb.delete(0, END)

    url = Btn_NewSongs.getvar("url")
    if Btn_NewSongs.getvar("url") == "" or Btn_NewSongs.getvar("url") is None:
        url = Btn_TopSongs.getvar("url")
    items = getMusicList(url)
    js = open('encrypt.js', 'r', encoding='utf-8').read()
    ctx = execjs.compile(js)
    list = []
    save_path = filedialog.askdirectory()
    print(save_path)
    for id, name in items:
        if name is not None and len(name) > 0:
            if list.__contains__(id):
                continue
            list.append(id)
            print(id, name)
            res = ctx.call('getEncrypt', id)
            data = {
                "params": res["encText"],
                "encSecKey": res["encSecKey"]
            }
            resp = requests.post(url=url_p, headers=headers, data=data).json()
            musicUrl = resp["data"][0]["url"]
            print(resp)
            if musicUrl is not None:
                try:
                    urllib.request.urlretrieve(musicUrl, f'{save_path}/{name}.mp3')
                    print(name, '下载完成～～～')
                    lb.insert(END, f"{name}:  下载完成～～～")
                except urllib.error.ContentTooShortError:  # music_list = getMusicList(url)

                    continue
            time.sleep(3)
def music_detail():
    for i in lb.curselection():
        if len(lb.curselection()) > 1:
            messagebox.showwarning('消息框', "仅允许选中一条歌曲查看详情！")
            break
        rows = lb.get(i)
        music_info = rows.split("|")[-1]
        messagebox.showinfo('详情', music_info)
if __name__ == "__main__":
    # url = r"https://music.163.com/weapi/search/suggest/web?csrf_token="
    url = r"https://music.163.com/discover/toplist"
    url_p = r"https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
    newSongUrl = r"https://music.163.com/discover/toplist?id=3779629"  # 新歌榜
    topUrl = r"https://music.163.com/discover/toplist?id=19723756"  # 飙升榜
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }
    driver = getDriver()
    driver.get(url)
    driver.minimize_window()
    ui()
    if driver is not None:
        driver.quit()
