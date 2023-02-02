import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from auto_show.models import AutoShow
from car.models import CarInstance, Car
from producer.models import Producer
from user.models import User
from deals.tasks import add, find_best_car_for_sale


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': "redis://redis:6379",
        'result_backend': "redis://redis:6379"
    }


@pytest.fixture
def celery_worker_parameters():
    return {'perform_ping_check': False, }


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user_auto_show() -> User:
    return User.objects.create(
        username="Audi AutoShow",
        password="12345",
        usertype="AutoShow",
        email="trainee5@gmail.com")


@pytest.fixture
def create_user_producer() -> User:
    return User.objects.create(
        username="Audi Producer",
        password="12345",
        usertype="Producer",
        email="trainee6@gmail.com")


@pytest.fixture
def create_auto_show_for_celery(create_user_auto_show) -> AutoShow:
    return AutoShow.objects.create(
        name="Audi Minsk",
        country="DE",
        balance=250.00,
        owner=User.objects.get(username="Audi AutoShow"),
        wish_car='{"brand": "Audi", "model": "A5", "year": "None", "color": "None", "price": "120"}')


@pytest.fixture
def create_producer_for_celery(create_user_producer) -> Producer:
    return Producer.objects.create(
        name="Audi Bayer",
        country="DE",
        balance=20.00,
        owner=User.objects.get(username="Audi Producer"))


@pytest.fixture
def create_car_for_celery() -> Car:
    return Car.objects.create(
        brand="Audi",
        model="A5",
        year=2000)


@pytest.fixture
def create_car_instance_for_celery(create_car_for_celery, create_producer_for_celery) -> CarInstance:
    return CarInstance.objects.create(
        name=Car.objects.get(brand="Audi"),
        condition="At Producer",
        price=80.00,
        producers=Producer.objects.get(name="Audi Bayer"))


@pytest.fixture
def create_car_instance_for_celery2(create_car_for_celery, create_producer_for_celery) -> CarInstance:
    return CarInstance.objects.create(
        name=Car.objects.get(brand="Audi"),
        condition="At Producer",
        price=15.00,
        producers=Producer.objects.get(name="Audi Bayer"))


def test_celery_worker_initializes(celery_app, celery_worker):
    assert True


def test_celery_tasks(celery_app, celery_worker):
    assert add.delay(8, 4).get(timeout=5) == 12


@pytest.mark.celery_app
@pytest.mark.celery_worker
@pytest.mark.django_db
def test_celery_find_best_car_for_sale(create_auto_show_for_celery, create_car_instance_for_celery,
                                       create_car_instance_for_celery2):
    assert AutoShow.objects.count() == 1
    assert CarInstance.objects.count() == 2
    assert AutoShow.objects.filter(balance=250.00).exists()
    assert CarInstance.objects.order_by('price').first().price == 15.00
    assert find_best_car_for_sale.delay().get(timeout=10) == '15.00'


@pytest.mark.django_db
def test_authenticate_but_forbidden_request(api_client, create_user_auto_show):
    user = User.objects.get(username="Audi AutoShow")
    api_client.force_authenticate(user=user)
    url = reverse('deal-list')
    response = api_client.get(url)
    status_code = status.HTTP_403_FORBIDDEN
    assert response.status_code == status_code
