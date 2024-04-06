import time
# 1. Инициализировать драйвер (любой, попробуйте Firefox) p.s: не забудьте его установить.
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# 2. Открыть любую страницу, например: vk.com.
driver.get("https://vk.com/")
time.sleep(3)

# 3. Получить и вывести title в консоль.
title = driver.title
print(title)

# 4. Открыть любую другую страницу, например: ya.ru.
driver.get("https://ya.ru")
time.sleep(3)

# 5. Получить и вывести title в консоль.
title = driver.title
print(title)

# 6. Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно.
driver.back()
url = driver.current_url
assert url == "https://vk.com/", "Не выполнился возврат на ВК"
time.sleep(3)

# 7. Сделать рефреш страницы.
driver.refresh()
time.sleep(3)

# 8. Получить и вывести URL-адрес текущей страницы.
url = driver.current_url
print("URL текущей страницы: ", url)

# 9. Вернуться "вперед" на страницу из пункта 4.
driver.forward()
time.sleep(3)

# 10. Убедиться, что URL-адрес изменился.
assert driver.current_url == "https://ya.ru",  "Не выполнился возврат на Яндекс"

time.sleep(5)