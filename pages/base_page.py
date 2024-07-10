import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    @allure.step("")
    def find_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        ) and self.visibility_of_element(locator)

    @allure.step("")
    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.visibility_of_element(locator).click()

    @allure.step("")
    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("")
    def open_url(self, endpoint=""):
        self.driver.get(f"{self.base_url}/{endpoint}")

    @allure.step("")
    def drag_and_drop(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("")
    def visibility_of_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("")
    def get_current_url(self):
        return self.driver.current_url




