from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    is_auto_show = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['is_customer', 'is_auto_show', 'is_producer', 'email']

    def __str__(self):
        return self.username
