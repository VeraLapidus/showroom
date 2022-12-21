from enum import Enum


class Participants(Enum):
    PRODUCER_AUTOSHOW = "Producer-AutoShow"
    AUTOSHOW_CUSTOMER = "AutoShow-Customer"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
