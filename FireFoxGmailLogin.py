import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://www.google.com')
browser.find_element_by_link_text('Sign in').click()

emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('sumanth.plan@gmail.com')
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(1)
#passwordElem = browser.find_element_by_id('password') aXBtI I0VJ4d Wic03c
passwordElem = browser.find_element_by_name("password")
passwordElem.send_keys('password@@')
signinButton = browser.find_element_by_class_name('CwaK9')
signinButton.click()

#Result in snapshot-1.3
