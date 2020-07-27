from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time



#Normal variables
login_url = "https://fineartamerica.com/loginartist.php"
username1 = "sametatila@gmail.com"
password = "Linkin123"
#create_url = "https://fineartamerica.com/controlpanel/updateartwork.html?newartwork=true&sessionid=c1a220c154a87787328d8031f88b25b7"
profile_url = "https://fineartamerica.com/profiles/samet-atila"
product_title = "Oha la!"
tags = "asd,asda,asdsad"
description = "asdfsadfsdfsdfdf"
design_path = "C:\ytw/az.png"
bg_color = "#000000"
medium = "Bilmiyom"

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
driver.find_element_by_xpath('//*[@id="loginartist"]/div/div[1]/input').send_keys(username1)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="loginartist"]/div/div[2]/input').send_keys(password)
time.sleep(3)

#Login Button
driver.find_element_by_xpath('//*[@id="loginartist"]/div/div[3]/a').click()
time.sleep(3)
###End

###Start
#Profil Page
driver.get(profile_url)
time.sleep(5)

#Product Create Page Button 
driver.find_element_by_xpath('//*[@id="memberfeaturesnewdiv"]/div/a[1]').click()
time.sleep(5)

#Yine Yapamadım AmkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#Design Path
driver.find_element_by_xpath('//*[@id="uploadimage[5f1f0938d1791]"]').send_keys(design_path)
time.sleep(3)

#Upload Button
driver.find_element_by_xpath('//*[@id="uploadImageDiv"]/a').click()
time.sleep(30)

#Background Color Bölümü Lazım

#Submit Button
driver.find_element_by_xpath('//*[@id="submitDivMakeOpaque-5f1f09c9e1f9a"]/a').click()
time.sleep(5)

#Product Title
driver.find_element_by_xpath('//*[@id="imageTitleDiv"]/input').send_keys(product_title)
time.sleep(1)

#Medium
driver.find_element_by_xpath('//*[@id="imageMediumDiv"]/input').send_keys(medium)
time.sleep(1)

#Tags
driver.find_element_by_xpath('//*[@id="artworkkeywords"]').send_keys(tags)
time.sleep(1)

#Description
driver.find_element_by_xpath('//*[@id="imageDetailsDiv"]/div/div[5]/textarea').send_keys(description)
time.sleep(1)

#BilmiyommmmmmmmmmmmmmmXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx
#Artwork Category
driver.find_element_by_xpath('').send_keys()
time.sleep(1)

#Submit Button Finish
driver.find_element_by_xpath('//*[@id="submitbottomdiv[5f1f09c9e1f9a]"]/a').click()
time.sleep(30)

