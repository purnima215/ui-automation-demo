#stackoverflow 

from selenium import webdriver
import time

#browser = webdriver.Firefox()
browser = webdriver.Chrome('C:\Users\PURNIMA\Documents\chromedriver')
browser.get("https://stackoverflow.com")
browser.find_element_by_id("nav-tags").click()
browser.find_element_by_id("tagfilter").send_keys("qa")
#need to use explicit webdriver wait here, instead of sleep. 
time.sleep(5)
print browser.find_element_by_xpath("//*[@id='tags-browser']/tbody/tr[1]/td[1]/div[2]/div[1]/a[2]").text.split(" ")[0]