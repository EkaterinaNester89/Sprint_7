from data.common import Urls


class CourierUrls:
    COURIER_CREATE = f"{Urls.MAIN_URL}/api/v1/courier"
    COURIER_LOGIN = f"{Urls.MAIN_URL}/api/v1/courier/login"


class CourierApiMessages:
    COURIER_CREATE = {"ok": True}
    COURIER_CREATE_MISSING_DATA = "Недостаточно данных для создания учетной записи"
    COURIER_CREATE_ACCOUNT_EXISTS = "Этот логин уже используется. Попробуйте другой."
    COURIER_LOGIN_MISSING_DATA = "Недостаточно данных для входа"
    COURIER_LOGIN_ACCOUNT_NOT_EXISTS = "Учетная запись не найдена"
