# 1. Авторизоваться на сайте https://fix-online.sbis.ru/                                                                  (Например, "Регламент123"/"Регламент1231")
# 2. Перейти в реестр Контакты
# 3. Отправить сообщение самому себе
# 4. Убедиться, что сообщение появилось в реестре
# 5. Удалить это сообщение и убедиться, что удалили

from atf import *
from atf.pytest_core.base.case_ui import TestCaseUI
from atf.ui import Region, TextField, Button, ExactText, CustomList, UrlExact, Enabled, Displayed, Element, \
    ContainsText, CountElements

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, "[data-qa='auth-AdaptiveLoginForm__login'] input", "логин")
    password = TextField(By.CSS_SELECTOR, "[type = 'password']", "пароль")
    enter_btn = Button(By.CSS_SELECTOR, "[data-qa='auth-AdaptiveLoginForm__checkSignInTypeButton']", "кнопка авторизации")

class MainPageOnline(Region):
    main_contact_menu = Button(By.CSS_SELECTOR, "[data-qa='Контакты']", "Контакты в главном аккордеоне")

class Contacts(Region):
    plus_btn = Button(By.CSS_SELECTOR, "[data-qa='sabyPage-addButton']", "Кнопка плюс")
    registry_slate = Element(By.CSS_SELECTOR, ".msg-dialogs-detail", "Контентная область")
    dialog_list = CustomList(By.CSS_SELECTOR, ".msg-dialogs-item", "Сообщения")
    contacts_search = TextField(By.CSS_SELECTOR, ".addressee-selector-popup__browser-search-area-wrapper input", "Строка поиска")
    adressee_list = CustomList(By.CSS_SELECTOR, ".msg-addressee-selector__addressee", "Список получателей")
    msg_window = TextField(By.CSS_SELECTOR, "[data-qa='textEditor_slate_Field']", "Поле ввода сообщения")
    send_btn = Button(By.CSS_SELECTOR, "[data-qa='msg-send-editor__send-button']", "Кнопка отправить")
    close_btn = Button(By.CSS_SELECTOR, "[data-qa='controls-stack-Button__close']", "Кнопка закрыть")
    delete_btn = Button(By.CSS_SELECTOR, "[title = 'Перенести в удаленные']", "Кнопка удаления из реестра")

class Test(TestCaseUI):

    def test(self):
        sbis_site = self.config.get("SBIS_SITE")

        log(f'Перейти на {sbis_site}')
        self.browser.open(sbis_site)

        log("Авторизовываемся")
        auth_page = AuthPage(self.driver)
        user_login, user_password = self.config.get("USER_LOGIN"), self.config.get("USER_PASSWORD")
        auth_page.login.type_in(user_login)
        auth_page.enter_btn.click()
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

        log("Переходим в реестр Контакты")
        main_page = MainPageOnline(self.driver)
        main_page.main_contact_menu.click()
        self.browser.should_be(UrlExact("https://fix-online.sbis.ru/page/dialogs"))

        log("Ищем получателя")
        contacts_page = Contacts(self.driver)
        user_message, user_name = self.config.get("USER_MESSAGE"), self.config.get("USER_NAME")
        contacts_page.registry_slate.should_be(Displayed)
        messages_before = contacts_page.dialog_list.size
        contacts_page.plus_btn.click()
        contacts_page.contacts_search.type_in(user_name)
        contacts_page.adressee_list.item(contains_text=user_name).click()

        log("Отправить сообщение получателю")
        contacts_page.msg_window.human_type_in(user_message)
        contacts_page.send_btn.click()
        contacts_page.close_btn.click()

        log("Проверяем появилось ли наше сообщение в реестре")
        contacts_page.dialog_list.should_be(CountElements(messages_before+1))
        contacts_page.dialog_list.item(1).should_be(ContainsText(user_message))

        log("Удаляем сообщение")
        contacts_page.dialog_list.item(1).context_click()
        contacts_page.delete_btn.click()

        log("Проверяем удалилось ли")
        contacts_page.dialog_list.item(1).should_not_be(ContainsText(user_message))
        contacts_page.dialog_list.should_be(CountElements(messages_before))