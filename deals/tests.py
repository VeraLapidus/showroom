import factory
import pytest
import factory.fuzzy

from auto_show.models import AutoShow
from car.models import CarInstance
from car.tests import CarFactory
from producer.models import Producer
from user.models import User
from deals.tasks import add, sale_car_from_producer


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = factory.Faker("password", length=40, special_chars=False, upper_case=False)
    usertype = factory.Faker("word", ext_word_list=["AutoShow", "Customer", "Producer"]),
    # usertype = factory.fuzzy.FuzzyChoice (choices = ["AutoShow", "Customer", "Producer"]),
    email = factory.Faker("email")


class AutoShowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AutoShow

    name = factory.Faker("name")
    country = factory.Faker("word", ext_word_list=["NZ", "CA", "FR", "DE", "US"])
    balance = factory.fuzzy.FuzzyDecimal(low=0, high=10000, precision=2)
    owner = factory.SubFactory(UserFactory)
    wish_car = '{"brand": "Audi", "model": "A3", "year": "None", "color": "None", "price": "120"}   ' \
               '{"brand": "Audi", "model": "A5", "year": "None", "color": "None", "price": "130"}   ' \
               '{"brand": "Audi", "model": "Q7", "year": "None", "color": "None", "price": "25"}'


class ProducerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Producer

    name = factory.Faker("name")
    country = factory.Faker("word", ext_word_list=["NZ", "CA", "FR", "DE", "US"])
    balance = 240
    # balance = factory.fuzzy.FuzzyDecimal(low=0, high=10000, precision=2)
    owner = factory.SubFactory(UserFactory)


class CarInstanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarInstance

    name = factory.SubFactory(CarFactory)
    condition = "At Producer"
    # condition = factory.fuzzy.FuzzyChoice(choices=["At Producer", "Wish for AutoShow", "At Producer", "At AutoShow", "At Producer", "At Producer"])
    price = factory.fuzzy.FuzzyDecimal(low=25, high=110, precision=2)
    producers = factory.SubFactory(ProducerFactory)


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
def users():
    return UserFactory.create_batch(3)


@pytest.fixture
def auto_shows():
    return AutoShowFactory.create_batch(5)


@pytest.fixture
def producers():
    return ProducerFactory.create_batch(3)


@pytest.fixture
def car_instances():
    return CarInstanceFactory.create_batch(10)


@pytest.fixture
def create_producer(create_user) -> Producer:
    return Producer.objects.create(
        name="Ford",
        country="DE",
        balance=200.00,
        owner=User.objects.get(username="Ford Minsk"),
        wish_car='{"brand": "Audi", "model": "A3", "year": "None", "color": "None", "price": "120"}   ' \
                 '{"brand": "Audi", "model": "A5", "year": "None", "color": "None", "price": "130"}   ' \
                 '{"brand": "Audi", "model": "Q7", "year": "None", "color": "None", "price": "25"}')


@pytest.mark.django_db
def test_create_users(users):
    assert User.objects.count() == 3


@pytest.mark.django_db
def test_create_auto_shows(auto_shows):
    assert AutoShow.objects.count() == 5


@pytest.mark.django_db
def test_create_producers(producers):
    assert Producer.objects.count() == 3


@pytest.mark.django_db
def test_create_car_instances(car_instances):
    assert CarInstance.objects.count() == 10


def test_celery_worker_initializes(celery_app, celery_worker):
    assert True


def test_celery_tasks(celery_app, celery_worker):
    assert add.delay(8, 4).get(timeout=5) == 12
