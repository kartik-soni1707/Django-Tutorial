from django.urls import path
from .views import say_hello

urlpatterns = [
    path("booyah/", say_hello),
]
