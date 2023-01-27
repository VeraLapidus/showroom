from decimal import Decimal

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from auto_show.models import AutoShow
from car.models import Car, CarInstance
from deals.models import Deal
from producer.models import Producer
from user.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user_producer() -> User:
    return User.objects.create(
        username="Mercedes Producer",
        password="12345",
        usertype="Producer",
        email="trainee7@gmail.com")


@pytest.fixture
def create_user_auto_show() -> User:
    return User.objects.create(
        username="Mercedes AutoShow",
        password="12345",
        usertype="AutoShow",
        email="trainee5@gmail.com")


@pytest.fixture
def create_producer(create_user_producer) -> Producer:
    return Producer.objects.create(
        name="Mercedes Berlin",
        country="DE",
        balance=100.00,
        owner=User.objects.get(username="Mercedes Producer"))


@pytest.fixture
def create_auto_show(create_user_auto_show) -> AutoShow:
    return AutoShow.objects.create(
        name="Mercedes Minsk",
        country="DE",
        balance=200.00,
        owner=User.objects.get(username="Mercedes AutoShow"))


@pytest.fixture
def create_car() -> Car:
    return Car.objects.create(
        brand="Mercedes",
        model="GL",
        year=2022)


@pytest.fixture
def create_car_instance(create_car, create_auto_show) -> CarInstance:
    return CarInstance.objects.create(
        name=Car.objects.get(brand="Mercedes"),
        condition="At AutoShow",
        price=80.00,
        auto_shows=AutoShow.objects.get(name="Mercedes Minsk"))


@pytest.fixture
def create_deal(create_producer, create_auto_show, create_car_instance) -> Deal:
    return Deal.objects.create(
        name='Mercedes GL 2022 from Mercedes Berlin to Mercedes Minsk',
        participants="Producer-AutoShow",
        producers=Producer.objects.get(name="Mercedes Berlin"),
        auto_shows=AutoShow.objects.get(name="Mercedes Minsk"),
        car_instances=CarInstance.objects.get(condition="At AutoShow"),
        price=80.00)


@pytest.mark.django_db
def test_deal_create(create_deal):
    assert Deal.objects.count() == 1


@pytest.mark.statistic
@pytest.mark.django_db
def test_producer_statistic(create_producer, create_deal, create_user_producer, api_client):
    user = User.objects.get(username="Mercedes Producer")
    api_client.force_authenticate(user=user)
    url = reverse('producer-stat', kwargs={'pk': create_producer.id})
    response = api_client.get(url, pk=create_producer.id)
    expected_data = {
        "producer_name": "Mercedes Berlin",
        "amount_of_sold_cars": 1,
        "profit": Decimal('80.00'),
        "unique_clients": {
            "Mercedes Minsk"
        },
        "amount_of_unique_clients": 1
    }
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_authentication_of_endpoints(api_client, create_user_producer):
    user = User.objects.get(username="Mercedes Producer")
    api_client.force_authenticate(user=user)
    url = reverse("producer-list")
    response = api_client.get(url)
    assert response.status_code == 200
