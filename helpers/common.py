import random
import string

import allure


class CommonApiHelper:
    @allure.step("Создание рандомной строки с количеством знаков: {length}")
    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string
