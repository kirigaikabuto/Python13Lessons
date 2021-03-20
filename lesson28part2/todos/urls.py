from django.urls import path
from .views import *

urlpatterns = [
    path("", main_page, name="main_page"),
    path("detail/<int:id>/", detail_page, name="detail_page"),
    path("add_todo_action/", add_todo_action, name="add_todo_action")
]
