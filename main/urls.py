from django.urls import path

from . import views

urlpatterns = [
    path("", views.data_entry_vehiculo_view, name="data_entry_vehiculo"),
]