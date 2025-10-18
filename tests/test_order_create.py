import allure

from data.order import OrderApiMessages


class TestOrderCreate:
    @allure.title("Проверка когда создаёшь заказ: цвета {order_color}")
    def test_order_create_with_or_not_color_201(self, order_api, order_color):
        data = order_api.generate_order_create_data()
        data.update({"color": order_color})
        response = order_api.send_request_create(data)
        assert response.status_code == 201

    @allure.title("Проверка когда создаёшь заказ: тело ответа содержит track")
    def test_order_create_body_contain_track(self, order_api):
        data = order_api.generate_order_create_data()
        response = order_api.send_request_create(data)
        assert OrderApiMessages.ORDER_CREATE in response.json()
