from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time, os


#Normal variables
login_url = "https://www.shirtee.com/en/customer/account/login/"
username1 = "sametatila@gmail.com"
password = "Linkin.123"
create_url = "https://www.shirtee.com/en/designer/?id=1140/"
product_title = "Oha amk!"
tags = "asd,asda,asdsad"
description = "asdfsadfsdfsdfdf"
design_path = "C:\ytw/az.png"
bg_color = "#000000"

#Run Chromium
options = Options()
options.binary_location = os.getcwd() + "/browser/chrome.exe"
options.add_argument("--mute-audio")
driver = webdriver.Chrome(chrome_options=options)

###Start
#Login Page
driver.get(login_url)
time.sleep(5)

#Login Info
driver.find_element_by_xpath('//*[@id="email"]').send_keys(username1)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
time.sleep(3)

#Login Button
driver.find_element_by_xpath('//*[@id="send2"]').click()
time.sleep(5)
###End

###Start
#Product Create Page   
driver.get(create_url)
time.sleep(3)

#Galiba olmadı çözemedimXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#Design Path
driver.find_element_by_xpath('//*[@id="upload-image-drop-zone"]/div[4]/a').send_keys(design_path)
time.sleep(30)

#Background Color
driver.find_element_by_xpath('//*[@id="right-color-group"]/span[4]').click()
time.sleep(1)

#Kuki lerle alakalı bişe diyor çözemedimXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxx
#First To The Next Step Button
driver.find_element_by_xpath('//*[@id="pd_gt_product"]').click()
time.sleep(5)

#Load Collection Template
driver.find_element_by_xpath('//*[@id="calculation-load-popup-button"]').click()
time.sleep(2)

#Standard Temp
driver.find_element_by_xpath('//*[@id="calculation-load-popup"]/div[1]/div/div[2]/div/div[2]/button[1]').click()
time.sleep(5)

#Second To The Next Step Button
driver.find_element_by_xpath('//*[@id="pd_gt_product"]').click()
time.sleep(5)

#Product Title
driver.find_element_by_xpath('//*[@id="sales_name"]').send_keys(product_title)
time.sleep(2)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Dil seçilmesi lazım
#Product Description
driver.find_element_by_xpath('//*[@id="pdproduct-description"]').click()
time.sleep(2)
driver.find_element_by_xpath('').click()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Digital Art seçilmesi lazım
#Product Category
driver.find_element_by_xpath('//*[@id="select2-categories_ids-container"]').click()
time.sleep(2)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Shop seçilmesi lazım
#Designer's Shop
driver.find_element_by_xpath('//*[@id="designers_categories_ids"]').click()
time.sleep(2)

#Product Tags
driver.find_element_by_xpath('//*[@id="tags-input"]').send_keys(tags)
time.sleep(2)

#Create Products Button
driver.find_element_by_xpath('//*[@id="pd_sales"]').click()
time.sleep(10)
