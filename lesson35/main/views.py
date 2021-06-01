from django.shortcuts import render
from quiz.models import *


def main_page(request):
    quizs = Quiz.objects.all()
    d = {
        "quizs": quizs,
    }
    return render(request, "main/main_page.html", context=d)
