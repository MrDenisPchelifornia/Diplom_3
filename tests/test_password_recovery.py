import pytest
import allure
from pages import base_page

@pytest.mark.usefixtures("setup")
class TestPasswordRecovery:

    # переход на страницу восстановления пароля по кнопке «Восстановить пароль»,
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transfer_to_recovery_password_page(self, login_page, password_recovery_page):
        login_page.open_url("login")
        password_recovery_page.transfer_recovery_password_page()

        assert "Восстановление пароля" == password_recovery_page.get_text_head_recovery_password_first_screen()

    # ввод почты и клик по кнопке «Восстановить»,
    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    def test_enter_email_and_click_on_recovery_button(self, login_page, password_recovery_page):
        login_page.open_url("login")
        password_recovery_page.transfer_recovery_password_page()
        password_recovery_page.recover_password("denis_pcheliakov_8123@yandex.ru")

        assert "Введите код из письма" == password_recovery_page.get_text_second_screen_placeholder()

    # клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.
    @allure.title('Проверка того что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_test_visiable_and_areas_activity(self, login_page, password_recovery_page):
        login_page.open_url("login")
        password_recovery_page.transfer_recovery_password_page()
        password_recovery_page.recover_password("denis_pcheliakov_8123@yandex.ru")
        password_recovery_page.toggle_show_password()

        assert password_recovery_page.get_eye_button() == password_recovery_page.assign_parent_class()

