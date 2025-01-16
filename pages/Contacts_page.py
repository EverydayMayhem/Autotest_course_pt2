from atf.ui import Region, Button, Element, CustomList, TextField, Displayed
from selenium.webdriver.common.by import By


class Contacts(Region):
    plus_btn = Button(By.CSS_SELECTOR, "[data-qa='sabyPage-addButton']", "Кнопка плюс")
    registry_slate = Element(By.CSS_SELECTOR, ".msg-dialogs-detail", "Контентная область")
    dialog_list = CustomList(By.CSS_SELECTOR, ".msg-dialogs-item", "Сообщения")
    contacts_search = TextField(By.CSS_SELECTOR, ".addressee-selector-popup__browser-search-area-wrapper input",
                                "Строка поиска")
    adressee_list = CustomList(By.CSS_SELECTOR, ".msg-addressee-selector__addressee", "Список получателей")
    msg_window = TextField(By.CSS_SELECTOR, "[data-qa='textEditor_slate_Field']", "Поле ввода сообщения")
    send_btn = Button(By.CSS_SELECTOR, "[data-qa='msg-send-editor__send-button']", "Кнопка отправить")
    close_btn = Button(By.CSS_SELECTOR, "[data-qa='controls-stack-Button__close']", "Кнопка закрыть")
    delete_btn = Button(By.CSS_SELECTOR, "[title = 'Перенести в удаленные']", "Кнопка удаления из реестра")

    def send_message(self, recepient: str, message: str):
        """Отправка сообщения из реестра по кнопке плюс
        :param recepient - получатель сообщения
        :param message - сообщение
        """
        self.plus_btn.click()
        self.contacts_search.should_be(Displayed, wait_time=20)
        self.contacts_search.type_in(recepient)
        self.adressee_list.item(contains_text=recepient).click()
        self.msg_window.should_be(Displayed)
        self.msg_window.human_type_in(message)
        self.send_btn.click()
        self.close_btn.click()

    def check_new_message(self, message: str):
        """Проверяет последнее сообщение по тексту"""
        return self.dialog_list.item(with_text=message)

    def count_messages_registry(self):
        """Проверяет количество элементов в реестре (не счетчик)"""
        return self.dialog_list.size

    def delete_message(self, message: str):
        """Удаляет сообщение по тексту и проверяет удалилось ли"""
        self.dialog_list.item(contains_text=message).context_click()
        self.delete_btn.click()
        self.dialog_list.item(contains_text=message).should_not_be(Displayed)