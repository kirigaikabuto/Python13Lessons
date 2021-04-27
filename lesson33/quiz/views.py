from django.shortcuts import render, redirect


def create_quiz_page(request, contextValue=None):
    print(contextValue)
    return render(request, "quiz/create_quiz_page.html", context=contextValue)


def create_question_page(request):
    return render(request, "quiz/create_question_page.html", )


def create_quiz_action(request):
    quizName = request.POST["quiz_name"]
    if len(quizName) == 0:
        data = {"error": "Please write quiz name"}
        return create_quiz_page(request=request, contextValue=data)
    return redirect("create_question_page")
