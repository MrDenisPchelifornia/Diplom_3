from selenium.webdriver.common.by import By

class OrderHistoryLocators:
    ORDER_IN_HISTORY = lambda order_id: (By.CSS_SELECTOR, f"order-item[data-id='{order_id}']")

