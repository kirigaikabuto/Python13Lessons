from django.urls import path
from .views import *

urlpatterns = [
    path("create_quiz_page/", create_quiz_page, name="create_quiz_page"),
    path("create_question_page/", create_question_page, name="create_question_page"),
    path("create_quiz_action/", create_quiz_action, name="create_quiz_action"),
    path("quiz_detail_page/<int:id>/", quiz_detail_page, name="quiz_detail_page"),
]
