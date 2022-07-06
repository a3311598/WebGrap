# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : MusicDownloadTool_orign.py
@Project: WebGrap1
@Time   : 2022-06-01 10:35:36
@Desc   : The file is download VIP music
@Version: v1.0
"""
import asyncio
import re
import this
import time
import urllib
import requests
from urllib3.exceptions import InsecureRequestWarning


import execjs
import logging
from urllib3 import PoolManager
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from bs4 import BeautifulSoup
from wcwidth import wcswidth

# ico图标转换网址 https://convertico.com/#


def ui():
    # 搭建界面
    # 1.创建画布
    root = Tk()
    # 2.添加标题
    root.title('音乐下载器')
    root.iconbitmap('./logo.ico')
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
    r1.grid(row=1, column=0, sticky=W, padx=5)
    r2 = Radiobutton(root, text="QQ", variable=var, value='qq', state='disabled')
    r2.grid(row=1, column=0, sticky=W, padx=75)
    r3 = Radiobutton(root, text="酷狗", variable=var, value='kugou', state='disabled')
    r3.grid(row=1, column=0, sticky=W, padx=120)
    # 榜单批量下载
    global Btn_NewSongs, Btn_TopSongs
    Btn_NewSongs = Button(root, text="新歌榜下载", fg="green", command=downloadMusic)
    Btn_NewSongs.grid(row=2, column=0, sticky=W, padx=5)
    Btn_NewSongs.setvar("newSongUrl", newSongUrl)
    Btn_TopSongs = Button(root, text="飙升榜下载", fg="blue", command=downloadMusic)
    Btn_TopSongs.grid(row=2, column=0, sticky=W, padx=80)
    Btn_TopSongs.setvar("topUrl", topUrl)
    # 默认选中网易云
    var.set('netease')
    # 文本框
    global lb
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


def searchMusic(id):
    url_music = "http://music.163.com/song/media/outer/url?id={}.mp3".format(id)
    print(url_music)
    mp3 = requests.get(url_music, headers=headers,verify=False).content
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


def getEncryptparamsByName(keyword):
    encrypt_js = open('encrypt.js', 'r', encoding='utf-8').read()
    ctx = execjs.compile(encrypt_js)
    res = ctx.call('getEncryptByName', keyword)
    data = {
        "params": res["encText"],
        "encSecKey": res["encSecKey"]
    }
    return data


def getMusicList(url):
    resp = requests.get(url, headers=headers,verify=False).content
    html = BeautifulSoup(resp, features="html5lib")
    soup = html.find_all('a', href=re.compile('^/song'))
    for i in soup:
        id = i.get("href")[9:]
        name = i.get_text()
        # print(id, name)
        yield id, name


def searchMusicByName(self):
    name = entry.get()
    url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    time.sleep(3)
    data = getEncryptparamsByName(name)
    resp = requests.post(url, headers=headers, data=data,verify=False).json()

    songs = resp['result']["songs"]

    lb.delete(0, END)
    padx = " " * 8
    title = f"|歌曲ID|    |歌曲名称|{padx}|演唱者|{padx}|专辑|{padx}       |时长|        详情\n"
    lb.insert(END, title)
    for s in songs:
        id = str(s["id"])
        name = s["name"]
        autor = s["ar"][0]["name"]
        album = s["al"]["name"]
        duration = time.strftime('%M:%S', time.gmtime(int(s["dt"])/1000))

        # print(id, name, autor, album, duration)
        music_info = f"{id}\n{name}\n{autor}\n{album}\n{duration}"
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

        songs = f"|{id}|{' ' * (8 - len(id))}|{name}|{' ' * (16 - wcswidth(name))}|{autor}|{' ' * (14 - wcswidth(autor))}|{album}|{' ' * (14 - wcswidth(album))}     |{duration}|\n    {music_info}"
        lb.insert(END, songs)


def downloadMusicByID():
    try:
        list_msg = []
        save_path = filedialog.askdirectory()
        for i in lb.curselection():
            rows = lb.get(i)
            id = rows.split("|")[1].rstrip()
            name = rows.split("|")[3]
            data = getEncryptparams(id)
            resp = requests.post(url=url_p, headers=headers, data=data,verify=False).json()
            musicUrl = resp["data"][0]["url"]

            # print(resp)

            if musicUrl is not None:
                try:
                    # print(save_path)
                    urllib.request.urlretrieve(musicUrl, f'{save_path}/{name}.mp3')
                    # print(name, '下载完成～～～')
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
    url = Btn_NewSongs.getvar("newSongUrl")
    if Btn_NewSongs.getvar("newSongUrl") == "" or Btn_NewSongs.getvar("newSongUrl") is None:
        url = Btn_TopSongs.getvar("topUrl")
    os.environ['NO_PROXY'] = url
    items = getMusicList(url)
    list = []
    save_path = filedialog.askdirectory()
    for id, name in items:
        if name is not None and len(name) > 0:
            if list.__contains__(id):
                continue
            list.append(id)
            data = getEncryptparams(id)
            resp = requests.post(url=url_p, headers=headers, data=data,verify=False).json()
            musicUrl = resp["data"][0]["url"]
            # print(resp)
            if musicUrl is not None:
                try:
                    urllib.request.urlretrieve(musicUrl, f'{save_path}/{name}.mp3')
                    print(name, '下载完成～～～')
                    time.sleep(3)
                    lb.insert(END, f"{name}:  下载完成～～～")
                except urllib.error.ContentTooShortError:  # music_list = getMusicList(url)
                    continue

def music_detail():
    for i in lb.curselection():
        if len(lb.curselection()) > 1:
            messagebox.showwarning('消息框', "仅允许选中一条歌曲查看详情！")
            break
        rows = lb.get(i)
        music_info = rows.split("|")[-1]
        messagebox.showinfo('详情', music_info)

if __name__ == "__main__":
    # http = PoolManager()
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    proxies = {
        'http': '47.106.105.236',
        'http': '202.55.5.209',
        'http': '183.247.199.114',
        'http': '183.247.211.50',
        'http': '122.9.101.6',
        'http': '183.247.215.218',
        'http': '60.170.204.30',
    }

    url = r"http://music.163.com/discover/toplist"
    url_p = r"http://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
    newSongID = "3779629"  # 新歌榜
    newSongUrl = f'{url}?id={newSongID}'
    topID = r"19723756"  # 飙升榜
    topUrl = f'{url}?id={topID}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
        'content-type': 'application/x-www-form-urlencoded'
    }
    logging.basicConfig(filename='../LOG.log',
                        format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.INFO,
                        filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
    try:
        ui()
    except Exception as result:
        logging.info(result)
