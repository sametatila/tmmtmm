from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


#Declare some variables
login_url = "https://teechip.com/manager/auth/login"
username1 = "sametatila@gmail.com"
password = "Linkin.123"
create_url = "https://teechip.com/manager/campaigns/duplicate?campaignId=5f15c4be941bfe7acc5341dd"
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
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/form/div[1]/div/input').send_keys(username1)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/form/div[2]/div/input').send_keys(password)
time.sleep(70)

#Login Button
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/form/div[4]/div/button').click()
time.sleep(5)
###End

###Start
#Product Create Page   
driver.get(create_url)
time.sleep(5)

#Delete All Artwork Button
driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div/div[1]/h1/a').click()
time.sleep(3)

#Remove All Button
driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[2]/div').click()
time.sleep(3)

#Design Upload
driver.find_element_by_xpath('//*[@id="design-tool"]/div[4]/div[2]/label/span').send_keys(design_path)
time.sleep(30)

#First Continue Button
driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div/div[3]/div').click()
time.sleep(2)

#Proceed Button
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/div[2]/div').click()
time.sleep(5)

#Second Continue Button
driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div/div[3]/a').click()
time.sleep(2)

#Product Title
driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[1]/form/div[1]/div[1]/div/input').clear()
driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[1]/form/div[1]/div[1]/div/input').send_keys(product_title)
time.sleep(1)

#Description
driver.find_element_by_xpath('//*[@id="ql-editor-1"]/div').clear()
driver.find_element_by_xpath('//*[@id="ql-editor-1"]/div').send_keys(description)
time.sleep(1)

#Product URL
driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[1]/form/div[2]/div[1]/div/input').clear()
driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[1]/form/div[2]/div[1]/div/input').send_keys(product_url)
time.sleep(1)

#Launch Campaign
driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div/div[3]/div').click()
time.sleep(60)