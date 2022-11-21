from celery import shared_task

from auto_show.models import AutoShow


@shared_task
def add():

    car = AutoShow.objects.all()
    print(car)
