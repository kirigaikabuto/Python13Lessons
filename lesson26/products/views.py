from django.shortcuts import render, HttpResponse


def main_page(request):
    return HttpResponse("Hello it is django")
