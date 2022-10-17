from django.urls import path

from .views import list_producers, ProducerList, ProducerView

app_name = "producer"

urlpatterns = [
    path('api/producers_list/', ProducerList.as_view()),
    path('api/producer/<int:pk>', ProducerView.as_view()),




    path('list_producers/', list_producers, name="list_producers"),
]