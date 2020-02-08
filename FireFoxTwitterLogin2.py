from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://twitter.com/login")

username_field = driver.find_element_by_class_name("js-username-field")
password_field = driver.find_element_by_class_name("js-password-field")

username_field.send_keys('vikramqoou@gmail.com')

password_field.send_keys('password@@')

driver.find_element_by_class_name("EdgeButtom--medium").click()