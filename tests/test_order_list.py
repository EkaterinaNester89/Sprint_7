import allure

from data.order import OrderApiMessages


class TestOrderList:
    @allure.title("Проверка в тело ответа возвращается список заказов")
    def test_order_list_body_contains_order_list(self, order_api):
        response = order_api.send_request_get_orders()
        assert OrderApiMessages.ORDERS_LIST in response.json()
