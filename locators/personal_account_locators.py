from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
    ORDER_HISTORY_TAB = (By.LINK_TEXT, "История заказов")
    LOGOUT_BUTTON = (By.XPATH,"//button[contains(.,'Выход')]")
    PROFILE_BUTTON = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    THE_ORDER_HISTORY = (By.XPATH, "/html/body/div/div/main/div/div/div/ul/li[1]/a/p")
    ENTER_TITLE = (By.XPATH,"//h2[contains(.,'Вход')]")
