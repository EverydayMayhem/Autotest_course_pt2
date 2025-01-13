from atf.ui import Region, TextField, Button, ExactText

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, "[data-qa='auth-AdaptiveLoginForm__login'] input", "логин")
    password = TextField(By.CSS_SELECTOR, "[type = 'password']", "пароль")
    enter_btn = Button(By.CSS_SELECTOR, "[data-qa='auth-AdaptiveLoginForm__checkSignInTypeButton']",
                       "кнопка авторизации")

    def authorize(self):
        auth_page = AuthPage(self.driver)
        user_login, user_password = self.config.get("USER_LOGIN"), self.config.get("USER_PASSWORD")
        auth_page.login.type_in(user_login)
        auth_page.enter_btn.click()
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

