from django.urls import path
from .views import *

urlpatterns = [
    path("list/", list_page),
    path("detail/", detail_page)
]
