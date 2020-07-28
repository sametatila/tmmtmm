from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time, os

#Ah ney yapsam ne etsem oldurabilsem. Olmuyor Amk olmuyor

#Normal variables
login_url = "https://partner.spreadshirt.com/login"
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

#Login Info
driver.find_element_by_xpath('').send_keys(username1)
time.sleep(3)
driver.find_element_by_xpath('').send_keys(password)
time.sleep(3)

#Login Button
driver.find_element_by_xpath('').click()
time.sleep(5)
###End
