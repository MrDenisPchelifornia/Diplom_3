from selenium.webdriver.common.by import By

class OrdersFeedLocators:
    FIRST_ELEMENT_IN_CLASS = (By.CSS_SELECTOR, ".OrderHistory_listItem__2x95r:nth-of-type(1)")
    ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
    ORDER_HISTORY_TAB = (By.LINK_TEXT, "История заказов")
    ORDER_NUMBER = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text "
                              "text_type_digits-large mb-8']")
    ORDERS_LIST = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    ALL_TIMES_COUNTER = (By.XPATH, "/html/body/div/div/main/div/div/div/div[2]/p[2]")
    TODAYS_COUNTER = (By.XPATH, "/html/body/div/div/main/div/div/div/div[3]/p[2]")
    IN_PROGRESS_NUMBER = (By.XPATH, ".//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    COMPOSITION_OF_ORDER = (By.XPATH, "/html/body/div/div/section[2]/div[1]/div/p[3]")

