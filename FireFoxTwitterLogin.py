import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://twitter.com/login')
time.sleep(10)
emailElem = browser.find_element_by_name('session[username_or_email]')
emailElem.send_keys('vikramqoou@gmail.com')
password = browser.find_element_by_name('session[password]')
password.send_keys('password@@')
#session[password] 
time.sleep(5)
password.send_keys(Keys.RETURN)
#browser.find_element_by_link_text('Log in').click()
time.sleep(5)

#result in snapshot-1.5