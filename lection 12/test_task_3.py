# Предварительные действия (Создайте эталонную задачу, заполнив обязательные поля)
# 1. Авторизоваться на сайте https://fix-online.sbis.ru/
# 2. Откройте эталонную задачу по прямой ссылке в новой вкладке браузера
# 3. Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА",
# где ДАТА и НОМЕР - это ваши эталонные значения
# 4. Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями

from atf import *
from atf.pytest_core.base.case_ui import TestCaseUI
from atf.ui import Displayed, TitleExact

from pages.Auth_page import *
from pages.Main_page import MainPage
from pages.Specific_tasks_page import SpecificTask


class TestSpecificTask(TestCaseUI):

    def test_my_task(self):
        sbis_site = self.config.get("SBIS_SITE")

        log(f"Переходим на сайт {sbis_site}")
        self.browser.open(sbis_site)

        log("Авторизовываемся")
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.config.USER_LOGIN, self.config.USER_PASSWORD)
        main_page = MainPage(self.driver)
        main_page.task_menu.should_be(Displayed, wait_time=10)

        log("Открываем задачу в новой вкладке по прямой ссылке")
        self.browser.create_new_tab(self.config.get("TASK_LINK"))
        self.browser.switch_to_opened_window()

        log("Проверяем открылась ли страница")
        specific_task = SpecificTask(self.driver)
        specific_task.number.should_be(Displayed)

        log("Проверяем наименование вкладки")
        task_number = self.config.get('TASK_NUM')
        task_date = self.config.get('TASK_DATE')
        self.browser.should_be(TitleExact(f"Задача №{task_number} от {task_date}"))

        log("Проверяем, что на странице отображаются эталонные Дата, номер задачи, автор и исполнитель, описание")
        task_description = self.config.get('TASK_DESCRIPTION')
        task_author = self.config.get('TASK_AUTHOR')
        task_executor = self.config.get('TASK_EXECUTOR')
        task_date_full = self.config.get('TASK_DATE_FULL')
        specific_task.number.should_be(ExactText(task_number))
        specific_task.date.should_be(ExactText(task_date_full))
        specific_task.author.should_be(ExactText(task_author))
        specific_task.executor.should_be(ExactText(task_executor))
        specific_task.description.should_be(ExactText(task_description))
