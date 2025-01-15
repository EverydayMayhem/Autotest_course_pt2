from atf.ui import Region, Button, Element, CustomList, TextField
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