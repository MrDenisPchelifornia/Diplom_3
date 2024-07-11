import data
import allure
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators

class PersonalAccountPage(BasePage):

    @allure.step("")
    def go_to_personal_account(self):
        self.click_element(PersonalAccountLocators.ACCOUNT_BUTTON)

    @allure.step("")
    def go_to_order_history(self):
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_TAB)

    @allure.step("")
    def logout(self):
        self.click_element(PersonalAccountLocators.LOGOUT_BUTTON)

    @allure.step("")
    def get_text_from_profile_button(self):
        return self.find_element(PersonalAccountLocators.PROFILE_BUTTON).text

    @allure.step("")
    def get_text_from_history_order(self):
        return self.find_element(PersonalAccountLocators.THE_ORDER_HISTORY).text

    @allure.step("")
    def get_text_after_logout(self):
        return self.find_element(PersonalAccountLocators.ENTER_TITLE).text