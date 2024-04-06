import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Список обозначений для использования вместо By:
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

driver.get("https://testautomationpractice.blogspot.com") # Откроем тестовую страницу
ELEMENT = driver.find_element("id", "Wikipedia1_wikipedia-search-input")
print(ELEMENT)
time.sleep(2)

driver.get("https://www.freeconferencecall.com/ru/ru/login") # Откроем тестовую страницу
time.sleep(2)
driver.find_element("id", "loginformsubmit").click() # Найдем элемент по id и кликнем по нему
time.sleep(2)


