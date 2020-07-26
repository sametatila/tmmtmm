from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


#Declare some variables
login_url = "https://teespring.com/login"
username1 = "sametatila@gmail.com"
password = "Linkin.123"
create_url = "https://teespring.com/design-launcher/design/5d79cc90-8310-4009-bfc9-ff2c20a8ea2d?duplicate=the-cat-looking-for-the-fut208"
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
driver.find_element_by_xpath('//*[@id="sessions_new"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/form/div/div[1]/input').send_keys(username1)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="sessions_new"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/input').send_keys(password)
time.sleep(70)

#Login Button
driver.find_element_by_xpath('//*[@id="sessions_new"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/form/div/input').click()
time.sleep(5)
###End

###Start
#Product Create Page   
driver.get(create_url)
time.sleep(5)


#Design Upload
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[2]/div/section[1]/div[3]/span/button/span').send_keys(design_path)
time.sleep(10)

#First Continue Button
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[3]/div/button[2]/span').click()
time.sleep(5)

#Second Continue Button
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[3]/div/button[2]/span').click()
time.sleep(5)

#Product Title
driver.find_element_by_xpath('//*[@id="title"]').clear()
driver.find_element_by_xpath('//*[@id="title"]').send_keys(product_title)
time.sleep(1)

#Description
driver.find_element_by_xpath('//*[@id="description"]').clear()
driver.find_element_by_xpath('//*[@id="description"]').send_keys(description)
time.sleep(1)

#Product URL
driver.find_element_by_xpath('//*[@id="url"]').send_keys(product_url)
time.sleep(1)

#Publish Listing Button
#driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[3]/div/button[2]/span').click()
#time.sleep(60)