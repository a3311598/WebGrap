import time
# import pyquery as pq
# import trains as trains
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Keys, DesiredCapabilities

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
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

from apscheduler.schedulers.blocking import BlockingScheduler
#chromedriver version 101.0.4951.15 | chrome 102.0.5005.13
sched = BlockingScheduler(timezone="Asia/Shanghai")

# 判断是否有元素
def is_element_present(obj, by, value):
    try:
        element = obj.find_element(by=by, value=value)
    except NoSuchElementException as e:
        return False
    return True
#选择买票
def input_info(driver):
    print('=====开始买票=====')
    start_station = '潮阳站'
    end_station = '广州南站'
    from_station = driver.find_element(By.XPATH,'//*[@id="fromStationText"]')
    from_station.send_keys(Keys.ENTER)
    from_station.send_keys(Keys.CONTROL, 'a')
    from_station.send_keys(start_station, Keys.ENTER)
    driver.implicitly_wait(5)
    to_station = driver.find_element(By.XPATH,'//*[@id="toStationText"]')
    to_station.send_keys(Keys.ENTER)
    to_station.send_keys(Keys.CONTROL, 'a')
    to_station.send_keys(end_station, Keys.ENTER)
    driver.implicitly_wait(5)
    start_date = driver.find_element(By.XPATH,'//*[@id="train_date"]')
    start_date.send_keys(Keys.ENTER)
    start_date.send_keys(Keys.CONTROL, 'a')
    start_date.send_keys(Keys.CONTROL, 'x')
    start_date.send_keys('2022-05-06', Keys.ENTER)
    driver.implicitly_wait(5)

    wait = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,'query_ticket'))).click()

def ticket_job():
    train_ticket();
def refresh_valid(driver):
    flag = is_element_present(driver, By.ID, 'nc_1_refresh1')
    refreshBtn = driver.find_element(By.ID, 'nc_1_refresh1')
    if(flag):
        refreshBtn.click()
    # 滑块验证
    driver.implicitly_wait(5)
    print('=====开始处理滑动验证码=====')

    track = [300, 400, 500]
    for i in track:
        try:
            btn = driver.find_element(By.XPATH,'//*[@id="nc_1__scale_text"]/span')
            ActionChains(driver).drag_and_drop_by_offset(btn,i,0).perform()
        except:
            time.sleep(2)
            print('出现异常')
def train_ticket():
    url = 'https://kyfw.12306.cn/otn/resources/login.html'
    s = Service(r"C:\Users\GAVX\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    driver = webdriver.Chrome(service=s,options=options)
    driver.minimize_window()
    driver.get(url)
    # 点击账号登录
    try:
        wait = WebDriverWait(driver,5,0.1).until(EC.element_to_be_clickable((By.CLASS_NAME,'login-hd-code'))).click()
    except:
        element = driver.find_element(By.ID, 'login-hd-code')
        driver.execute_script("arguments[0].click();", element)
        print('出现异常')
    # 输入账号
    input_account=driver.find_element(By.ID,'J-userName')
    input_account.send_keys('youracount')
    # 输入密码

    input_password=driver.find_element(By.ID,'J-password')
    input_password.send_keys('yourpassword')
    # 点击登录按钮

    element = driver.find_element(By.ID, 'J-login')
    driver.execute_script("arguments[0].click();", element)
    # 滑块验证
    driver.implicitly_wait(5)
    print('=====开始处理滑动验证码=====')
    track = [300, 400, 500]
    for i in track:
        try:
            btn = driver.find_element(By.XPATH, '//*[@id="nc_1__scale_text"]/span')
            ActionChains(driver).drag_and_drop_by_offset(btn, i, 0).perform()
        except:
            time.sleep(2)
            print('出现异常')

    #疫情特殊要求
    driver.implicitly_wait(5)
    try:
        element1 = driver.find_element(By.CLASS_NAME, 'btn-primary')
        driver.execute_script("arguments[0].click();", element1)
    except:
        print('出现异常')

    # 点击车票预定
    try:
        driver.find_element(By.ID,'link_for_ticket').click()
    except:
        print('出现异常')
    input_info(driver)
    input_info(driver)
    while(True):
        issuccess = purchase_ticket(driver)
        if issuccess:
            print('预定成功')
            break;
        else:
            try:
                element2 = driver.find_element(By.ID, 'query_ticket')
                driver.execute_script("arguments[0].click();", element2)
            except:
                print('出现异常')




def purchase_ticket(driver):
    trList = driver.find_elements(By.XPATH,".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
    for tr in trList:
        trainNum = tr.find_element(By.CLASS_NAME,"number").text
        trains = ['G6361', 'G9641', 'G6313', 'G1607', 'G9795','D7119','G6359','D2387','G4315']
        if trainNum in trains:
            leftTicket = tr.find_element(By.XPATH,".//td[4]").text
            # leftTicket1 = tr.find_element(By.XPATH,".//td[11]").text
            print('leftTicket', leftTicket)
            time.sleep(0.5)
            if leftTicket == '有' or leftTicket.isdigit():
                orderBtn = tr.find_element(By.CLASS_NAME,"btn72")
                orderBtn.click()
                driver.implicitly_wait(5)
                # 勾选乘客信息第一个是自己
                driver.find_element(By.ID, 'normalPassenger_0').click()
                driver.implicitly_wait(20)
                # 获取提交按钮
                submitBtn = driver.find_element(By.ID,"submitOrder_id")
                submitBtn.click()
                driver.implicitly_wait(20)
                confirmBtn = driver.find_element(By.ID,"qr_submit_id")
                confirmBtn.click()
                time.sleep(2)
                driver.implicitly_wait(20)
                confirmBtn = driver.find_element(By.ID,"qr_submit_id")
                confirmBtn.click()
                return True
    return False

if __name__ == '__main__':
    try:
        train_ticket()
        if sched is not None:
            sched.shutdown()
    except:
        sched.add_job(ticket_job, 'interval', seconds=60)
        sched.start()


