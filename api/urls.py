from django.urls import path
from .views import Testapi

urlpatterns = [
    path("test/", Testapi.as_view())
]
