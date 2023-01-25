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
def create_user_auto_show() -> User:
    return User.objects.create(
        username="Ford AutoShow",
        password="12345",
        usertype="AutoShow",
        email="trainee5@gmail.com")


@pytest.fixture
def create_auto_show(create_user_auto_show) -> AutoShow:
    return AutoShow.objects.create(
        name="Ford Minsk",
        country="DE",
        balance=200.00,
        owner=User.objects.get(username="Ford AutoShow"))


@pytest.mark.django_db
def test_auto_show_create(create_auto_show):
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
    AutoShow.objects.filter(name="Ford Minsk").delete()
    assert AutoShow.objects.count() == 0


@pytest.mark.django_db
def test_auto_show_statistic(create_auto_show, api_client):
    url = reverse('autoshow-stat', kwargs={'pk': create_auto_show.id})
    response = api_client.get(url, pk=create_auto_show.id)
    expected_data = {
        "auto_show": "Ford Minsk",
        "amount_of_bought_cars": 0,
        "consumption, USD": None,
        "bought_cars": []
    }
    assert response.status_code == 200
    assert response.data == expected_data
