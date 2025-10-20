import allure

from data.order import OrderApiMessages
from helpers.order import OrderAPIHelper


class TestOrderList:
    @allure.title("Проверка в тело ответа возвращается список заказов")
    def test_order_list_body_contains_order_list_shows_200(self):
        order_api = OrderAPIHelper()
        response = order_api.send_request_get_orders()
        assert response.status_code == 200
        assert OrderApiMessages.ORDERS_LIST in response.json()
