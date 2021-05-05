from django.urls import path
from .views import *

urlpatterns = [
    path("quiz_show_page/<int:id>/", quiz_show_page, name="quiz_show_page"),
    path("quiz_show_detail_page/<int:id>/", quiz_show_detail_page, name="quiz_show_detail_page"),
    path("quiz_submission_action/", quiz_submission_action, name="quiz_submission_action"),
]
