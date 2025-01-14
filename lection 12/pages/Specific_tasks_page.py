from atf.ui import Region, Element
from selenium.webdriver.common.by import By

class SpecificTask(Region):
    executor = Element(By.CSS_SELECTOR, "[data-qa='SelectedCollection__item']", "Исполнитель задачи")
    date = Element(By.CSS_SELECTOR, "[data-qa='edo3-Document_docDate']", "Дата задачи")
    number = Element(By.CSS_SELECTOR, "[data-qa='edo3-Document_docNumber']", "Номер задачи")
    author = Element(By.CSS_SELECTOR, "[data-qa='edo3-Sticker__mainInfo']", "Автор задачи")
    description = Element(By.CSS_SELECTOR, "[name='taskDescrAttr']", "Описание задачи")