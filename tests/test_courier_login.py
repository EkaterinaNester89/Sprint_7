import allure
import pytest

from data.courier import CourierApiMessages
from helpers.courier import CourierAPIHelper


class TestCourierLogin:
    @allure.title(
        "Проверка курьер может авторизоваться "
        "и для авторизации нужно передать все обязательные поля "
        "и успешный запрос возвращает id"
    )
    def test_courier_can_login_success_code_200(self):
        courier_api = CourierAPIHelper()
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        response = courier_api.send_request_login(data)
        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.parametrize(
        "test_case, keys",
        [
            pytest.param(
                "Проверка система вернёт ошибку, если неправильно указать логин",
                ["login"],
                id="incorrect_login",
            ),
            pytest.param(
                "Проверка система вернёт ошибку, если неправильно указать пароль",
                ["password"],
                id="incorrect_password",
            ),
            pytest.param(
                "Проверка если авторизоваться под несуществующим пользователем, запрос возвращает ошибку",
                ["login", "password"],
                id="incorrect_login_password",
            ),
        ],
    )
    @allure.title("{test_case}")
    def test_courier_login_incorrect_login_shows_error_404(
        self,
        test_case,
        keys,
    ):
        courier_api = CourierAPIHelper()
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        for key in keys:
            data.update({key: f"not_existing_{key}" + courier_api.generate_random_string()})
        response = courier_api.send_request_login(data)
        assert response.status_code == 404
        assert response.json().get("message") == CourierApiMessages.COURIER_LOGIN_ACCOUNT_NOT_EXISTS

    @pytest.mark.parametrize(
        "test_case, key",
        [
            pytest.param(
                "Проверка если поля логин нет, запрос возвращает ошибку",
                "login",
                id="missing_login",
            ),
            pytest.param(
                "Проверка если поля пароль нет, запрос возвращает ошибку",
                "password",
                id="missing_password",
            ),
        ],
    )
    @allure.title("{test_case}")
    def test_courier_login_missing_data_shows_error_400(
        self,
        test_case,
        key,
    ):
        courier_api = CourierAPIHelper()
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        data.update({key: ""})
        response = courier_api.send_request_login(data)
        assert response.status_code == 400
        assert response.json().get("message") == CourierApiMessages.COURIER_LOGIN_MISSING_DATA
