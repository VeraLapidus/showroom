import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from auto_show.models import AutoShow
from auto_show.serializers import AutoShowSerializer
from user.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user() -> User:
    return User.objects.create(
        username="Ford Minsk",
        password="12345",
        usertype="AutoShow",
        email="trainee5@gmail.com")


@pytest.fixture
def create_auto_show(create_user) -> AutoShow:
    return AutoShow.objects.create(
        name="Ford",
        country="DE",
        balance=200.00,
        owner=User.objects.get(username="Ford Minsk"))


@pytest.mark.django_db
def test_user_create(create_user):
    assert User.objects.filter(username="Ford Minsk").exists()


@pytest.mark.django_db
def test_auto_show_create(create_auto_show):
    assert AutoShow.objects.filter(name="Ford").exists()
    assert AutoShow.objects.count() == 1


@pytest.mark.django_db
def test_auto_show_api(api_client):
    url = reverse("autoshow-list")
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_auto_show_response_data(create_auto_show, api_client):
    url = reverse('autoshow-list')
    response = api_client.get(url)
    serializer_data = AutoShowSerializer([create_auto_show], many=True).data
    assert response.status_code == 200
    assert response.data == serializer_data


@pytest.mark.django_db
def test_auto_show_delete(create_auto_show):
    AutoShow.objects.filter(name="Ford").delete()
    assert AutoShow.objects.count() == 0
