from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    RECOVER_PASSWORD_BUTTON = (By.LINK_TEXT, "Восстановить пароль")
    EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']/../input")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(.,'Восстановить')]")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    PASSWORD_FIELD_PARENT = (By.XPATH, ".//input[contains(@type,'text')]/parent::div")
    VISIBLE_PASSWORD_FIELD = (
        By.XPATH,
        ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")  # глаз
    RECOVERY_PASSWORD_FIRST_SCREEN_HEADING = (By.XPATH, "//button[text()='Восстановить']")
    RECOVERY_PASSWORD_SECOND_SCREEN_PLACEHOLDER = (By.XPATH, "//button[text()='Сохранить']")
