from data.common import Urls


class OrderUrls:
    ORDER_CREATE = f"{Urls.MAIN_URL}/api/v1/orders"
    ORDER_LIST = f"{Urls.MAIN_URL}/api/v1/orders"


class OrderApiMessages:
    ORDER_CREATE = "track"
    ORDERS_LIST = "orders"
