from selenium import webdriver
from selenium.webdriver.firefox.service import Service

cdp = 'C:/Users/hp/Downloads/geckodriver.exe'
service = Service(executable_path=cdp)
driver = webdriver.Firefox(service=service)
driver.get('http://google.com')
print(driver.title)
driver.quit()