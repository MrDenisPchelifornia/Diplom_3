import allure
from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from seletools.actions import drag_and_drop

class ConstructorPage(BasePage):
    @allure.step("")
    def transfer_to_constructor_page(self):
        self.click_element(ConstructorLocators.CONSTRUCTOR_BUTTON)

    @allure.step("")
    def transfer_to_order_list(self):
        self.click_element(ConstructorLocators.ORDER_LIST_BUTTON)

    @allure.step("")
    def add_ingredient_to_order(self):
        source = self.find_element(ConstructorLocators.FIRST_BUN_FROM_BUNS)
        target = self.find_element(ConstructorLocators.ORDER_AREA)
        drag_and_drop(self.driver, source, target)

    @allure.step("")
    def get_ingredient_counter(self):
        return self.find_element(ConstructorLocators.COUNT_OF_INGREDIENTS).text

    @allure.step("")
    def open_ingredient_details(self):
        self.click_element(ConstructorLocators.INGREDIENT)

    @allure.step("")
    def close_ingredient_details(self):
        return self.visibility_of_element(ConstructorLocators.CLOSE_DETAILS_BUTTON)
        self.click_element(ConstructorLocators.CLOSE_DETAILS_BUTTON)

    @allure.step("")
    def submit_order(self):
        self.click_element(ConstructorLocators.SUBMIT_ORDER_BUTTON)

    @allure.step("")
    def get_text_on_constractor_page(self):
        return self.find_element(ConstructorLocators.MAKE_BURGER_HEADING).text

    @allure.step("")
    def get_text_on_order_page(self):
        return self.find_element(ConstructorLocators.ORDER_LIST_HEADING).text

    @allure.step("")
    def get_text_on_details_cart_heading(self):
        return self.find_element(ConstructorLocators.DETAILS_OF_INGRADIENTS_HEADING).text

    @allure.step("")
    def get_text_on_submit_window(self):
        return self.find_element(ConstructorLocators.INFORMATION_ON_SUBMIT_WINDOW).text

    def wait_and_close_submit_modal_window(self):
        self.wait_submit_modal_window()
        self.close_submit_modal_window()

    def wait_submit_modal_window(self):
        return self.find_element(ConstructorLocators.SUBMIT_MODAL_WINDOW)

    def close_submit_modal_window(self):
        self.find_element(ConstructorLocators.CLOSE_MODAL_WINDOW_BUTTON).click()

