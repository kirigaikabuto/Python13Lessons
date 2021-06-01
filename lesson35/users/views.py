from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from kafka import KafkaProducer
import json
import datetime


def profile_page(request):
    d = {
        "user": request.user,
    }
    return render(request, "users/profile_page.html", context=d)


def register_page(request):
    form = RegisterForm()
    d = {
        "form": form,
    }
    return render(request, "users/register_page.html", context=d)


def register_action(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect("login_page")
    else:
        d = {
            "form": form,
            "error": form.errors
        }
        return render(request, "users/register_page.html", context=d)


def login_page(request):
    form = LoginForm()
    d = {
        "form": form
    }
    return render(request, "users/login_page.html", context=d)


def login_action(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(username=cd["username"], password=cd["password"])
        if user is not None:
            data = {
                "username": cd["username"],
                "action": "login",
                "time": str(datetime.datetime.now())
            }
            print(data)
            send_message_to_kf(data, "quiz_app")
            if user.is_active:
                login(request, user)

                return redirect("main_page")
            else:
                return HttpResponse("User is deactivated")
        else:
            return HttpResponse("No user by this username and password")
    else:
        form = LoginForm()
        d = {
            "form": form,
            "error": form.errors,
        }
        return render(request, "users/login_page.html", context=d)


def log_out_action(request):
    logout(request)
    return redirect("main_page")


def send_message_to_kf(data, topicName):
    jsonData = json.dumps(data).encode("ascii")
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    producer.send(topicName, jsonData)
    producer.flush()
