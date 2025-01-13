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

from Auto_auth import *

class MainPage(Region):
    pass

class TaskPage(Region):
    pass


class TestTaskRegistry(TestCaseUI):

    def test_task_registry(self):
        sbis_site = self.config.get("SBIS_SITE")

        log(f"Переходим на сайт {sbis_site}")
        self.browser.open(sbis_site)

        log("Авторизовываемся")
        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        log("Переходим в реестр Задачи на вкладку В работе ")
        task_page = TaskPage(self.driver)
