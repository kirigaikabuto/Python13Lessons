from django.shortcuts import render, redirect
from quiz.models import *
from .models import *


def quiz_show_page(request, id):
    quiz = Quiz.objects.get(pk=id)
    d = {
        "quiz": quiz,
    }
    return render(request, "quiz_submission/quiz_show_page.html", context=d)


def quiz_show_detail_page(request, id):
    quiz = Quiz.objects.get(pk=id)
    questions = Question.objects.filter(quiz=quiz)
    d = {
        "quiz": quiz,
        "questions": questions,
    }
    return render(request, "quiz_submission/quiz_show_detail_page.html", context=d)


def quiz_submission_action(request):
    quizId = int(request.POST["quiz_id"])
    quiz = Quiz.objects.get(pk=quizId)
    questions = Question.objects.filter(quiz=quizId)
    result = {}
    for question in questions:
        answerId = int(request.POST["question" + str(question.pk)])
        answer = QuestionAnswer.objects.get(pk=answerId)
        result[question] = answer
    quizSub = QuizSubmission(quiz=quiz, user=request.user)
    quizSub.save()
    for i in result:
        questionSub = QuestionSubmission(question=i, answer=result[i])
        questionSub.save()
        quizSub.answers.add(questionSub)
    quizSub.save()
    return quiz_show_page(request, quizId)
