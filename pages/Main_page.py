from atf.ui import Region, Button, CustomList
from selenium.webdriver.common.by import By
from atf import *

class MainPage(Region):
    task_menu = Button(By.CSS_SELECTOR, "[data-qa='Задачи']", "Задачи в синем аккордеоне")
    task_submenu_head = Button(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__head", "Задачи в подменю аккордеона")
    contact_menu = Button(By.CSS_SELECTOR, "[data-qa='Контакты']", "Контакты в главном аккордеоне")
    contact_submenu_head = Button(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__head",
                                  "Контакты в выпадающем аккордеоне")
    main_menu = CustomList(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]', 'Основной аккордеон')
    main_submenu = CustomList(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__item', 'Разворачивающееся меню')
    head_title = Button(By.CSS_SELECTOR, '[name="headTitle"]', 'Главный пункт разворачивающегося меню')

    def dropdown_accordion(self, registry_name: str, subregistry_name = None):
        """Выбор пункта \ подпункта аккордеона.
        :param registry_name - Имя пункта аккордеона
        :param subregistry_name - Имя подпункта аккордеона
        """
        if subregistry_name is None:
            subregistry_name = ''

        self.main_menu.item(with_text=registry_name).click()
        delay(1)

        if self.main_submenu.is_displayed and subregistry_name == '':
            self.head_title.click()
        else:
            self.main_submenu.item(with_text=subregistry_name).click()