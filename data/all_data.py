class Links:
    BASE_URL = "https://stellarburgers.nomoreparties.site"
    URL = 'https://stellarburgers.nomoreparties.site/'

class User:
    email = "denis_pcheliakov_8123@yandex.ru"
    password = "8123456"

class Assert:
    no_progress_orders = 'Все текущие заказы готовы!'

class Handle:
    login_handle = "login"
    order_list_handle = "feed"

class Asserts:
    expect_constructor_heading = 'Соберите бургер'
    expect_order_page_heading = 'Лента заказов'
    expect_details_cart_heading = "Детали ингредиента"
    expect_cont_of_ingredient = "2"
    expect_submit_window_heading = "Ваш заказ начали готовить"
    recover_password_first_step_button = "Восстановить"
    recover_password_second_step_button = "Сохранить"
    profile_button_text_on_account_page = "Профиль"
    order_status_text_in_history = "Выполнен"
    enter_heading_on_login_page = 'Вход'
    order_details_text = "Cостав"