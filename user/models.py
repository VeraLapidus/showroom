from django.contrib.auth.models import AbstractUser
from django.db import models

from user.enums import Usertype


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    usertype = models.CharField(max_length=50, choices=Usertype.choices())

    REQUIRED_FIELDS = ['usertype', 'email']

    def __str__(self):
        return self.username
