from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get ("https://speech-to-text-demo.ng.bluemix.net/")
time.sleep(10)

btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
btn.send_keys("C:\ytw/tmmtmm/test.mp3")
time.sleep(5)
result = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div').text
print(result)

