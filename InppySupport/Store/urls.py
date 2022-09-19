from django.urls import path
from . import views

urlpatterns = [path("", views.store_details, name="store_details")]
