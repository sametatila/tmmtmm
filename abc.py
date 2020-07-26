from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

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
    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div').find_elements_by_tag_name('dd')
    result = " ".join( [ each.text for each in text ] )

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return result

def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)


#Normal variables
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
#options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
driver.delete_all_cookies()
driver.set_window_size(1100,1000)
driver.set_window_position(0,0)

#Run Chromium
#driver = webdriver.Chrome('chromedriver.exe')

###Start
#Login Page
driver.get(login_url)
time.sleep(5)

#Accept Cuki
driver.find_element_by_xpath('//*[@id="RB_React_Component_CookieBanner_1"]/div/div/div/button').click()

#Login Info
driver.find_element_by_xpath('//*[@id="ReduxFormInput1"]').send_keys(username1)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ReduxFormInput2"]').send_keys(password)
time.sleep(3)

#Login Button
driver.find_element_by_xpath('//*[@id="RB_React_Component_LoginFormContainer_0"]/div/form/span/button').click()
time.sleep(3)




#Gerizekali bölüm

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

