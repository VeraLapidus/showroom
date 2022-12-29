from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERTYPE = (
        ('AutoShow', 'AutoShow'),
        ('Customer', 'Customer'),
        ('Producer', 'Producer'),
        ('Admin', 'Admin'),
    )
    usertype = models.CharField(max_length=50, choices=USERTYPE)
    email = models.EmailField(max_length=255, unique=True)

    REQUIRED_FIELDS = ['usertype', 'email']

    def __str__(self):
        return self.username
