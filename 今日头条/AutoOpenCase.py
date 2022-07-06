import pyautogui
import time
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler(timezone="Asia/Shanghai")
# currentMouseX, currentMouseY = pyautogui.position() # 鼠标当前位置
# print(currentMouseX, currentMouseY)


# 获取鼠标位置
def get_mouse_positon():
    time.sleep(5)  # 准备时间
    print('开始获取鼠标位置')
    try:
        for i in range(10):
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            positionStr = '鼠标坐标点（X,Y）为：{},{}'.format(str(x).rjust(4), str(y).rjust(4))
            pix = pyautogui.screenshot().getpixel((x, y))  # 获取鼠标所在屏幕点的RGB颜色
            positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
                3) + ')'
            print(positionStr)
            time.sleep(0.5)  # 停顿时间
    except:
        print('获取鼠标位置失败')
# 鼠标坐标点（X,Y）为：1817, 943 RGB:(235, 99,  0)

def click_job():
    start_time = time.time()
    # 获得文件图片在现在的屏幕上面的坐标，返回的是一个元组(top, left, width, height)
    # 如果截图没找到，pyautogui.locateOnScreen()函数返回None
    pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot1.png', region=(1075, 945, 111, 22))
    a = pyautogui.locateOnScreen(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot.png')
    a1 = pyautogui.locateOnScreen(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot1.png')
    if a is not None or a1 is not None:
        pyautogui.click(x=1141, y=956, duration=1)
        pyautogui.click(x=991, y=713, duration=2)
        time.sleep(15)
        pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Picturereenshot_close.png', region=(1819, 52, 32, 18))
        # b = pyautogui.locateOnScreen(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_close.png')

        # c = pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_read.png')
        # d = pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_back.png')
        # e = pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_task.png')
        for i in range(0,20):
            a2 = pyautogui.locateOnScreen(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot1.png')
            f = pyautogui.locateOnScreen(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_backgroud.png')
            f1 = pyautogui.locateOnScreen(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_backgroud1.png')
            pyautogui.click(x=1190, y=62, duration=1)
            # b = pyautogui.locateOnScreen(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_close.png')
            # pix = pyautogui.screenshot().getpixel((1830, 61))  # 获取坐标(220,200)所在屏幕点的RGB颜色
            # positionStr = 'RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
            #     3) + ')'
            # if b is not None or positionStr == 'RGB:(242,247,248)':
            pyautogui.click(x=994, y=582, duration=1)
            time.sleep(15)
            if a2 is not None:
                break
            # print(positionStr)
            if f is not None or f1 is not None:
                pyautogui.click(x=827, y=1013, duration=1)
                pyautogui.click(x=914, y=296, duration=1)
                time.sleep(120)
                pyautogui.click(x=936, y=658, duration=1)
                time.sleep(120)
                # pyautogui.scroll(-800)
                # pyautogui.click(x=936, y=658, duration=1)
                # time.sleep(120)
                pyautogui.click(x=674, y=71, duration=1)
                pyautogui.click(x=938, y=1013, duration=1)
                break
            # elif c is not None:
            #     pyautogui.click(x=1758, y=593, duration=2)
            #     pyautogui.click(x=1499, y=124, duration=2)
            #     pyautogui.click(x=1464, y=212, duration=2)
            #     pyautogui.scroll(-100)  # 向下滚动10格
            #     pyautogui.scroll(100)  # 向上滚动10格
            # else:
            #     # pyautogui.click(x=1605, y=1007, duration=1)
            #     pyautogui.click(x=1588, y=1002, duration=1)
            #     break

    # time.sleep(15)
    end_time = time.time()
if __name__ == "__main__":
    # get_mouse_positon()
    # pyautogui.click(x=1078, y=11, duration=1)
    # pyautogui.dragTo(1576, 11, 3, button='left')
    # 鼠标坐标点（X,Y）为：1844,  60 RGB:(130,126,125)
    # 匹配屏幕所有与目标图片的对象，可以用for循环和list()输出
    # pyautogui.locateAllOnScreen(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot.png')
    # for pos in pyautogui.locateAllOnScreen(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot.png'):
    #     print(pos)s\region_sc
    # 不截全屏，截取区域图片。截取区域region参数为：左上角XY坐标值、宽度和高度
    # pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot.png', region=(1075, 945, 111, 22))
    # pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot1.png', region=(1075, 945, 111, 22))
    # pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Picturereenshot_close.png', region=(1819, 52, 32, 18))
    # pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_read.png', region=(1723, 679, 82, 33))
    # # pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_back.png', region=(665, 59, 19, 22))
    # pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_task.png', region=(1576, 993, 35, 34))
    # pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_backgroud.png', region=(1011, 64, 111, 34))
    # pyautogui.screenshot(r'C:\Users\GAVX\Pictures\Saved Pictures\region_screenshot_backgroud1.png', region=(1011, 64, 111, 34))
    # pix = pyautogui.screenshot().getpixel((1190, 62))  # 获取坐标(220,200)所在屏幕点的RGB颜色
    # positionStr = ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
    #     3) + ')'
    # print(positionStr)
    start_time = time.time()
    click_job()
    end_time = time.time()
    exe_time = end_time-start_time
    sched.add_job(click_job, 'interval', seconds=600-exe_time, max_instances=10)
    sched.start()

