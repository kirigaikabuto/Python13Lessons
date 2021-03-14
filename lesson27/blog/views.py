from django.shortcuts import render, HttpResponse


def main_page(request):
    return HttpResponse("hello from main page")
