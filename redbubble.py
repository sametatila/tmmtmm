from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
import time


# Declare some variables
login_url = "https://www.redbubble.com/auth/login"
username = "sametatila@gmail.com"
password = "Linkin.123"
create_url = "https://www.redbubble.com/portfolio/images/53012017-the-cat-looking-for-the-future/duplicate"
product_title = "Oha amk!"
tags = "asd,asda,asdsad"
description = "asdfsadfsdfsdfdf"
design_path = "C:\ytw/az.png"
bg_color = "#000000"


        
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')


#Run Chromium
driver = webdriver.Chrome('chromedriver.exe')


###Start
#Login Page
driver.get (login_url)
time.sleep(8)

#Accept Cuki
driver.find_element_by_xpath('//*[@id="RB_React_Component_CookieBanner_1"]/div/div/div/button').click()

#Login Info
driver.find_element_by_xpath('//*[@id="ReduxFormInput1"]').send_keys(username)
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

