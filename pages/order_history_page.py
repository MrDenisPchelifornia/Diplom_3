import allure
from pages.base_page import BasePage
from locators.order_history_locators import OrderHistoryLocators

class OrderHistoryPage(BasePage):
    @allure.step("")
    def check_order_in_history(self, order_id):
        return self.find_element(OrderHistoryLocators.ORDER_IN_HISTORY(order_id))

