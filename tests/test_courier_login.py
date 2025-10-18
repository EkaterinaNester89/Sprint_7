import allure


class TestCourierLogin:
    @allure.title("Проверка курьер может авторизоваться")
    def test_courier_can_login_success_code_200(self, courier_api):
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        response = courier_api.send_request_login(data)
        assert response.status_code == 200

    @allure.title("Проверка для авторизации нужно передать все обязательные поля")
    def test_courier_can_login_with_all_required_fields_success(self, courier_api):
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        response = courier_api.send_request_login(data)
        assert response.status_code == 200

    @allure.title("Проверка система вернёт ошибку, если неправильно указать логин")
    def test_courier_login_incorrect_login_shows_error_404(self, courier_api):
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        data.update(
            {"login": "not_existing_login" + courier_api.generate_random_string()}
        )
        response = courier_api.send_request_login(data)
        assert response.status_code == 404

    @allure.title("Проверка система вернёт ошибку, если неправильно указать пароль")
    def test_courier_login_incorrect_password_shows_error_404(self, courier_api):
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        data.update(
            {"password": "not_existing_password" + courier_api.generate_random_string()}
        )
        response = courier_api.send_request_login(data)
        assert response.status_code == 404

    @allure.title("Проверка если поля логин нет, запрос возвращает ошибку")
    def test_courier_login_without_login_shows_error_400(self, courier_api):
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        data.update({"login": ""})
        response = courier_api.send_request_login(data)
        assert response.status_code == 400

    @allure.title("Проверка если поля пароль нет, запрос возвращает ошибку")
    def test_courier_login_without_password_shows_error_400(self, courier_api):
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        data.update({"password": ""})
        response = courier_api.send_request_login(data)
        assert response.status_code == 400

    @allure.title(
        "Проверка если авторизоваться под несуществующим пользователем, запрос возвращает ошибку"
    )
    def test_courier_login_account_not_exits_shows_error_404(self, courier_api):
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        data.update(
            {
                "login": "not_existing_login" + courier_api.generate_random_string(),
                "password": "not_existing_password"
                + courier_api.generate_random_string(),
            }
        )
        response = courier_api.send_request_login(data)
        assert response.status_code == 404

    @allure.title("Проверка успешный запрос возвращает id")
    def test_courier_login_success_show_id(self, courier_api):
        data = courier_api.data_random_new_courier_account(keys=["login", "password"])
        response = courier_api.send_request_login(data)
        assert "id" in response.json()
