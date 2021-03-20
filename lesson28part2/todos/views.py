from django.shortcuts import render, redirect
from .models import *


def main_page(request):
    todos_not_completed = Todo.objects.all().filter(isCompleted=False)
    todos_completed = Todo.objects.all().filter(isCompleted=True)
    d = {
        "todos_not_completed": todos_not_completed,
        "todos_completed": todos_completed,
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


def remove_todo_action(request, id):
    instance = Todo.objects.get(pk=id)
    instance.delete()
    return redirect("main_page")


def update_todo_action(request):
    id = int(request.POST["id"])
    isCompleted = bool(request.POST["isCompleted"])
    todo = Todo.objects.get(pk=id)
    todo.isCompleted = isCompleted
    todo.save()
    return redirect("main_page")
