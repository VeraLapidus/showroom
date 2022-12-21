from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_auto_show = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=False)

    def __str__(self):
        return self.username
