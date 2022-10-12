from django.urls import path

from auto_show.views import list_auto_shows
from deals.views import start_page

app_name = "deals"

urlpatterns = [
    path('', start_page, name="start_page"),

]