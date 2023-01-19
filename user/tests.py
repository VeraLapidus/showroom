import pytest
from user.models import User


@pytest.fixture
def create_user() -> User:
    return User.objects.create(
        username="Ford Minsk",
        password="12345",
        usertype="AutoShow",
        email="trainee5@gmail.com")


@pytest.mark.django_db
def test_user_filter(create_user):
    assert User.objects.filter(username="Ford Minsk").exists()
