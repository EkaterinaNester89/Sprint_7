import allure

from data.courier import CourierApiMessages


class TestCourierCreate:
    @allure.title("Проверка курьера можно создать")
    def test_courier_create_account_success(self, courier_api):
        data = courier_api.generate_courier_create_data()
        response = courier_api.send_request_create(data)
        assert 'ok' in response.json()

    @allure.title("Проверка нельзя создать двух одинаковых курьеров")
    def test_courier_create_account_twice_same_shows_error(self, courier_api):
        data = courier_api.generate_courier_create_data()
        courier_api.send_request_create(data)
        response = courier_api.send_request_create(data)
        assert response.status_code == 409

    @allure.title(
        "Проверка чтобы создать курьера, нужно передать в ручку все обязательные поля (логин - пароль)"
    )
    def test_courier_create_account_with_all_required_fields(self, courier_api):
        data = courier_api.generate_courier_create_data(keys=["login", "password"])
        response = courier_api.send_request_create(data)
        assert response.status_code == 201

    @allure.title("Проверка запрос возвращает правильный код ответа - 201")
    def test_courier_create_account_shows_code_201(self, courier_api):
        data = courier_api.generate_courier_create_data()
        response = courier_api.send_request_create(data)
        assert response.status_code == 201

    @allure.title('Проверка успешный запрос возвращает {{"ok":true}}')
    def test_courier_create_account_shows_ok_true(self, courier_api):
        data = courier_api.generate_courier_create_data()
        response = courier_api.send_request_create(data)
        assert response.json() == CourierApiMessages.COURIER_CREATE

    @allure.title("Проверка если логина нет - запрос возвращает ошибку")
    def test_courier_create_account_without_login_field_shows_error_400(
        self, courier_api
    ):
        data = courier_api.generate_courier_create_data(keys=["firstName", "password"])
        response = courier_api.send_request_create(data)
        assert response.status_code == 400

    @allure.title("Проверка если пароля нет - запрос возвращает ошибку")
    def test_courier_create_account_without_password_field_shows_error_400(
        self, courier_api
    ):
        data = courier_api.generate_courier_create_data(keys=["login", "firstName"])
        response = courier_api.send_request_create(data)
        assert response.status_code == 400

    @allure.title("Проверка если имени нет - создание происходит")
    def test_courier_create_account_without_first_name_field_shows_success_201(
        self, courier_api
    ):
        data = courier_api.generate_courier_create_data(keys=["login", "password"])
        response = courier_api.send_request_create(data)
        assert response.status_code == 201

    @allure.title(
        "Проверка если создать пользователя с логином, который уже есть, возвращается ошибка"
    )
    def test_courier_create_account_login_exists_show_error_409(self, courier_api):
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
