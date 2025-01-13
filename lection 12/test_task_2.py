# 1. Авторизоваться на сайте https://fix-online.sbis.ru/
# 2. Перейти в реестр Задачи на вкладку "В работе"
# 3. Убедиться, что выделена папка "Входящие" и стоит маркер.
# 4. Убедиться, что папка не пустая (в реестре есть задачи)
# 5. Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# 6. Создать новую папку и перейти в неё
# 7. Убедиться, что она пустая
# 8. Удалить новую папку, проверить, что её нет в списке папок

from atf import *
from atf.pytest_core.base.case_ui import TestCaseUI
from atf.ui import Region, TextField, Button, ExactText, CustomList, UrlExact, Enabled, Displayed, Element, \
    ContainsText, CountElements, UrlContains

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from Auth_page import *

class MainPage(Region):
    task_accordeon = Button(By.CSS_SELECTOR, "[data-qa='Задачи']", "Задачи в синем аккордеоне")
    task_submenu_head = Button(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__head", "Задачи в подменю аккордеона")

class TaskPage(Region):
    work_tabs = CustomList(By.CSS_SELECTOR, "[data-qa='controls-Tabs__item-element']", "Вкладки у папки Входящие")
    left_filters = CustomList(By.CSS_SELECTOR, ".controls-ListEditor__columns", "Фильтры в аккордеоне")
    in_work_selected = Button(By.CSS_SELECTOR, "[data-qa='marker']+[title='Входящие']", "Маркированная папка Входящие")
    task_list = CustomList(By.CSS_SELECTOR, ".edws-MainColumn", "Список входящих задач")
    regular_selected = Button(By.CSS_SELECTOR, "[data-qa='marker']+[title='Регулярные']", "Маркированная папка Регулярные")
    regular_folder = Button(By.CSS_SELECTOR, "[title='Регулярные']", "Папка Регулярные")
    plus_btn = Button(By.CSS_SELECTOR, "[data-qa='sabyPage-addButton']", "Кнопка плюс")
    plus_btn_item = CustomList(By.CSS_SELECTOR, "[data-qa='item']", "Варианты создания папок")
    dialog_popup = Element(By.CSS_SELECTOR, ".controls-DialogTemplate", "Попап создания папки")
    dialog_popup_naming = TextField(By.CSS_SELECTOR, ".controls-DialogTemplate input", "Поле ввода названия папки")
    text_buttons = CustomList(By.CSS_SELECTOR, ".controls-BaseButton__text", "Кнопки с текстом, по которым будем искать нашу")
    empty_folder_hint = Element(By.CSS_SELECTOR, "[data-qa='hint-EmptyView__title'", "Пустая папка")
    delete_folder_btn = Button(By.CSS_SELECTOR, "[title='Удалить папку']", "Кнопка 'Удалить папку'")
    confirm_button = Button(By.CSS_SELECTOR, "[data-qa='controls-ConfirmationDialog__button-true']", "Кнопка Да")

class TestTaskRegistry(TestCaseUI):

    def test_task_registry(self):
        sbis_site = self.config.get("SBIS_SITE")

        log(f"Переходим на сайт {sbis_site}")
        self.browser.open(sbis_site)

        log("Авторизовываемся")
        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        log("Переходим в реестр задач через аккордеон")
        main_page = MainPage(self.driver)
        main_page.task_accordeon.click()
        main_page.task_submenu_head.should_be(Displayed)
        main_page.task_submenu_head.click()

        log("В реестре задач перейти на вкладку 'В работе' ")
        task_page = TaskPage(self.driver)
        task_page.work_tabs.item(with_text="В работе").click()
        self.browser.should_be(UrlExact(f'{sbis_site}page/tasks-in-work'))

        log("Проверяем, что что выделена папка 'Входящие' и стоит маркер")
        task_page.left_filters.should_be(Displayed)
        task_page.in_work_selected.should_be(Displayed)

        log("Проверяем, что реестр входящих задач не пустой")
        task_page.task_list.should_not_be(CountElements(0))

        log("Переходим в папку 'Регулярные', убедиться, что теперь она выделена, а со 'Входящие' выделение снято")
        task_page.regular_folder.click()
        task_page.work_tabs.should_not_be(Displayed)
        task_page.regular_selected.should_be(Displayed)
        task_page.in_work_selected.should_not_be(Displayed)

        log("Создадим новую папку по кнопке плюс")
        task_page.plus_btn.click()
        task_page.plus_btn_item.should_be(Displayed, wait_time=2)
        task_page.plus_btn_item.item(with_text='Папка').click()

        log("Проверяем что появился попап создания папки")
        task_page.dialog_popup.should_be(Displayed)

        log("Создаем папку с именем Новая папка")
        folder_name = self.config.get("FOLDER_NAME")
        task_page.dialog_popup_naming.type_in(folder_name)
        task_page.text_buttons.item(with_text="Сохранить").click()

        log(f"Проверяем что появилась папка с именем {folder_name}")
        task_page.left_filters.item(with_text=folder_name).click()

        log("Проверяем, что папка пустая")
        task_page.empty_folder_hint.should_be(Displayed)

        log("Удаляем новую папку")
        task_page.left_filters.item(with_text=folder_name).context_click()
        task_page.delete_folder_btn.click()
        task_page.confirm_button.click()

        log("Проверяем что удалилась")
        task_page.left_filters.item(with_text=folder_name).should_not_be(Displayed)
