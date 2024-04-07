import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 1.На странице https://testautomationpractice.blogspot.com/ найти иконку Wikipedia по имени класса
driver.get("https://testautomationpractice.blogspot.com")

driver.find_element("class name", "wikipedia-search-wiki-link")

# 2.Найти поле ввода Wikipedia по id
driver.find_element("id", "Wikipedia1_wikipedia-search-input")

# 3.Найти кнопку поиска Wikipedia по классу
driver.find_element("class name", "wikipedia-search-input")

# 4. Найти любой другой элемент на странице по тегу
print(len(driver.find_elements("tag name", "h2")))
print(driver.find_elements("tag name", "h2")[1])