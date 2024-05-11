import allure
import requests
import data_for_tests as dft
import constants as cnst
from helpers import User


class TestUserRegister:

    # тест 001 - позитивный, проверка создания пользователя
    @allure.title('Проверка ручки создания пользователя - позитивная')
    @allure.description('Проверяем, что пользователя можно создать, когда передаются все обязательные поля, '
                        'возвращаются правивльные код и текст ответа')
    def test_user_register(self):
        user = User()
        data = user.create_new_user()
        user.delete_user(data["response"].json()["accessToken"])

        assert (dft.answr_post_register_user_ok_status_code == data["response"].status_code and
                dft.answr_post_register_user_ok_success == data["response"].json()["success"]), \
            f'Код ответа - {data["response"].status_code}, текст ответа - "{data["response"].text}"'

    # тест 002 - негативный, проверка создания пользователя, который уже зарегитрирован
    @allure.title('Проверка ручки создания пользователя - негативная. Создание пользователя, который уже '
                  'зарегистрирован')
    @allure.description('Проверяем, что нельзя создать одинаковых пользователей, и что при этом возвращается ошибка, '
                        'возвращаются правильные код и текст ответа')
    def test_user_register_same_data(self, payload_user):
        data = {
            "email": payload_user["email"],
            "password": payload_user["password"],
            "name": payload_user["name"]
        }
        response = requests.post(cnst.URL_STLBRGRS + cnst.API_USER_REG, data=data)

        assert (dft.answr_post_register_user_same_data_status_code == response.status_code and
                dft.answr_post_register_user_same_data_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тест 003 - негативный, проверка создания пользователя без заполнения обязательного поля
    @allure.title('Проверка ручки создания пользователя - негативная. Создание пользователя без заполнения '
                  'обязательного поля')
    @allure.description('Проверяем, что нельзя создать пользователя без заполнения обязательного поля, и что при этом '
                        'возвращается ошибка, возвращаются правильные код и текст ответа')
    def test_user_register_without_data(self, payload_user):
        data = {
            "email": payload_user["email"],
            "password": payload_user["password"],
            "name": ""
        }
        response = requests.post(cnst.URL_STLBRGRS + cnst.API_USER_REG, data=data)

        assert (dft.answr_post_register_user_without_data_status_code == response.status_code and
                dft.answr_post_register_user_without_data_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'
