import allure
from pages.base_page import BasePage
from locators.orders_feed_locators import OrdersFeedLocators
import time
from data.all_data import Assert

class OrdersFeedPage(BasePage):
    @allure.step("")
    def get_text_on_order_information(self):
        return self.find_element(OrdersFeedLocators.COMPOSITION_OF_ORDER).text

    @allure.step("")
    def open_order_details(self):
        self.click_element(OrdersFeedLocators.FIRST_ELEMENT_IN_CLASS)

    @allure.step("")
    def get_order_number(self):
        return self.find_element(OrdersFeedLocators.ORDER_NUMBER).text

    @allure.step("")
    def get_order_list(self):
        return self.find_element(OrdersFeedLocators.ORDERS_LIST).text

    @allure.step("")
    def get_all_times_count(self):
        return self.find_element(OrdersFeedLocators.ALL_TIMES_COUNTER).text

    @allure.step("")
    def get_todays_count(self):
        return self.find_element(OrdersFeedLocators.TODAYS_COUNTER).text

    @allure.step("")
    def go_to_history(self):
        self.click_element(OrdersFeedLocators.ACCOUNT_BUTTON)
        self.click_element(OrdersFeedLocators.ORDER_HISTORY_TAB)

    @allure.step("")
    def get_number_order_in_progress(self, timeout=8):
        start_time = time.time()
        while time.time() - start_time < timeout:
            order_in_progress = self.find_element(OrdersFeedLocators.IN_PROGRESS_NUMBER).text
            if order_in_progress != Assert.no_progress_orders:
                return order_in_progress
