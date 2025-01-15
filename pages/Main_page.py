from atf.ui import Region, Button
from selenium.webdriver.common.by import By


class MainPage(Region):
    task_menu = Button(By.CSS_SELECTOR, "[data-qa='Задачи']", "Задачи в синем аккордеоне")
    task_submenu_head = Button(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__head", "Задачи в подменю аккордеона")
    contact_menu = Button(By.CSS_SELECTOR, "[data-qa='Контакты']", "Контакты в главном аккордеоне")
    contact_submenu_head = Button(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__head", "Контакты в выпадающем аккордеоне")