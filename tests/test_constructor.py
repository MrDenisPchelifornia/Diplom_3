import pytest
import allure
from data.all_data import User, Handle, Asserts

@pytest.mark.usefixtures("setup")
class TestConstructor:

    @allure.title('Переход в раздел "Коснтурктор"')
    def test_transfer_to_constructor_page(self, constructor_page, login_page, personal_account_page):
        constructor_page.open_url(Handle.login_handle)
        login_page.login(User.email, User.password)
        personal_account_page.go_to_personal_account()
        constructor_page.transfer_to_constructor_page()

        assert constructor_page.get_text_on_constractor_page() == Asserts.expect_constructor_heading

    @allure.title('Переход в раздел "Лента заказов"')
    def test_transfer_to_order_list(self, constructor_page):
        constructor_page.open_url(Handle.login_handle)
        constructor_page.transfer_to_order_list()

        assert constructor_page.get_text_on_order_page() == Asserts.expect_order_page_heading

    @allure.title('Проверка всплывающего ока с деталями об инградиенте при клике на него')
    def test_pop_up_with_details(self, constructor_page):
        constructor_page.open_url()
        constructor_page.open_ingredient_details()

        assert constructor_page.get_text_on_details_cart_heading() == Asserts.expect_details_cart_heading

    @allure.title('Проверка что всплывающее окно с деталями об инградиете закрывается на крестик')
    def test_close_pop_up_with_details(self, constructor_page):
        constructor_page.open_url()
        constructor_page.open_ingredient_details()
        constructor_page.close_ingredient_details()

        assert constructor_page.get_text_on_constractor_page() == Asserts.expect_constructor_heading

    @allure.title('Проверка что счетчик инградиента увеличивается если добавить его в заказ')
    def test_add_ingredient_to_order(self, constructor_page):
        constructor_page.open_url()
        constructor_page.add_ingredient_to_order()
        counter = constructor_page.get_ingredient_counter()

        assert counter == Asserts.expect_cont_of_ingredient

    @allure.title('Проверка оформелния заказа залогиненным пользователем')
    def test_submit_order_logged_in_user(self, login_page, constructor_page):
        login_page.open_url(Handle.login_handle)
        login_page.login(User.email, User.password)
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()

        assert constructor_page.get_text_on_submit_window() == Asserts.expect_submit_window_heading
