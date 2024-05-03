import allure
import requests
import data_for_tests as dft
import constants as cnst


class TestGetOrdersUser:

    # тест 017 - позитивный, получение заказов пользователя
    @allure.title('Проверка ручки получение заказов пользователя - позитивная')
    @allure.description('Проверяем, что можно полученить информацию о заказах пользователя с авторизацией, '
                        'возвращаются правивльные код и текст ответа')
    def test_get_orders_user(self, payload_user):
        payload_ing = {
            "ingredients": [requests.get(cnst.URL_STLBRGRS + cnst.API_INGREDIENTS).json()["data"][0]["_id"]]
        }
        requests.post(cnst.URL_STLBRGRS + cnst.API_ORDER, data=payload_ing,
                      headers={'Authorization': payload_user[3]["accessToken"]})
        response = requests.get(cnst.URL_STLBRGRS + cnst.API_ORDER,
                                headers={'Authorization': payload_user[3]["accessToken"]})

        assert (dft.answr_get_orders_user_status_code == response.status_code and
                dft.answr_get_orders_user_success == response.json()["success"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'

    # тест 018 - негативный, получение заказов пользователя без авторизации
    @allure.title('Проверка ручки получение заказов пользователя - позитивная')
    @allure.description('Проверяем, что нельзя получить информацию о заказах пользователя без авторизации, и что при '
                        'этом возвращается ошибка, возвращаются правильные код и текст ответа')
    def test_get_orders_user_without_auth(self, payload_user):
        payload_ing = {
            "ingredients": [requests.get(cnst.URL_STLBRGRS + cnst.API_INGREDIENTS).json()["data"][0]["_id"]]
        }
        requests.post(cnst.URL_STLBRGRS + cnst.API_ORDER, data=payload_ing,
                      headers={'Authorization': payload_user[3]["accessToken"]})
        response = requests.get(cnst.URL_STLBRGRS + cnst.API_ORDER)

        assert (dft.answr_get_orders_user_without_auth_status_code == response.status_code and
                dft.answr_get_orders_user_without_auth_success == response.json()["success"] and
                dft.answr_get_orders_user_without_auth_message == response.json()["message"]), \
            f'Код ответа - {response.status_code}, текст ответа - "{response.text}"'
