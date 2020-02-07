import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#opens Firefox
browser = webdriver.Firefox()

#opens Google
browser.get('http://www.google.com')

#Access search box
search = browser.find_element_by_name('q')

#Enters search element
search.send_keys("Data science")

#Returns and press enter 
search.send_keys(Keys.RETURN)

time.sleep(5) # sleep for 5 seconds so you can see the results

#WebLinks are pulled from first page
Links = browser.find_elements_by_xpath("//cite[@class='iUh30 bc']")
for Link in Links:
    print (Link.text)
    
#Click on next button
browser.find_element_by_css_selector("a.pn[id='pnnext']").click()

#butn = browser.find_element_by_link_text('next')
#butn.click()  

#Second page Web Links
Links = browser.find_elements_by_xpath("//cite[@class='iUh30 bc']")
for Link in Links:
    print (Link.text)


#print (browser.find_elements_by_class_name("iUh30 bc"))
#print (search.findElement(By.className("iUh30 bc")))

#Result in snapshot-1.1