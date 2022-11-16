from enum import Enum


class Participants(Enum):
    PRODUCER_SHOWROOM = "Поставщик-автосалон"
    SHOWROOM_CUSTOMER = "Автосалон-покупатель"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
