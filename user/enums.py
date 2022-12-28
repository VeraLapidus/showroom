from enum import Enum


class Usertype(Enum):
    Is_AutoShow = "Is_AutoShow"
    Is_Customer = "Is_Customer"
    Is_Producer = "Is_Producer"
    Is_Admin = "Is_Admin"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
