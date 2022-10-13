from django.urls import path

from .views import list_auto_shows, auto_show_detail, AutoShowList

app_name = "auto_show"

urlpatterns = [

    path('api/auto_shows_list', AutoShowList.as_view()),








    path('list_auto_shows/', list_auto_shows, name="list_auto_shows"),
    path('auto_show_detail/<int:id>/', auto_show_detail, name="auto_show_detail"),
]