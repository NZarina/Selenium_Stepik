import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://hyperskill.org/tracks")

time.sleep(3)

# driver.find_elements("class name", "nav-link") # находим элементы по классу
# print(len(driver.find_elements("class name", "nav-link"))) # печатаем длину списка элементов

driver.find_elements("class name", "nav-link")[2].click() # находим элемент по номеру индекса и кликаем
time.sleep(3)


