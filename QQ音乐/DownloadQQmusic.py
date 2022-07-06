# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : test.py
@Project: WebGrap1
@Time   : 2022-05-27 00:31:39
@Desc   : The file is downloaded QQ Music
@Version: v1.0
"""
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('Connection=keep-alive')
from selenium.webdriver.chrome.service import Service
import requests
import wget

def dowload(url):
    # 请求url地址
    # url = 'https://dl.stream.qqmusic.qq.com/RS020647JhcU1kN0iF.mp3?guid=1466879566&vkey=3A91F1F9C157F0E5522CB5D68278C98510B50ACD78F976EC4F05BD67AEBB21904B37F8488A6ADF34FFAB69E512CF5A4313D6BF1DF8BDEFBA&uin=&fromtag=120002'
    # 请求头设置代理
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.13 Safari/537.36'}
    # 发起请求
    req = requests.get(url=url,headers=headers, verify=False)
    # 保存路径
    save_path = r'E:/music'
    print(url)
    # 下载
    wget.download(url, save_path) #or urllib.request.urlretrieve(url,save_path)
    # search = 'https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?key=%E5%91%A8%E6%9D%B0%E4%BC%A6'
    search = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=10&w=林俊杰'

def searchMusicByName():
    pass

if __name__ == '__main__':
    s = Service(r"C:\Users\GAVX\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    url = 'http://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=10&w=桥边姑娘'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}

    resp = requests.get(url)
    orign_str = resp.text
    json_str = orign_str[9:-1]
    dic = eval(json_str)
    songs = dic['data']['song']['list']
    driver.get("https://y.qq.com/")
    js_str = open('./encrypt.js','r',encoding='utf-8').read().strip()
    sign = driver.execute_script(js_str)
    print(sign)
    pass
    print(songs)
    for song in songs:
        songmid = song['songmid']
        songname = song['songname']
        singer_name = song['singer'][0]['name']
        albumname = song['albumname']

        print(albumname)
        if songmid == '001aKaqX36nWoC':
            # guid1 = 3263266218
            guid1 = 1177541064
            # guid2 = 907733300
            guid2 = 5757550948
            # sign = "zzbcc04691d5qksosmxcov2kgj43q530af4f82d71"
            sign = "zzba82c76f0grfs5jh5ibu85sa5ycybq2aa9e2a9"
            uin = 799129490
            # albumMid = "0037Yq3H3RznaX"
            albumMid = "0005lSRL2PyXVp"
            # g_tk_new = 946290626
            g_tk_new = 1948303673
            # g_tk = 946290626
            g_tk = 1948303673
            # biz_id = 244625442
            biz_id = 250633820
            # songmids = ["001zLvbN1NYMuv","004DXFlC0nsTCZ"]
            songmids = '["'+songmid+'","001zLvbN1NYMuv","004DXFlC0nsTCZ"]'
            # songtype = [0,0]
            songtype = '[0,0,0]'
            # v_songmid = ["001zLvbN1NYMuv", "000NqZLy2lfXjT", "004DXFlC0nsTCZ", "001bo9Wy1NfHpb"]
            v_songMid = '["'+songmid+'","001zLvbN1NYMuv","000NqZLy2lfXjT","004DXFlC0nsTCZ","001bo9Wy1NfHpb"]'
            data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":799129490,"g_tk_new_20200303":'+str(g_tk)+',"g_tk":'+str(g_tk)+'},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["'+str(uin)+'"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["'+str(uin)+'"]}},"req_3":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"'+str(guid1)+'","songmid":'+songmids+',"songtype":'+songtype+',"uin":"'+str(uin)+'","loginflag":1,"platform":"20"}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":'+str(v_songMid)+'}},"req_5":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"'+str(biz_id)+'","biz_sub_type":0}]}},"req_6":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"'+albumMid+'"}},"req_7":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"'+str(guid2)+'","songmid":["'+songmid+'"],"songtype":[0],"uin":"'+str(uin)+'","loginflag":1,"platform":"20"}}}'
            print(data)
            # data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":799129490,"g_tk_new_20200303":2136651788,"g_tk":2136651788},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["799129490"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["799129490"]}},"req_3":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"9824529208","songmid":["004DXFlC0nsTCZ"],"songtype":[0],"uin":"799129490","loginflag":1,"platform":"20"}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["000NqZLy2lfXjT","004DXFlC0nsTCZ","001bo9Wy1NfHpb"]}},"req_5":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"218224537","biz_sub_type":0}]}},"req_6":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"004QnEHc3zjC7J"}},"req_7":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":'+guid+',"songmid":['+songmid+'],"songtype":[0],"uin":"799129490","loginflag":1,"platform":"20"}}}'
            url_1 = f'http://u.y.qq.com/cgi-bin/musics.fcg?sign={sign}'
            resp1 = requests.post(url_1, headers=headers, data=data, verify=False).json()
            purl = resp1["req_7"]["data"]["midurlinfo"][0]["purl"]
            music_url = 'http://dl.stream.qqmusic.qq.com/' + purl
            dowload(music_url)
            break
    #     # https://dl.stream.qqmusic.qq.com/RS020647JhcU1kN0iF.mp3?guid=1466879566&vkey=3A91F1F9C157F0E5522CB5D68278C98510B50ACD78F976EC4F05BD67AEBB21904B37F8488A6ADF34FFAB69E512CF5A4313D6BF1DF8BDEFBA&uin=&fromtag=120002
    #     # url_1 = 'https://c.y.qq.com/fcgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","filename":"M800","param":{"guid":"8846039534","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer",""method":"CgiGetVkey","filename":"M800","param":{"guid":"8846039534","songmid"["%s"],"songtype":[0],"uin":"1152921504784213523","loginflag":1,"platform":"20"}},"comm":{"uin":"1152921504784213523","format":"json","ct":24,"cv":0}}' % songmid
    #     data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":799129490,"g_tk_new_20200303":2136651788,"g_tk":2136651788},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["799129490"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["799129490"]}},"req_3":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"9824529208","songmid":["004DXFlC0nsTCZ"],"songtype":[0],"uin":"799129490","loginflag":1,"platform":"20"}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["000NqZLy2lfXjT","004DXFlC0nsTCZ","001bo9Wy1NfHpb"]}},"req_5":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"218224537","biz_sub_type":0}]}},"req_6":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"004QnEHc3zjC7J"}},"req_7":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"1070629287","songmid":["004DXFlC0nsTCZ"],"songtype":[0],"uin":"799129490","loginflag":1,"platform":"20"}}}'
    #     url_1 = 'https://u.y.qq.com/cgi-bin/musics.fcg?_=1654990352670&sign=zzb458b10d2ocnewtoqpwdipqh9fixkwfbaae559'
    #     resp1 = requests.post(url_1, headers=headers, data=data).json()

        # purl = requests.get(url_1,headers=headers).json()['req_0']['data']['midurlinfo'][0]['purl']
        # music_url = 'https://dl.stream.qqmusic.qq.com/'+purl
        # print(requests.get(url_1,headers=headers).json())
        # music_data = requests.get(music_url).content
        # with open(f'歌曲下載/{songname}--{singer_name}.mp3',mode='wb') as f:
        #     f.write(music_data)
        # print(f'正在下载:{songname}--{singer_name}')
    # dowload()