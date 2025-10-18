import pytest

from helpers.courier import CourierAPIHelper
from helpers.order import OrderAPIHelper


@pytest.fixture()
def courier_api():
    return CourierAPIHelper()


@pytest.fixture()
def order_api():
    return OrderAPIHelper()


@pytest.fixture(
    params=[
        pytest.param(["BLACK"], id="BLACK"),
        pytest.param(["GREY"], id="GREY"),
        pytest.param(["BLACK", "GREY"], id="BLACK, GREY"),
        pytest.param([], id="EMPTY"),
    ]
)
def order_color(request):
    return request.param
