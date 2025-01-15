from atf.ui import Region, TextField, Button, CustomList, Element
from selenium.webdriver.common.by import By

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