# 1. Авторизоваться на сайте https://fix-online.sbis.ru/                                                                  (Например, "Регламент123"/"Регламент1231")
# 2. Перейти в реестр Контакты
# 3. Отправить сообщение самому себе
# 4. Убедиться, что сообщение появилось в реестре
# 5. Удалить это сообщение и убедиться, что удалили

from atf import *
from atf.pytest_core.base.case_ui import TestCaseUI
from atf.ui import Displayed, ContainsText, CountElements

from pages.Auth_page import *
from pages.Main_page import MainPage
from pages.Contacts_page import Contacts

class TestMessage(TestCaseUI):

    def test_message(self):
        sbis_site = self.config.get("SBIS_SITE")

        log(f'Перейти на {sbis_site}')
        self.browser.open(sbis_site)

        log("Авторизовываемся")
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.config.USER_LOGIN, self.config.USER_PASSWORD)

        log("Переходим в реестр Контакты")
        main_page = MainPage(self.driver)
        main_page.dropdown_accordion('Контакты')

        log("Ищем получателя")
        contacts_page = Contacts(self.driver)
        user_message, user_name = self.config.USER_MESSAGE, self.config.USER_NAME
        contacts_page.registry_slate.should_be(Displayed, wait_time=10)
        messages_before = contacts_page.dialog_list.size
        contacts_page.plus_btn.click()
        contacts_page.contacts_search.type_in(user_name)
        contacts_page.adressee_list.item(contains_text=user_name).click()

        log("Отправить сообщение получателю")
        contacts_page.msg_window.human_type_in(user_message)
        contacts_page.send_btn.click()
        contacts_page.close_btn.click()

        log("Проверяем появилось ли наше сообщение в реестре")
        contacts_page.dialog_list.should_be(CountElements(messages_before + 1))
        contacts_page.dialog_list.item(1).should_be(ContainsText(user_message))

        log("Удаляем сообщение")
        contacts_page.dialog_list.item(1).context_click()
        contacts_page.delete_btn.click()

        log("Проверяем удалилось ли")
        contacts_page.dialog_list.item(1).should_not_be(ContainsText(user_message))
        contacts_page.dialog_list.should_be(CountElements(messages_before))