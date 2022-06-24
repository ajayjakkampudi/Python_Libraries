from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path=r"C:\Users\J Narasimha Rao\Downloads\chromedriver_win32 (1)\chromedriver.exe")
driver.get('https://www.hotstar.com/')
driver.find_element(By.XPATH,'//*[@id="searchField"]').send_keys("Endgame")
#element.send_keys('Endgame')
