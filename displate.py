from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


#Declare some variables
login_url = "https://displate.com/auth/signin"
username1 = "sametatila@gmail.com"
password = "Linkin.123"
create_url = "https://displate.com/file-upload"
product_title = "Oha amk!"
tags = "asd,asda,asdsad"
description = "asdfsadfsdfsdfdf"
product_url = "oha-amk"
design_path = "C:\ytw/az.png"
bg_color = "#000000"



options = webdriver.ChromeOptions()
options.add_argument("--mute-audio")
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery");
options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
#options.add_argument("--start-maximized")
# add here any tag you want.
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
driver.delete_all_cookies()
driver.set_window_size(1100,1000)
driver.set_window_position(0,0)

#Run Chromium
#driver = webdriver.Chrome('chromedriver.exe')

###Start
#Login Page
driver.get(login_url)
time.sleep(10)

#Login Info
driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div/input').send_keys(username1)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div/input').send_keys(password)
time.sleep(70)

#Login Button
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(5)
###End

###Start
#Product Create Page   
driver.get(create_url)
time.sleep(5)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#Design Upload
driver.find_element_by_xpath('//*[@id="multiuploader"]/div/div[1]/div/div/button').send_keys(design_path)
time.sleep(10)
#Sadece JPG ve 4200px üzeri kabul ediyor.