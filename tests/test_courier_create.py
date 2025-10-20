import allure
import pytest

from data.courier import CourierApiMessages
from helpers.courier import CourierAPIHelper


class TestCourierCreate:

    @allure.title(
        "Проверка курьера можно создать "
        'и успешный запрос возвращает {{"ok":true}} '
        "и запрос возвращает правильный код ответа - 201 "
        "и нужно передать в ручку все обязательные поля (логин - пароль) "
        "и если имени нет - создание происходит"
    )
    def test_courier_create_account_shows_ok_true_201(self):
        courier_api = CourierAPIHelper()
        data = courier_api.generate_courier_create_data(keys=["login", "password"])
        response = courier_api.send_request_create(data)
        assert response.status_code == 201
        assert response.json() == CourierApiMessages.COURIER_CREATE

    @allure.title(
        "Проверка нельзя создать двух одинаковых курьеров "
        "и если создать пользователя с логином, который уже есть, возвращается ошибка"
    )
    def test_courier_create_account_twice_same_shows_error_409(self):
        courier_api = CourierAPIHelper()
        data = courier_api.generate_courier_create_data()
        courier_api.send_request_create(data)
        data.update(
            {
                "password": "password" + courier_api.generate_random_string(23),
                "firstName": "firstName" + courier_api.generate_random_string(23),
            }
        )
        response = courier_api.send_request_create(data)

        assert response.status_code == 409
        assert response.json().get("message") == CourierApiMessages.COURIER_CREATE_ACCOUNT_EXISTS

    @pytest.mark.parametrize(
        "test_case, keys",
        [
            pytest.param(
                "Проверка если логина нет - запрос возвращает ошибку",
                ["firstName", "password"],
                id="without_login",
            ),
            pytest.param(
                "Проверка если пароля нет - запрос возвращает ошибку",
                ["login", "firstName"],
                id="without_password",
            ),
        ],
    )
    @allure.title("{test_case}")
    def test_courier_create_with_missing_fields_shows_error_400(self, test_case, keys):
        courier_api = CourierAPIHelper()

        data = courier_api.generate_courier_create_data(keys=keys)
        response = courier_api.send_request_create(data)

        assert response.status_code == 400
        assert response.json().get("message") == CourierApiMessages.COURIER_CREATE_MISSING_DATA
