from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


#Declare some variables
login_url = "https://www.redbubble.com/auth/login"
username1 = "linkinqark1000@gmail.com"
password = "Linkin.123"
create_url = "https://www.redbubble.com/portfolio/images/53012017-the-cat-looking-for-the-future/duplicate"
product_title = "Oha amk!"
tags = "asd,asda,asdsad"
description = "asdfsadfsdfsdfdf"
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
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
driver.delete_all_cookies()
driver.set_window_size(900,1000)
driver.set_window_position(0,0)

#Run Chromium
#driver = webdriver.Chrome('chromedriver.exe')

###Start
#Login Page
driver.get(login_url)
time.sleep(10)

#Accept Cuki
driver.find_element_by_xpath('//*[@id="RB_React_Component_CookieBanner_1"]/div/div/div/button').click()

#Login Info
driver.find_element_by_xpath('//*[@id="ReduxFormInput1"]').send_keys(username1)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="ReduxFormInput2"]').send_keys(password)
time.sleep(5)

#Login Button
driver.find_element_by_xpath('//*[@id="RB_React_Component_LoginFormContainer_0"]/div/form/span/button').click()
time.sleep(60)
###End

###Start
#Product Create Page   
driver.get(create_url)
time.sleep(3)


#Product Title
driver.find_element_by_xpath('//*[@id="work_title_en"]').send_keys(product_title)
time.sleep(1)

#Product Tags
driver.find_element_by_xpath('//*[@id="work_tag_field_en"]').send_keys(tags)
time.sleep(1)

#Product Description
driver.find_element_by_xpath('//*[@id="work_description_en"]').send_keys(description)
time.sleep(1)

#Design Path
driver.find_element_by_xpath('//*[@id="select-image-base"]').send_keys(design_path)
time.sleep(1)

