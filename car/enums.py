from enum import Enum


class CarStatus(Enum):
    WISH_AUTO_SHOW = "Желаемый для автосалона"
    WISH_CUSTOMER = "Желаемый для покупателя"
    AT_AUTO_SHOW = "В автосалоне"
    AT_PRODUCER = "У поставщика"
    AT_CUSTOMER = "У покупателя"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
