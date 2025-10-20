import allure
import pytest

from data.order import OrderApiMessages
from helpers.order import OrderAPIHelper


class TestOrderCreate:
    @pytest.mark.parametrize(
        "order_color",
        [
            pytest.param(["BLACK"], id="BLACK"),
            pytest.param(["GREY"], id="GREY"),
            pytest.param(["BLACK", "GREY"], id="BLACK, GREY"),
            pytest.param([], id="EMPTY"),
        ],
    )
    @allure.title(
        "Проверка когда создаёшь заказ: цвета {order_color} " "и тело ответа содержит track"
    )
    def test_order_create_with_or_not_color_success_shows_201(self, order_color):
        order_api = OrderAPIHelper()
        data = order_api.generate_order_create_data()
        data.update({"color": order_color})
        response = order_api.send_request_create(data)
        assert response.status_code == 201
        assert OrderApiMessages.ORDER_CREATE in response.json()
