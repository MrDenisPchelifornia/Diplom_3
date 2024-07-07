from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    RECOVER_PASSWORD_BUTTON = (By.LINK_TEXT, "Восстановить пароль")
    EMAIL_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset/div/div")
    EMAIL_INPUT2 = (By.XPATH, "/html/body/div/div/main/div/form/fieldset/div/div/input")
    RECOVER_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/button")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/div")
    PASSWORD_FIELD_PARENT = (By.XPATH, ".//input[contains(@type,'text')]/parent::div")
    VISIBLE_PASSWORD_FIELD = (
        By.XPATH,
        ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")  # глаз
    RECOVERY_PASSWORD_FIRST_SCREEN_HEADING = (By.XPATH, "//div/main/div/h2")
    RECOVERY_PASSWORD_SECOND_SCREEN_PLACEHOLDER = (By.XPATH, "//div/main/div/form/fieldset[2]/div/div/label")
