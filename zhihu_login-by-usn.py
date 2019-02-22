from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import subprocess
import json

url='https://www.zhihu.com/signup?next=%2F'
usn="your username"
psd="your password"
follower_list=[]

def login(browser):
    button_login = browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[2]/span")
    button_login.click()
    time.sleep(1)
    username=browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input")
    username.send_keys(usn)
    password=browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input")
    password.send_keys(psd)
    login=browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/button")
    login.click()
    print("是否有验证码？如有请手动输入验证码，完成后在控制台回车；如无请直接在控制台回车")
    input()
    time.sleep(1)
    return

def extract_user_information(browser):
    page = 1
    while page<3:
        users=browser.find_elements_by_class_name("UserLink-link")
        for user in users:
            follower_list.append(user.text)
            follower_list.append(user.get_attribute("href"))
        nextpage=browser.find_element_by_xpath("//*[@id='Profile-following']/div[2]/div[21]/button[7]")
        nextpage.click()
        time.sleep(2)
        webpage="第",page,"页"
        follower_list.append(webpage)
        page=page+1
    return

if __name__ == '__main__':
    subprocess.Popen('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"')
    time.sleep(1)
    chrome_options = Options()  # 取得对已有浏览器的控制
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    browser = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    browser.get(url)     #打开知乎
    time.sleep(2)
    login(browser)       #调用login函数登录知乎
    time.sleep(1)
    browser.get("https://www.zhihu.com/people/zhang-jia-wei/followers")     #跳转至“张佳玮”的follower界面
    time.sleep(1)
    extract_user_information(browser)      #调用extract_user_information开始捕获follower的信息
    for i in follower_list:
        print(i)
    print('Mission complete!')

    time.sleep(5)
    browser.quit()
