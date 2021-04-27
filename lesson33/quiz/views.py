from django.shortcuts import render, redirect
from .models import Quiz


def create_quiz_page(request, contextValue=None):
    quizes = Quiz.objects.all()
    if contextValue is not None:
        contextValue["quizes"] = quizes
    else:
        contextValue = {"quizes": quizes}
    return render(request, "quiz/create_quiz_page.html", context=contextValue)


def create_question_page(request):
    return render(request, "quiz/create_question_page.html", )


def create_quiz_action(request):
    quizName = request.POST["quiz_name"]
    if len(quizName) == 0:
        data = {"error": "Please write quiz name"}
        return create_quiz_page(request=request, contextValue=data)
    q = Quiz(name=quizName, owner=request.user)
    q.save()
    return redirect("create_question_page")
