from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie(r'C:\Users\Z004408T\PycharmProjects\selenium\drivers\IEDriverServer.exe')
driver.set_page_load_timeout(5)

driver.get('http://google.com')

driver.find_element_by_name("q").send_keys('Machine Learning')
driver.find_element_by_name('btnK').send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()
