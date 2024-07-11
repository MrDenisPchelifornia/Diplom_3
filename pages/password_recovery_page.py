import allure
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators

class PasswordRecoveryPage(BasePage):

    @allure.step("")
    def transfer_recovery_password_page(self):
        self.click_element(PasswordRecoveryLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step("")
    def recover_password(self, email):
        self.enter_text(PasswordRecoveryLocators.EMAIL_INPUT, email)
        self.click_element(PasswordRecoveryLocators.RECOVER_BUTTON)

    @allure.step("")
    def toggle_show_password(self):
        self.click_element(PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Получаем родительский класс')
    def get_eye_button(self):
        return self.find_element(PasswordRecoveryLocators.PASSWORD_FIELD_PARENT)

    @allure.step('Присваиваем переменной родительский класс')
    def assign_parent_class(self):
        return self.find_element(PasswordRecoveryLocators.VISIBLE_PASSWORD_FIELD)

    @allure.step("")
    def get_text_head_recovery_password_first_screen(self):
        return self.find_element(PasswordRecoveryLocators.RECOVERY_PASSWORD_FIRST_SCREEN_HEADING).text

    @allure.step("")
    def get_text_second_screen_placeholder(self):
        return self.find_element(PasswordRecoveryLocators.RECOVERY_PASSWORD_SECOND_SCREEN_PLACEHOLDER).text
