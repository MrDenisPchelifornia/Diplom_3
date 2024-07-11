import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    @allure.step("")
    def login(self, email, password):
        self.enter_text(LoginLocators.EMAIL_INPUT, email)
        self.enter_text(LoginLocators.PASSWORD_INPUT, password)
        self.click_element(LoginLocators.LOGIN_BUTTON)



