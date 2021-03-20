from django.shortcuts import render, redirect
from .models import *


def main_page(request):
    todos = Todo.objects.all()
    d = {
        "todos": todos,
    }
    return render(request, "todos/main_page.html", context=d)


def detail_page(request, id):
    todo = Todo.objects.get(pk=id)
    count_of_days = (todo.deadline - todo.created_date).days
    d = {
        "todo": todo,
        "days": count_of_days,
    }
    return render(request, "todos/detail_page.html", context=d)


def add_todo_action(request):
    title = request.POST["title"]
    deadline = request.POST["deadline"]
    todo = Todo(title=title, deadline=deadline)
    todo.save()
    return redirect("main_page")
