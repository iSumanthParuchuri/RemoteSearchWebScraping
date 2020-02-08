import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyodbc
server = 'localhost'
database = 'python'
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
                      "Server=" + server + ";" +
                      "Database=" + database + ";" +
                      "Trusted_Connection=yes;")
cursor = conn.cursor()
CheckT = "SELECT * FROM information_schema.tables where table_name = 'GoogleSearchData1';"
DropT = "Drop table GoogleSearchData1"
conn.execute(CheckT)
flag = conn.execute(CheckT).fetchall()
if flag:
    conn.execute(DropT)
    conn.commit()
CreateT = "Create table GoogleSearchData1(Descriptions nvarchar(max));"
conn.execute(CreateT)
conn.commit()
insertT = "Insert into GoogleSearchData1(Descriptions) values(?);"
browser = webdriver.Firefox()
browser.get('http://www.google.com')
search = browser.find_element_by_name('q')
search.send_keys("Data science")
search.send_keys(Keys.RETURN)
time.sleep(5)
Links = browser.find_elements_by_xpath("//cite[@class='iUh30 bc']")
Descriptions = browser.find_elements_by_xpath("//h3[@class='LC20lb']")
i=0
for Description in Descriptions:
    print (Descriptions[i].text)
    conn.execute(insertT, Descriptions[i].text)
    conn.commit()
    i=i+1
browser.find_element_by_css_selector("a.pn[id='pnnext']").click()
Links = browser.find_elements_by_xpath("//cite[@class='iUh30 bc']")
Descriptions = browser.find_elements_by_xpath("//h3[@class='LC20lb']")
i=0
for Description in Descriptions:
    print (Descriptions[i].text)
    conn.execute(insertT, Descriptions[i].text)
    conn.commit()
    i=i+1
