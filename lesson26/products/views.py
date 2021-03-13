from django.shortcuts import render, HttpResponse


def list_page(request):
    return render(request, "products/list.html")


def detail_page(request):
    return render(request, "products/detail.html")
