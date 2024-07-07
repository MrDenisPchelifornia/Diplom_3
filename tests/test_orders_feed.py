import pytest
import allure

@pytest.mark.usefixtures("setup")
class TestOrdersFeed:

    # если кликнуть на заказ, откроется всплывающее окно с деталями,
    @allure.title('Проверка что по клику на заказ высплывает оконо с деталями о нем')
    def test_open_order_details(self, login_page, orders_feed_page):
        login_page.open_url("feed")
        orders_feed_page.open_order_details()
        composition = orders_feed_page.get_text_on_order_information()

        assert composition == "Cостав"

    # заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
    @allure.title('Проверка того что заказ из "Истории заказов" обображается в "Лента заказов"')
    def test_same_order_on_history_and_list(self, login_page, constructor_page, orders_feed_page):
        login_page.open_url("login")
        login_page.login("denis_pcheliakov_8123@yandex.ru", "8123456")
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()
        constructor_page.close_ingredient_details()
        orders_feed_page.open_url("feed")
        order_list = orders_feed_page.get_order_list()
        orders_feed_page.go_to_history()
        order_number = orders_feed_page.get_order_number()

        assert order_number in order_list

    #при создании нового заказа счётчик Выполнено за всё время увеличивается,
    @allure.title('Проверка что при создании наказа счетчик "Выполнено за все время" увеличивается')
    def test_order_all_times_counters_update(self, login_page, constructor_page, orders_feed_page):
        orders_feed_page.open_url("feed")
        all_times_count_before_order = orders_feed_page.get_all_times_count()
        login_page.open_url("login")
        login_page.login("denis_pcheliakov_8123@yandex.ru", "8123456")
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()
        constructor_page.close_ingredient_details()
        orders_feed_page.open_url("feed")
        all_times_count_after_order = orders_feed_page.get_all_times_count()

        assert all_times_count_before_order < all_times_count_after_order

    #при создании нового заказа счётчик Выполнено за сегодня увеличивается,
    @allure.title('Проверка что при создании наказа счетчик "Выполнено за сегодня" увеличивается')
    def test_order_todays_counters_update(self, login_page, constructor_page, orders_feed_page):
        orders_feed_page.open_url("feed")
        todays_count_before_order = orders_feed_page.get_todays_count()
        login_page.open_url("login")
        login_page.login("denis_pcheliakov_8123@yandex.ru", "8123456")
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()
        constructor_page.close_ingredient_details()
        orders_feed_page.open_url("feed")
        todays_count_before_after_order = orders_feed_page.get_todays_count()

        assert todays_count_before_order < todays_count_before_after_order

    #после оформления заказа его номер появляется в разделе В работе.
    @allure.title('Проверка того что номер оформленного заказа находится "В работе"')
    def test_order_number_in_work(self, login_page, constructor_page, orders_feed_page):
        login_page.open_url("login")
        login_page.login("denis_pcheliakov_8123@yandex.ru", "8123456")
        constructor_page.add_ingredient_to_order()
        constructor_page.submit_order()
        constructor_page.close_ingredient_details()
        orders_feed_page.open_url("feed")
        order_number = orders_feed_page.get_order_number()
        in_progress = orders_feed_page.get_number_order_in_progress()

        assert order_number in in_progress