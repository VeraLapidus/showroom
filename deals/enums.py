from enum import Enum


class Participants(Enum):
    PRODUCER_SHOWROOM = "Producer-AutoShow"
    SHOWROOM_CUSTOMER = "AutoShow-Customer"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
