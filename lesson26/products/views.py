from django.shortcuts import render, HttpResponse


def list_page(request):
    return HttpResponse("Hello it is django")


def detail_page(request):
    return HttpResponse("Hello it is detail page")
