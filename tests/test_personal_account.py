import pytest
import allure
from data.all_data import User, Handle, Asserts

@pytest.mark.usefixtures("setup")
class TestPersonalAccount:

    @allure.title('Проверка перехода в раздел "Личный кабинет"')
    def test_navigation_to_account(self, login_page, personal_account_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.email, User.password)
        personal_account_page.go_to_personal_account()

        assert personal_account_page.get_text_from_profile_button() == Asserts.profile_button_text_on_account_page

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_navigation_to_order_history(self, login_page, personal_account_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.email, User.password)
        personal_account_page.go_to_personal_account()
        personal_account_page.go_to_order_history()

        assert personal_account_page.get_text_from_history_order() == Asserts.order_status_text_in_history

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, login_page, personal_account_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.email, User.password)
        personal_account_page.go_to_personal_account()
        personal_account_page.logout()

        assert personal_account_page.get_text_after_logout() == Asserts.enter_heading_on_login_page