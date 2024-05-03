import allure
import requests
import data_for_tests as dft
import constants as cnst


class TestOrderCreate:

    # тест 013 - позитивный, проверка создания заказа
    @allure.title('Проверка ручки создания заказа - позитивная')
    @allure.description('Проверяем, что можно создать заказ, когда передаются все обязательные поля с авторизацией, '
                        'возвращаются правивльные код и текст ответа')
    def test_order_create(self, payload_user):
        payload_ing = {
            "ingredients": [requests.get(cnst.URL_STLBRGRS + cnst.API_INGREDIENTS).json()["data"][0]["_id"]]
        }
        response = requests.post(cnst.URL_STLBRGRS + cnst.API_ORDER, data=payload_ing,
                                 headers={'Authorization': payload_user[3]["accessToken"]})

        assert (dft.answr_post_create_order_ok_status_code == response.status_code and
                dft.answr_post_register_user_ok_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тест 014 - негативный, проверка создания заказа без ингредиентов
    @allure.title('Проверка ручки создания заказа без ингредиентов - негативная')
    @allure.description('Проверяем, что нельзя создать заказ без ингредиентов с авторизацией, и что при '
                        'этом возвращается ошибка, возвращаются правильные код и текст ответа')
    def test_order_create_without_ingredients(self, payload_user):
        payload_ing = {
            "ingredients": []
        }
        response = requests.post(cnst.URL_STLBRGRS + cnst.API_ORDER, data=payload_ing,
                                 headers={'Authorization': payload_user[3]["accessToken"]})

        assert (dft.answr_post_create_order_without_ingredients_status_code == response.status_code and
                dft.answr_post_create_order_without_ingredients_success == response.json()["success"] and
                dft.answr_post_create_order_without_ingredients_message == response.json()["message"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тест 015 - негативный, проверка создания заказа с неверными хешами ингредиентов
    @allure.title('Проверка ручки создания заказа с неверными хэшами ингредиентов - негативная')
    @allure.description('Проверяем, что нельзя создать заказ с неверными хэшами ингредиентов с авторизацией, и что при '
                        'этом возвращается ошибка, возвращаются правильные код и текст ответа')
    def test_order_create_with_badhash_ingredients(self, payload_user):
        payload_ing = {
            "ingredients": [requests.get(cnst.URL_STLBRGRS + cnst.API_INGREDIENTS).json()["data"][0]["_id"] + 'a']
        }
        response = requests.post(cnst.URL_STLBRGRS + cnst.API_ORDER, data=payload_ing,
                                 headers={'Authorization': payload_user[3]["accessToken"]})

        assert dft.answr_post_create_order_with_badhash_ingredients_status_code == response.status_code, \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тест 016 - негативный, проверка создания заказа без авторизации
    @allure.title('Проверка ручки создания заказа без авторизации - негативная')
    @allure.description('Проверяем, что нельзя создать заказ без авторизации, и что при '
                        'этом возвращается ошибка, возвращаются правильные код и текст ответа')
    def test_order_create_without_auth(self):
        payload_ing = {
            "ingredients": [requests.get(cnst.URL_STLBRGRS + cnst.API_INGREDIENTS).json()["data"][0]["_id"]]
        }
        response = requests.post(cnst.URL_STLBRGRS + cnst.API_ORDER, data=payload_ing)

        assert (dft.answr_post_create_order_without_auth_status_code == response.status_code and
                dft.answr_post_create_order_without_auth_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'
