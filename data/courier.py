from data.common import Urls


class CourierUrls:
    COURIER_CREATE = f"{Urls.MAIN_URL}/api/v1/courier"
    COURIER_LOGIN = f"{Urls.MAIN_URL}/api/v1/courier/login"


class CourierApiMessages:
    COURIER_CREATE = {"ok": True}
