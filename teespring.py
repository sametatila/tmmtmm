from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
import time


#Declare some variables
login_url = "https://teespring.com/login"
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

#Run Chromium
driver = webdriver.Chrome('chromedriver.exe')

###Start
#Login Page
driver.get(login_url)
time.sleep(10)

#Accept Cuki
#driver.find_element_by_xpath('//*[@id="RB_React_Component_CookieBanner_1"]/div/div/div/button').click()

#Login Info
driver.find_element_by_xpath('//*[@id="sessions_new"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/form/div/div[1]/input').send_keys(username)
time.sleep(10)
driver.find_element_by_xpath('//*[@id="sessions_new"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/input').send_keys(password)
time.sleep(10)

#Bot Button
driver.find_element_by_id('recaptcha-anchor').click()

#Login Button
driver.find_element_by_xpath('//*[@id="sessions_new"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/form/div/input').click()
time.sleep(10)

###End
