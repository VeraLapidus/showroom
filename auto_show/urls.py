from django.urls import path

from auto_show.views import list_auto_shows, auto_show_detail

app_name = "auto_show"

urlpatterns = [
    path('list_auto_shows/', list_auto_shows, name="list_auto_shows"),
    path('auto_show_detail/<int:id>/', auto_show_detail, name="auto_show_detail"),
]