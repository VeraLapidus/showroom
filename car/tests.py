import factory
import pytest
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from car.models import Car
from car.views import CarViewSet


@pytest.fixture
def api_client():
    return APIClient()


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    brand = factory.Faker("word", ext_word_list=["Audi", "Mercedes", "BMW", "VW", "Ford"]),
    model = factory.Faker("word", ext_word_list=["A3", "Q7", "X5", "Polo", "Mustang"]),
    year = factory.Faker("year")
    description = factory.Faker("sentence", nb_words=10)


@pytest.fixture
def cars():
    return CarFactory.create_batch(5)


@pytest.fixture
def car():
    return CarFactory.create_batch(1)


@pytest.mark.django_db
def test_create_car(car):
    assert Car.objects.count() == 1


@pytest.mark.django_db
def test_cars_list(cars, api_client):
    url = reverse("car-list")
    response = api_client.get(url)
    assert Car.objects.count() == 5
    assert response.status_code == 200


@pytest.mark.django_db
def test_car_detail(car, api_client):
    url = reverse('car-detail', kwargs={'pk': car[0].id})
    response = api_client.get(url, pk=car[0].id)
    assert response.status_code == 200


@pytest.mark.django_db
def test_car_view_set(cars):
    factory = APIRequestFactory()
    view = CarViewSet.as_view(actions={'get': 'list'})
    request = factory.get(reverse('car-list'))
    response = view(request)
    assert response.status_code == 200
    assert Car.objects.count() == 5


@pytest.mark.django_db
def test_car_view_set_retrieve(car):
    factory = APIRequestFactory()
    view = CarViewSet.as_view(actions={'get': 'retrieve'})
    request = factory.get(reverse('car-detail', args=(car[0].pk,)))
    response = view(request, pk=car[0].pk)
    assert response.status_code == 200
    assert Car.objects.count() == 1
