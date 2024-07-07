import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def base_url():
    return "https://stellarburgers.nomoreparties.site"

@pytest.fixture(params=["chrome", "firefox"])
def setup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture()
def login_page(setup, base_url):
    from pages.login_page import LoginPage
    return LoginPage(setup, base_url)

@pytest.fixture()
def password_recovery_page(setup, base_url):  # передаем base_url
    from pages.password_recovery_page import PasswordRecoveryPage
    return PasswordRecoveryPage(setup, base_url)

@pytest.fixture()
def personal_account_page(setup, base_url):
    from pages.personal_account_page import PersonalAccountPage
    return PersonalAccountPage(setup, base_url)

@pytest.fixture()
def order_history_page(setup, base_url):
    from pages.order_history_page import OrderHistoryPage
    return OrderHistoryPage(setup, base_url)

@pytest.fixture()
def constructor_page(setup, base_url):
    from pages.constructor_page import ConstructorPage
    return ConstructorPage(setup, base_url)

@pytest.fixture()
def orders_feed_page(setup, base_url):
    from pages.orders_feed_page import OrdersFeedPage
    return OrdersFeedPage(setup, base_url)
