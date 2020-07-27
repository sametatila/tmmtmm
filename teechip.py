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
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/form/div[1]/div/input').send_keys(username1)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/form/div[2]/div/input').send_keys(password)
time.sleep(3)


#Google Rechaptcha v3 Bot

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

#Success
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/span'))
    WebDriverWait(driver, delayTime).until(element_present)
finally:
    print(element_present)
    #driver.quit()