from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "https://www.youtube.com/"
driver.get(url)

time.sleep(5)
driver.quit()