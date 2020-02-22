import urllib.request
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#wd = webdriver.Chrome()
#wd.implicitly_wait(3)
mobile_emulation = { "deviceName": "Galaxy S5" }

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

wd = webdriver.Chrome( desired_capabilities = chrome_options.to_capabilities())

wd.get('https://www.baidu.com')
#mouth=ActionChains(wd)
#mouth.move_to_element(wd.find_element_by_css_selector('[name="tj_briicon"]')).perform()
print(wd.current_url)
#em=wd.find_element_by_id('kw')
#em.send_keys('123')
#em2=wd.find_element_by_id('su')
#em2.click()
#sleep(2)
#em3=wd.find_element_by_id('1')
#print(em.get_attribute('value'))