from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time


#Normal variables
login_url = "http://artists.teefury.com/signin"
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
options.binary_location = r"C:/ytw/browser/chrome.exe"
options.add_argument("--mute-audio")
driver = webdriver.Chrome(chrome_options=options)

###Start
#Login Page
driver.get(login_url)
time.sleep(5)

#Login Info
driver.find_element_by_xpath('//*[@id="root"]/main/section/form/div[1]/input').send_keys(username1)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/main/section/form/div[2]/input').send_keys(password)
time.sleep(3)

#Login Button
driver.find_element_by_xpath('//*[@id="root"]/main/section/form/div[4]/button').click()
time.sleep(5)
###End
#PAYPAL OLMADAN YAPAMIYORUZ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX