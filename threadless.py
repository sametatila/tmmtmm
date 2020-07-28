from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

#Declare some variables
login_url = "https://www.threadless.com/login/"
username = "sametatila@gmail.com"
password = "Linkin.123!"
create_url = "https://www.threadless.com/profile/artist_dashboard/artist-shop/products/create/"
product_title = "Oha amk!"
design_path = os.getcwd() + "/az.png"
bg_color = "#000000"

#Run Chromium
options = Options()
options.binary_location = r"C:/ytw/browser/chrome.exe"
options.add_argument("--mute-audio")
driver = webdriver.Chrome(chrome_options=options)



###Start
#Login Page
driver.get (login_url)
time.sleep(5)

#Login Info
driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(username)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(password)
time.sleep(1)

#Login Button
driver.find_element_by_xpath('//*[@id="login_form"]/fieldset/input[2]').click()
time.sleep(5)
###End

###Start
#Product Create Page
driver.get(create_url)
time.sleep(3)

#Product Title
driver.find_element_by_xpath('//*[@id="id_title"]').send_keys(product_title)
time.sleep(1)

#Design Upload
driver.find_element_by_name("upload").send_keys(design_path)
time.sleep(1)

#Backround_Color
driver.find_element_by_class_name("sp-preview").click()
time.sleep(1)
#Pick Color
driver.find_element_by_class_name("sp-input").clear()
driver.find_element_by_class_name("sp-input").send_keys(bg_color)
time.sleep(1)

#Mature Content
driver.find_element_by_xpath('//*[@id="id_nsfw_1"]').click()
time.sleep(1)

#Add Add Apparel, Home and Accessories
driver.find_element_by_xpath('//*[@id="createProductForm"]/section[1]/h2/i').click()
time.sleep(1)

#Apparel
driver.find_element_by_xpath('//*[@id="createProductForm"]/section[1]/div/div[2]/div/div[1]/label/i').click()
time.sleep(1)

#Color Select All
driver.find_element_by_xpath('//*[@id="createProductForm"]/section[1]/div/div[2]/div/div[1]/div/div[1]/div/a').click()
time.sleep(1)

#Men's Select All
driver.find_element_by_xpath('//*[@id="createProductForm"]/section[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/a').click()
time.sleep(1)

#Women's Select All
driver.find_element_by_xpath('//*[@id="createProductForm"]/section[1]/div/div[2]/div/div[1]/div/div[3]/div[1]/a').click()
time.sleep(1)

#Kid's Select All
driver.find_element_by_xpath('//*[@id="createProductForm"]/section[1]/div/div[2]/div/div[1]/div/div[4]/div[1]/a').click()
time.sleep(1)

#Home Select All
driver.find_element_by_xpath('//*[@id="createProductForm"]/section[1]/div/div[2]/div/div[2]/a').click()
time.sleep(1)

#Accessories Select All
driver.find_element_by_xpath('//*[@id="createProductForm"]/section[1]/div/div[2]/div/div[3]/a').click()
time.sleep(1)

#User Agreement
driver.find_element_by_xpath('//*[@id="id_design_ownership"]').click()
time.sleep(1)

#Create Product Button
#driver.find_element_by_xpath('//*[@id="createProductForm"]/div[3]/div').click()
#time.sleep(1)
###End
