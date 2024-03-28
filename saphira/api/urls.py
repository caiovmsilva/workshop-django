from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_datetime, name="get_datetime"),
    path("texto/<texto>", views.get_texto, name="get_texto")
]
