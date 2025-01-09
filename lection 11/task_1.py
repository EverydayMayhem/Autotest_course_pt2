# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

tensor_about = 'https://tensor.ru/about'
driver = webdriver.Chrome()

try:
    time.sleep(1)
    driver.get('https://sbis.ru/') # 1. Переходим на разводяшую
    # 2. Ищем раздел Контакты через класс (раздел находится в подвале) :
    # .sbisru-Footer__list-item [href='/contacts']
    contacts = driver.find_element(By.CSS_SELECTOR, ".sbisru-Footer__list-item [href='/contacts']")
    # перед кликом неплохо было бы переместиться вниз страницы
    contacts.click()
    time.sleep(5)
    # когда переходим на страницу Контакты, есть три вкладки
    # и лого Тензора находится на двух из них - "Клиентам" и "Партнерам"
    # в задаче не уточняется, поэтому возьмем лого из вкладки "Клиентам"
    tensor_banner = driver.find_elements(By.CSS_SELECTOR, "[href='https://tensor.ru/']")
    tensor_banner[0].click()
    time.sleep(5)
    # при клике открывается новая вкладка браузера, переключимся на неё
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    #после переключения, найдем блок "Сила в людях" и убедимся, что он видимый
    people_power_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4')
    people_power_block.location_once_scrolled_into_view
    assert people_power_block.is_displayed(), 'Нет блока "Сила в людях" о Тензоре'
    time.sleep(5)
    # кликаем по кнопке "Подробнее" в этом блоке
    about_btn = driver.find_element(By.CSS_SELECTOR, "[href = '/about'].tensor_ru-link")
    about_btn.click()
    time.sleep(5)
    assert driver.current_url == tensor_about, 'Перешли не туда или поменялась ссылка'
finally:
    driver.quit()
