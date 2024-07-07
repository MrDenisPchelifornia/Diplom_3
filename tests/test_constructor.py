import pytest
import allure

@pytest.mark.usefixtures("setup")
class TestConstructor:

    # переход по клику на «Конструктор»,
    @allure.title('Переход в раздел "Коснтурктор"')
    def test_transfer_to_constructor_page(self, constructor_page, login_page, personal_account_page):
        constructor_page.open_url("login")
        login_page.login("denis_pcheliakov_8123@yandex.ru", "8123456")
        personal_account_page.go_to_personal_account()
        constructor_page.transfer_to_constructor_page()

        assert 'Соберите бургер' == constructor_page.get_text_on_constractor_page()

    # переход по клику на «Лента заказов»,
    @allure.title('Переход в раздел "Лента заказов"')
    def test_transfer_to_order_list(self, constructor_page):
        constructor_page.open_url("login")
        constructor_page.transfer_to_order_list()

        assert 'Лента заказов' == constructor_page.get_text_on_order_page()

    # если кликнуть на ингредиент, появится всплывающее окно с деталями,
    @allure.title('Проверка всплывающего ока с деталями об инградиенте при клике на него')
    def test_pop_up_with_details(self, constructor_page):
        constructor_page.open_url("")
        constructor_page.open_ingredient_details()

        assert constructor_page.get_text_on_details_cart_heading() == "Детали ингредиента"

    # всплывающее окно закрывается кликом по крестику,
    @allure.title('Проверка что всплывающее окно с деталями об инградиете закрывается на крестик')
    def test_close_pop_up_with_details(self, constructor_page):
        constructor_page.open_url("")
        constructor_page.open_ingredient_details()
        constructor_page.close_ingredient_details()

        assert 'Соберите бургер' == constructor_page.get_text_on_constractor_page()

    # при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,
    @allure.title('Проверка что счетчик инградиента увеличивается если добавить его в заказ')
    def test_add_ingredient_to_order(self, constructor_page):
        constructor_page.open_url("")
        constructor_page.add_ingredient_to_order()
        counter = constructor_page.get_ingredient_counter()

        assert counter == '2'

    # залогиненный пользователь может оформить заказ.
    @allure.title('Проверка оформелния заказа залогиненным пользователем')
    def test_submit_order_logged_in_user(self, login_page, constructor_page):
        login_page.open_url("login")
        login_page.login("denis_pcheliakov_8123@yandex.ru", "8123456")
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()

        assert "Ваш заказ начали готовить" == constructor_page.get_text_on_submit_window()
