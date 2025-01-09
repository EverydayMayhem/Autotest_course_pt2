# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains


driver = webdriver.Chrome()
sbis_fix = 'https://fix-online.sbis.ru/'
sbis_test = 'https://test-online.sbis.ru/'
try:
    driver.maximize_window()

    print(f'Перейти на {sbis_fix}')
    driver.get(sbis_fix)
    time.sleep(1)

    print('Авторизоваться')
    sleep(1)
    user_login, user_password = 'Proverka95', 'Proverka11'
    #login = driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"]')
    login = driver.find_element(By.CSS_SELECTOR, "[data-qa='auth-AdaptiveLoginForm__login'] input")
    # если использовать просто data-qa без input, то send_keys() не работает

    login.click()
    login.send_keys(user_login)
    time.sleep(1)

    login_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='auth-AdaptiveLoginForm__checkSignInTypeButton']")
    login_btn.click()
    time.sleep(1)

    password = driver.find_element(By.CSS_SELECTOR, "[type = 'password']")
    password.send_keys(user_password, Keys.ENTER)
    time.sleep(11)

    print('Перейти в "Контакты"')
    contact_registry = driver.find_element(By.CSS_SELECTOR, "[data-qa='Контакты']")
    contact_registry.click()
    time.sleep(2)

    contact_sub_btn = driver.find_element(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__headTitle")
    contact_sub_btn.click()
    time.sleep(10)

    print('Отправить сообщение себе')
    user_message = 'Дай денег'
    user_name = 'Вилинский Андрей Александрович'

    plus_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='sabyPage-addButton']")
    plus_btn.click()
    time.sleep(3)

    search_field = driver.find_elements(By.CSS_SELECTOR, "[data-qa='controls-Render__field']>input")
    # на странице две строки поиска - одна реестровая, вторая - на выезжающей панели. Нам нужна вторая
    search_field[0].send_keys(user_name)
    time.sleep(1)

    adressee_list = driver.find_elements(By.CSS_SELECTOR, "[class='msg-addressee-selector__addressee']")
    adressee_list[0].click()
    time.sleep(2)

    msg_window = driver.find_element(By.CSS_SELECTOR, "[data-qa='textEditor_slate_Field']")
    msg_window.send_keys(user_message)
    time.sleep(0.5)

    send_msg_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='msg-send-editor__send-button']")
    send_msg_button.click()
    time.sleep(1)

    close_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='controls-stack-Button__close']")
    close_btn.click()
    time.sleep(3)

    print("Проверяем появление сообщения в реестре")
    registry_slate = driver.find_element(By.CSS_SELECTOR, ".msg-dialogs-detail__layout-content")
    assert user_message in registry_slate.text, 'Новое сообщение не появилось'

    print("Контекстное меню на последнем сообщении")
    messages = driver.find_elements(By.CSS_SELECTOR, ".msg-dialogs-detail__layout-content [data-qa='item']")
    last_message = messages[0]
    action_chains = ActionChains(driver)
    action_chains.context_click(last_message)
    action_chains.perform()
    time.sleep(1)

    print("Удаляем сообщение через контекстное меню")
    delete_button = driver.find_element(By.CSS_SELECTOR, "[title = 'Перенести в удаленные']")
    delete_button.click()
    time.sleep(2)

    print("Проверяем удалилось ли")
    assert user_message not in registry_slate.text, 'Сообщение не удалилось'
finally:
    driver.quit()