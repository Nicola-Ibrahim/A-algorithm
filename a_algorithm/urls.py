from django.urls import path
from . import views

app_name = "a_algorithm"

urlpatterns = [
    path("", views.index, name='index'),
]
