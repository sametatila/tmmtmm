from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time, os


#Normal variables
login_url = "https://www.designbyhumans.com/login"
username1 = "sametatila@gmail.com"
password = "Linkin.123"
create_url = ""
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

#XPATH'te Rastgele sayılar koymuşlar her sayfa yüklendiğinde değişiyorXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#Login Info
driver.find_element_by_xpath('//*[@id="username_b174e88737910"]').send_keys(username1)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="pwd_b8107d84ca949"]').send_keys(password)
time.sleep(3)

#Login Button
driver.find_element_by_xpath('//*[@id="login_form"]/div/div[6]/div/div/span[2]/a/span').click()
time.sleep(5)
###End
#PAYPAL OLMADAN YAPAMIYORUZ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX