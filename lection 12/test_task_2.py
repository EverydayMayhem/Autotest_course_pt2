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
from atf.ui import UrlExact, Displayed, CountElements

from pages.Auth_page import *
from pages.Task_page import TaskPage
from pages.Main_page import MainPage


class TestTaskRegistry(TestCaseUI):

    def test_task_registry(self):
        sbis_site = self.config.get("SBIS_SITE")

        log(f"Переходим на сайт {sbis_site}")
        self.browser.open(sbis_site)

        log("Авторизовываемся")
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.config.USER_LOGIN, self.config.USER_PASSWORD)

        log("Переходим в реестр задач через аккордеон")
        main_page = MainPage(self.driver)
        main_page.task_menu.click()
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
