from django.urls import path
from .views import main_page

urlpatterns = [
    path("list/", main_page)
]
