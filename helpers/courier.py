import requests

from data.courier import CourierUrls
from helpers.common import CommonApiHelper


class CourierAPIHelper(CommonApiHelper):
    def send_request_create(self, data):
        return requests.post(CourierUrls.COURIER_CREATE, json=data)

    def send_request_login(self, data):
        return requests.post(CourierUrls.COURIER_LOGIN, json=data)

    def data_random_new_courier_account(self, keys=None):
        data = self.generate_courier_create_data(keys=keys)
        response = self.send_request_create(data)
        if response.status_code == 201:
            return data

    def generate_courier_create_data(self, keys=None):
        login = self.generate_random_string(23)
        password = self.generate_random_string(23)
        first_name = self.generate_random_string(23)

        full_data = {"login": login, "password": password, "firstName": first_name}

        if keys is None:
            return full_data

        return {k: full_data[k] for k in keys if k in full_data}
