from lib2to3.pgen2 import driver
from optparse import Option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
options.add_argument("--start-maximized")
# options.add_argument("disable-infobars")
browser=webdriver.Chrome(options=options,service=Service('C:/Users/J Narasimha Rao/Downloads/chromedriver_win32(1)/chromedriver.exe'))
browser.get('https://www.amazon.in/')
# time.sleep(5)
search=browser.find_element("name","field-keywords")
search.send_keys("Samsung")
search.submit()
print(browser.current_url)
