import allure
import requests
import data_for_tests as dft
import constants as cnst


class TestUserLogin:

    # тест 004 - позитивный, проверка логина под существующим пользователем
    @allure.title('Проверка ручки логина под существующим пользователем - позитивная')
    @allure.description('Проверяем, что под существующим пользователем можно залогиниться, '
                        'возвращаются правивльные код и текст ответа')
    def test_user_login(self, payload_user):
        response = requests.post(cnst.URL_STLBRGRS + cnst.API_USER_LOG, data=payload_user[0])

        assert (dft.answr_post_login_user_ok_status_code == response.status_code and
                dft.answr_post_login_user_ok_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тест 005 - негативный, проверка логина с неверными логином и паролем пользователя
    @allure.title('Проверка ручки логина под пользователем с неверными логином и паролем пользователя - негативная')
    @allure.description('Проверяем, что нельзя залогиниться пользователем с неверными логином и паролем, и что при '
                        'этом возвращается ошибка, возвращаются правильные код и текст ответа')
    def test_user_login_with_incorrect_data(self, payload_user):
        payload_user[0]["name"] = 'qwqwqw'
        payload_user[0]["password"] = '123456'
        response = requests.post(cnst.URL_STLBRGRS + cnst.API_USER_LOG, data=payload_user[0])

        assert (dft.answr_post_login_user_with_incorrect_data_status_code == response.status_code and
                dft.answr_post_login_user_with_incorrect_data_success == response.json()["success"] and
                dft.answr_post_login_user_with_incorrect_data_message == response.json()["message"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'
