from enum import Enum


class CarStatus(Enum):
    WISH_AUTO_SHOW = "Wish for AutoShow"
    WISH_CUSTOMER = "Wish for Customer"
    AT_AUTO_SHOW = "At AutoShow"
    AT_PRODUCER = "At Producer"
    AT_CUSTOMER = "At Customer"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
