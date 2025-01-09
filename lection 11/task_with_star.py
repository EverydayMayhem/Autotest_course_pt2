# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import os
import time
import glob

from selenium import webdriver
from selenium.webdriver.common.by import By

params = {'behavior' : 'allow', 'downloadPath' : os.getcwd()}
sbis_site = 'https://sbis.ru'
driver = webdriver.Chrome()
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

try:
    driver.maximize_window()

    print(f'Переходим на {sbis_site}')
    driver.get(sbis_site)
    time.sleep(4)

    print('Переходим в раздел поддержки')
    support_tab = driver.find_element(By.CSS_SELECTOR, "[href='/support'].sbisru-Header__menu-link")
    support_tab.click()
    time.sleep(2)

    print('Жмем Скачать')
    download_tab = driver.find_element(By.CSS_SELECTOR, "[href='/download?tab=plugin&innerTab=default']")
    download_tab.click()
    time.sleep(2)

    print('Берем самую верхнюю ссылку (Веб-установщик) и скачиваем файл')
    download_link = driver.find_elements(By.CSS_SELECTOR, ".sbis_ru-DownloadNew-loadLink")
    download_link[0].click()
    time.sleep(5)

    file_path = glob.glob(rf'{os.getcwd()}\\sbisplugin*')
    assert file_path, 'Не скачан файл'

    file_size = os.stat(file_path[0]).st_size
    print(f'Размер скачиваемого файла: {file_size / 1048576 : .2f} MB')
finally:
    driver.quit()
    os.remove(file_path[0])