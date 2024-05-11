import allure
import pytest
import requests
import data_for_tests as dft
import constants as cnst
from helpers import User


class TestUserUpdate:

    # тесты 006-008 - позитивные, проверка изменения данных пользователя с авторизацией
    @allure.title('Проверка ручки изменения данных пользователя ({field}) с авторизацией - позитивная')
    @allure.description('Проверяем, что данные пользователя ({field}) можно изменить с авторизацией, '
                        'возвращаются правивльные код и текст ответа')
    @pytest.mark.parametrize('field', ["email", "name", "password"])
    def test_user_update(self, payload_user, field):
        data = {
            "email": payload_user["email"],
            "password": payload_user["password"],
            "name": payload_user["name"]
        }
        data[field] += 's'
        response = requests.patch(cnst.URL_STLBRGRS + cnst.API_USER_AUTH, data=data,
                                  headers={'Authorization': payload_user["response"].json()["accessToken"]})

        assert (dft.answr_patch_update_user_ok_status_code == response.status_code and
                dft.answr_patch_update_user_ok_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тесты 009-011 - негативные, проверка изменения данных пользователя без авторизации
    @allure.title('Проверка ручки изменения данных пользователя ({field}) без авторизации - негативная')
    @allure.description('Проверяем, что нельзя измененить данные пользователя ({field}) без авторизации, и что при '
                        'этом возвращается ошибка, возвращаются правильные код и текст ответа')
    @pytest.mark.parametrize('field', ["email", "name", "password"])
    def test_user_update_without_auth(self, payload_user, field):
        data = {
            "email": payload_user["email"],
            "password": payload_user["password"],
            "name": payload_user["name"]
        }
        data[field] += 's'
        response = requests.patch(cnst.URL_STLBRGRS + cnst.API_USER_AUTH, data=data)

        assert (dft.answr_patch_update_user_without_auth_status_code == response.status_code and
                dft.answr_patch_update_user_without_auth_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тест 012 - негативный, проверка изменения почты пользователя на уже существующую
    @allure.title('Проверка ручки изменения почты пользователя на уже существующую - негативная')
    @allure.description('Проверяем, что нельзя измененить почту пользователя на уже существующую, и что при '
                        'этом возвращается ошибка, возвращаются правильные код и текст ответа')
    def test_user_update_with_same_email(self, payload_user):
        user = User()
        data = user.create_new_user()
        data["email"] = payload_user["email"]
        response = requests.patch(cnst.URL_STLBRGRS + cnst.API_USER_AUTH, data=data,
                                  headers={'Authorization': data["response"].json()["accessToken"]})
        user.delete_user(data["response"].json()["accessToken"])

        assert (dft.answr_patch_update_user_with_same_email_status_code == response.status_code and
                dft.answr_patch_update_user_with_same_email_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'
