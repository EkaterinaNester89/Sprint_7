import datetime
import random

import allure
import requests

from data.order import OrderUrls
from helpers.common import CommonApiHelper


class OrderAPIHelper(CommonApiHelper):
    @allure.step("Создание тестовых данных заказа")
    def generate_order_create_data(self, keys=None):
        future_date = datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 7))
        delivery_date = future_date.strftime("%Y-%m-%d")

        phone = "+7" + "".join([str(random.randint(0, 9)) for _ in range(10)])

        full_data = {
            "firstName": self.generate_random_string(10),
            "lastName": self.generate_random_string(10),
            "address": self.generate_random_string(20),
            "metroStation": random.choice([4, 26, 215]),
            "phone": phone,
            "rentTime": random.randint(1, 7),
            "deliveryDate": delivery_date,
            "comment": self.generate_random_string(15),
            "color": random.choice([["BLACK"], ["GREY"], ["BLACK", "GREY"], []]),
        }

        if keys is None:
            return full_data

        return {k: full_data[k] for k in keys if k in full_data}

    @allure.step("Отправка запроса для создания тестового заказа в системе")
    def send_request_create(self, data):
        return requests.post(OrderUrls.ORDER_CREATE, json=data)

    @allure.step("Отправка запроса для получения всех заказов из системы")
    def send_request_get_orders(self, data=None):
        return requests.get(OrderUrls.ORDER_LIST, json=data)
