from appium import webdriver
import time

usn="your usn"
psd="your psd"

desired_caps = {
'platformName':'Android',
'platformVersion':'7.1.1',
'deviceName':'192.168.93.101:5555',
'appPackage':'com.ss.android.article.news',
'appActivity':'com.ss.android.article.news.activity.SplashBadgeActivity',
'dontStopAppOnReset':True,
'autoGrantPermissions':True,
'noReset':True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)       #根据字典打开app
time.sleep(3)
x=driver.get_window_size()['width']
y=driver.get_window_size()['height']
driver.swipe(1/2*x,5/6*y,1/2*x,1/6*y,200)  #向下滑动
time.sleep(3)
driver.swipe(1/2*x,1/6*y,1/2*x,5/6*y,200)  #向上滑动
time.sleep(3)
Me=driver.find_element_by_xpath("//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.RelativeLayout[4]")  #进入我的界面
Me.click()
time.sleep(2)
login=driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ss.android.article.news:id/c29']")   #点击登录
login.click()
time.sleep(2)
psdlogin=driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ss.android.article.news:id/s_']")
psdlogin.click()
time.sleep(1)
usnfield=driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.article.news:id/s3']")  #输入手机号
usnfield.send_keys(usn)
psdfield=driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.article.news:id/rj']")
psdfield.send_keys(psd)
#idcodebutton=driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ss.android.article.news:id/p5']")  #验证码
#idcodebutton.click()
#idcode=input("please type in the idcode, if you finish, please press the 'enter' button on your keyboard")
#idcodefield=driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.article.news:id/s5']")
#idcodefield.send_keys(idcode)
time.sleep(1)
enter=driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.ss.android.article.news:id/rm']")    #点击登录按钮
enter.click()
time.sleep(1)

print("Finish!")
