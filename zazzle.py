from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os, sys
import time,requests
from bs4 import BeautifulSoup

#Declare aq variables
delayTime = 2
audioToTextDelay = 10
filename = 'test.mp3'
googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'

def audioToText(mp3Path):
    
    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])

    driver.get(googleIBMLink)

    # Upload file 
    time.sleep(1)
    root = driver.find_element_by_id('root').find_elements_by_class_name('dropzone _container _container_large')
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    btn.send_keys(mp3Path)

    # Audio to text is processing
    time.sleep(audioToTextDelay)
    result = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div').text

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return result

def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)


#Normal variables
login_url = "https://www.zazzle.com/lgn/signin"
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
driver.find_element_by_xpath('//*[@id="page_username-input"]').send_keys(username1)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="page_password-input"]').send_keys(password)
time.sleep(3)

#Login Button
driver.find_element_by_xpath('//*[@id="page_signin"]').click()
time.sleep(5)


##Google Rechaptcha v3 Bot

#googleClass = driver.find_elements_by_class_name('g-recaptcha')[0]
#outeriframe = googleClass.find_element_by_tag_name('iframe')
#outeriframe.click()

allIframesLen = driver.find_elements_by_tag_name('iframe')
audioBtnFound = False
audioBtnIndex = -1

for index in range(len(allIframesLen)):
    driver.switch_to_default_content()
    iframe = driver.find_elements_by_tag_name('iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(delayTime)
    try:
        audioBtn = driver.find_element_by_id('recaptcha-audio-button') or driver.find_element_by_id('recaptcha-anchor')
        audioBtn.click()
        audioBtnFound = True
        audioBtnIndex = index
        break
    except Exception as e:
        pass

if audioBtnFound:
    try:
        while True:
            href = driver.find_element_by_id('audio-source').get_attribute('src')
            response = requests.get(href, stream=True)
            saveFile(response,filename)
            response = audioToText(os.getcwd() + '/' + filename)
            print(response)

            driver.switch_to_default_content()
            iframe = driver.find_elements_by_tag_name('iframe')[audioBtnIndex]
            driver.switch_to.frame(iframe)

            inputbtn = driver.find_element_by_id('audio-response')
            inputbtn.send_keys(response)
            inputbtn.send_keys(Keys.ENTER)

            time.sleep(2)
            errorMsg = driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]

            if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                print("Success")
                break
             
    except Exception as e:
        print(e)
        print('Caught. Need to change proxy now')
else:
    print('Button not found. This should not happen.')
###End
