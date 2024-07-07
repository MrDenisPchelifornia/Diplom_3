import pytest
import allure

@pytest.mark.usefixtures("setup")
class TestPersonalAccount:

    # переход по клику на «Личный кабинет»,
    @allure.title('Проверка перехода в раздел "Личный кабинет"')
    def test_navigation_to_account(self, login_page, personal_account_page):
        login_page.open_url("login")
        login_page.login("denis_pcheliakov_8123@yandex.ru", "8123456")
        personal_account_page.go_to_personal_account()

        assert personal_account_page.get_text_from_profile_button() == "Профиль"

    # переход в раздел «История заказов»,
    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_navigation_to_order_history(self, login_page, personal_account_page):
        login_page.open_url("login")
        login_page.login("denis_pcheliakov_8123@yandex.ru", "8123456")
        personal_account_page.go_to_personal_account()
        personal_account_page.go_to_order_history()

        assert personal_account_page.get_text_from_history_order() == "Выполнен"

    # выход из аккаунта.
    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, login_page, personal_account_page):
        login_page.open_url("login")
        login_page.login("denis_pcheliakov_8123@yandex.ru", "8123456")
        personal_account_page.go_to_personal_account()
        personal_account_page.logout()

        assert 'Вход' == personal_account_page.get_text_after_logout()