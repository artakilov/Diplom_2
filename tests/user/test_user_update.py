import allure
import pytest
import requests
import data_for_tests as dft
import constants as cnst
import helpers as hlprs


class TestUserUpdate:

    # тесты 006-008 - позитивные, проверка изменения данных пользователя с авторизацией
    @allure.title('Проверка ручки изменения данных пользователя ({field}) с авторизацией - позитивная')
    @allure.description('Проверяем, что данные пользователя ({field}) можно изменить с авторизацией, '
                        'возвращаются правивльные код и текст ответа')
    @pytest.mark.parametrize('field', ["email", "name", "password"])
    def test_user_update(self, payload_user, field):
        payload_user[0][field] += 's'
        response = requests.patch(cnst.URL_STLBRGRS + cnst.API_USER_AUTH, data=payload_user[0],
                                  headers={'Authorization': payload_user[3]["accessToken"]})

        assert (dft.answr_patch_update_user_ok_status_code == response.status_code and
                dft.answr_patch_update_user_ok_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тесты 009-011 - негативные, проверка изменения данных пользователя без авторизации
    @allure.title('Проверка ручки изменения данных пользователя ({field}) без авторизации - негативная')
    @allure.description('Проверяем, что нельзя измененить данные пользователя ({field}) без авторизации, и что при '
                        'этом возвращается ошибка, возвращаются правильные код и текст ответа')
    @pytest.mark.parametrize('field', ["email", "name", "password"])
    def test_user_update_without_auth(self, payload_user, field):
        payload_user[0][field] += 's'
        response = requests.patch(cnst.URL_STLBRGRS + cnst.API_USER_AUTH, data=payload_user[0])

        assert (dft.answr_patch_update_user_without_auth_status_code == response.status_code and
                dft.answr_patch_update_user_without_auth_success == response.json()["success"] and
                dft.answr_patch_update_user_without_auth_message == response.json()["message"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тест 012 - негативный, проверка изменения почты пользователя на уже существующую
    @allure.title('Проверка ручки изменения почты пользователя на уже существующую - негативная')
    @allure.description('Проверяем, что нельзя измененить почту пользователя на уже существующую, и что при '
                        'этом возвращается ошибка, возвращаются правильные код и текст ответа')
    def test_user_update_with_same_email(self, payload_user):
        payload_user[0]["name"] += 's'
        payload_user[0]["email"] += 's'
        payload_user[0]["password"] += 's'
        response_user_reg = requests.post(cnst.URL_STLBRGRS + cnst.API_USER_REG, data=payload_user[0])
        payload_user[0]["email"] = payload_user[0]["email"][:-1]
        response = requests.patch(cnst.URL_STLBRGRS + cnst.API_USER_AUTH, data=payload_user[0],
                                  headers={'Authorization': response_user_reg.json()["accessToken"]})
        hlprs.delete_user(response_user_reg.json()["accessToken"])

        assert (dft.answr_patch_update_user_with_same_email_status_code == response.status_code and
                dft.answr_patch_update_user_with_same_email_success == response.json()["success"] and
                dft.answr_patch_update_user_with_same_email_message == response.json()["message"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'
