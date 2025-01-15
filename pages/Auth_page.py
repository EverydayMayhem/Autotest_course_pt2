from atf.ui import Region, TextField, Button, ExactText

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, "[data-qa='auth-AdaptiveLoginForm__login'] input", "логин")
    password = TextField(By.CSS_SELECTOR, "[type = 'password']", "пароль")

    def auth(self, login: str, password: str):
        """Авторизация"""

        self.login.type_in(login + Keys.ENTER)
        self.login.should_be(ExactText(login))
        self.password.type_in(password + Keys.ENTER)

