import requests
import re
import json
import pprint
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# 时间戳转换为日期
from selenium.webdriver.common.by import By


def timeToTime(comment_date):
    create_time = i["createTime"]
    timeArray = time.localtime(int(create_time))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

driver = webdriver.Chrome()
driver.get('https://www.douyin.com/user/MS4wLjABAAAALOX4oB6bTBYYyPWW3OASbq7u51ha9zlcdB09d3b8NBk?relation=0')
lis = driver.find_elements(By.CSS_SELECTOR, '.ECMy_Zdt')
print(lis)
for li in lis:
    # url = li.find_elements(By.CSS_SELECTOR, 'a').get_attribute('href')
    url = li.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')


    # url = 'https://www.douyin.com/video/7081188549869063461'

    headers = {
        'cookie': '__ac_nonce=062bc0e28006de042d0a0; __ac_signature=_02B4Z6wo00f01RgPWigAAIDBmA2gaapZyrkYL16AACTCe8; ttwid=1|3hVua9uEMhqi6diQ7pN_BYQbMhASIcjjl3-bcGhWW3Q|1656491561|d6b6441657d6f56c73da17cc581d2ed391972be0ccd7fadea8ce53bc3d807cbb; strategyABtestKey=1656491563.119; s_v_web_id=verify_l4zcb2fr_8VqnNdn8_IXwn_46n6_9101_8krco0nXoTpl; passport_csrf_token=0fca02fc2d11dcf1be9f043f2646b02b; passport_csrf_token_default=0fca02fc2d11dcf1be9f043f2646b02b; AB_LOGIN_GUIDE_TIMESTAMP="1656491562928"; AVATAR_LOGIN_GUIDE_COUNT="1"; ttcid=718626ef66cd494f821b23994676df3512; AVATAR_FULL_LOGIN_GUIDE_ITA_TIMESTAMP="1656491562929"; AVATAR_FULL_LOGIN_GUIDE_ITA_COUNT="1"; pwa_guide_count="1"; n_mh=oyX1dMINTE3eG_2t7gedeaciels_D6rk52Sq1rVEN_A; sso_uid_tt=b6c4cb83ff6d3171660ba4051c497ec8; sso_uid_tt_ss=b6c4cb83ff6d3171660ba4051c497ec8; toutiao_sso_user=eb015d371897e8766ca12a53c479557d; toutiao_sso_user_ss=eb015d371897e8766ca12a53c479557d; uid_tt=b6c4cb83ff6d3171660ba4051c497ec8; uid_tt_ss=b6c4cb83ff6d3171660ba4051c497ec8; sid_tt=eb015d371897e8766ca12a53c479557d; sessionid=eb015d371897e8766ca12a53c479557d; sessionid_ss=eb015d371897e8766ca12a53c479557d; sid_ucp_sso_v1=1.0.0-KDQ5ZjIxZTNhMzZhYjI5MmE5N2U0OWM4NzY3MThjMjdhMDFjOTcyNmIKHQjzxrLK5QIQjp3wlQYY7zEgDDDAhN3VBTgGQPQHGgJsZiIgZWIwMTVkMzcxODk3ZTg3NjZjYTEyYTUzYzQ3OTU1N2Q; ssid_ucp_sso_v1=1.0.0-KDQ5ZjIxZTNhMzZhYjI5MmE5N2U0OWM4NzY3MThjMjdhMDFjOTcyNmIKHQjzxrLK5QIQjp3wlQYY7zEgDDDAhN3VBTgGQPQHGgJsZiIgZWIwMTVkMzcxODk3ZTg3NjZjYTEyYTUzYzQ3OTU1N2Q; msToken=meHg-cfuWA4MKY-37JWSzgCJXYuguay-kC5ka0AM0HvnYPozdqSV1aFfCFL-1mK2deP6CIjJSOQfoH0aZ-YN3kSqV6opZP1Ym8WhwcpZ4JU_wr51IjbcEQ==; odin_tt=322b67faad06084266ce52b388bbdf0a1efcad1f0939b24d82a1896185ca16c1cc606168344cbc10ce197bc1f214509b; sid_guard=eb015d371897e8766ca12a53c479557d|1656491663|5184000|Sun,+28-Aug-2022+08:34:23+GMT; sid_ucp_v1=1.0.0-KDc4NmZlYjA4MTg0ODEwNTBjYzYwY2ZkMmZjYWUyNWJiNGM4NDBkMDcKHQjzxrLK5QIQj53wlQYY7zEgDDDAhN3VBTgGQPQHGgJsZiIgZWIwMTVkMzcxODk3ZTg3NjZjYTEyYTUzYzQ3OTU1N2Q; ssid_ucp_v1=1.0.0-KDc4NmZlYjA4MTg0ODEwNTBjYzYwY2ZkMmZjYWUyNWJiNGM4NDBkMDcKHQjzxrLK5QIQj53wlQYY7zEgDDDAhN3VBTgGQPQHGgJsZiIgZWIwMTVkMzcxODk3ZTg3NjZjYTEyYTUzYzQ3OTU1N2Q; msToken=1SGuuIVq4FnurrLOvxAQykWhp5IhakYOoJcpaYYjSSgcKkjQMXjtt_vFBkrRDhoUSRkCPSh21Uwx3TJPsdoBU9gMHD7Z824-vSSjd5zJur98MhoqYAyQEg==; tt_scid=Ru80d2eeSgs20PtdFkaFDffL-hm4hlrdwYdC5UoedBG7l9EWo6FAAJFYwDYE8lWD2d62; THEME_STAY_TIME="145660"; home_can_add_dy_2_desktop="0"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    response = requests.get(url=url, headers=headers)

    print(response)  # <Response [200]>

    # print(response.text)

    # 获取html内容
    html_data = re.findall('type="application/json">(.*?)</script>', response.text)[0]

    # urldecode解码
    html_data = requests.utils.unquote(html_data)

    """
    或者使用此函数
    html_data_decode = parse.unquote(html_data)
    
    html_data = json.loads(html_data_decode)
    """
    # print(html_data)
    # 转换为json字典数据
    json_data = json.loads(html_data)
    # print(json_data)

    # 格式化打印json字典数据
    pprint.pprint(json_data)

    # 账号部分
    # 获取账号名称
    acoount_name = re.findall('<div class="yy223mQ8"><span class="Nu66P_ba"><span><span><span><span>(.*?)</span>', response.text)[0]
    print(acoount_name)

    # 获取账号粉丝数
    account_fan = re.findall('<span class="qvmsOheY">粉丝</span><span class="EobDY8fd">(.*?)</span>', response.text)[0]
    print(account_fan)

    # 视频部分
    # 获取视频标题
    video_title = re.findall('<title data-react-helmet="true">(.*?)</title>', response.text)[0]
    print(video_title)

    # 获取视频链接
    video_url = 'https:' + json_data['74']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0]['src']
    print(video_url)

    # 视频发布时间
    video_date = re.findall('发布时间：<!-- -->(.*?)</span>', response.text)[0]
    print(video_date)

    # 视频点赞评论转发数
    video_diggCount = re.findall('<span class="CE7XkkTw">(.*?)</span>', response.text)[0]   # 视频点赞
    video_commentCount = re.findall('<span class="CE7XkkTw">(.*?)</span>', response.text)[1]    # 视频评论
    video_shareCount = re.findall('<span class="CE7XkkTw">(.*?)</span>', response.text)[2]  # 视频转发

    print(video_diggCount, video_commentCount, video_shareCount)

    # 评论部分
    for i in json_data['74']['comment']['comments']:
        comment_nickname = i['user']['nickname']  # 用户昵称
        comment_text = i['text']  # 评论内容
        comment_date = timeToTime(i["createTime"])  # 评论时间
        comment_diggCount = i['diggCount']  # 点赞数
        print(comment_nickname, comment_text, comment_date, comment_diggCount)
    # 保存视频
    video_content = requests.get(url=video_url, headers=headers).content
    with open('video\\' + video_title + '.mp4', mode='wb') as f:
        f.write(video_content)
