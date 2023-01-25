import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from producer.models import Producer
from user.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user() -> User:
    return User.objects.create(
        username="Mercedes Minsk",
        password="12345",
        usertype="Producer",
        email="trainee7@gmail.com")


@pytest.fixture
def create_producer(create_user) -> Producer:
    return Producer.objects.create(
        name="Mercedes",
        country="DE",
        balance=100.00,
        owner=User.objects.get(username="Mercedes Minsk"))


@pytest.mark.statistic
@pytest.mark.django_db
def test_producer(create_producer):
    assert Producer.objects.count() == 1


@pytest.mark.statistic
@pytest.mark.django_db
def test_producer_api(api_client):
    url = reverse("producer-list")
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.statistic
@pytest.mark.django_db
def test_producer_statistic(create_producer, api_client):
    url = reverse('producer-stat', kwargs={'pk': create_producer.id})
    response = api_client.get(url, pk=create_producer.id)
    assert response.status_code == 200
