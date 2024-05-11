import allure
import requests
import random
import string
import constants as cnst


class User:

    @allure.step('Генерируем строку, состоящую только из букв нижнего регистра длиной {length}')
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Создаем нового пользователя, возвращаем данные о новом пользователе')
    def create_new_user(self):
        new_user = {}

        email = self.generate_random_string(8) + '@ya.ru'
        password = self.generate_random_string(8)
        name = self.generate_random_string(8)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(cnst.URL_STLBRGRS + cnst.API_USER_REG, data=payload)
        if response.status_code == 200:
            new_user = {
                "email": email,
                "password": password,
                "name": name,
                "response": response
            }
        return new_user

    @allure.step('Удаляем пользователя')
    def delete_user(self, token):
        requests.delete(cnst.URL_STLBRGRS + cnst.API_USER_AUTH, headers={'Authorization': token})
