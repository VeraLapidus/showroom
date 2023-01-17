import pytest
from django.test import TestCase

from auto_show.models import AutoShow
from user.models import User


@pytest.mark.django_db
@pytest.fixture
def create_user() -> User:
    return User.objects.create(
        username="Ford Minsk",
        password="12345",
        usertype="AutoShow",
        email="vera.lapidus.trainee5@gmail.com")


@pytest.mark.django_db
def test_filter_user(create_user):
    assert User.objects.filter(username="Ford Minsk").exists()






######### TestCase ########
# class TestUser(TestCase):
#     def test_create_user(self):
#         user = User.objects.create(
#             username="Ford Minsk",
#             password="12345",
#             usertype="AutoShow",
#             email="vera.lapidus.trainee5@gmail.com")
#
#         assert user.username == "Ford Minsk"


