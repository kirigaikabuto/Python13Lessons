from django.shortcuts import render, redirect
from .models import *
from users.views import create_log


def main_page(request):
    user = request.user
    d = {}
    if user.is_authenticated:
        todos_not_completed = Todo.objects.all().filter(isCompleted=False, author=user)
        todos_completed = Todo.objects.all().filter(isCompleted=True, author=user)
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
    user = request.user
    title = request.POST["title"]
    deadline = request.POST["deadline"]
    todo = Todo(title=title, deadline=deadline, author=user)
    todo.save()
    create_log(user, "add_todo")
    return redirect("main_page")


def remove_todo_action(request, id):
    instance = Todo.objects.get(pk=id)
    instance.delete()
    create_log(request.user, "remove_todo")
    return redirect("main_page")


def update_todo_action(request):
    id = int(request.POST["id"])
    isCompleted = bool(request.POST["isCompleted"])
    todo = Todo.objects.get(pk=id)
    todo.isCompleted = isCompleted
    todo.save()
    create_log(request.user, "update_todo")
    return redirect("main_page")
