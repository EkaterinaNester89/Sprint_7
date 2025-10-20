import allure
import requests

from data.courier import CourierUrls
from helpers.common import CommonApiHelper


class CourierAPIHelper(CommonApiHelper):
    @allure.step("Отправка запроса для регистрирования тестового курьера в системе")
    def send_request_create(self, data):
        return requests.post(CourierUrls.COURIER_CREATE, json=data)

    @allure.step("Отправка запроса для входа с данными курьера")
    def send_request_login(self, data):
        return requests.post(CourierUrls.COURIER_LOGIN, json=data)

    @allure.step("Получение данных свежерегистрированного тестового курьера")
    def data_random_new_courier_account(self, keys=None):
        data = self.generate_courier_create_data(keys=keys)
        response = self.send_request_create(data)
        if response.status_code == 201:
            return data

    @allure.step("Создание тестовых данных курьера")
    def generate_courier_create_data(self, keys=None):
        login = self.generate_random_string(23)
        password = self.generate_random_string(23)
        first_name = self.generate_random_string(23)

        full_data = {"login": login, "password": password, "firstName": first_name}

        if keys is None:
            return full_data

        return {k: full_data[k] for k in keys if k in full_data}
