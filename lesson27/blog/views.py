from django.shortcuts import render
from .models import *


def main_page(request):
    # get array of elemetns all elements
    articles = Article.objects.all()
    # get only one element
    # articles = Article.objects.get(pk=1)
    d = {
        "articles": articles
    }

    return render(request, "blog/main_page.html", context=d)


def detail_page(request, id):
    article = Article.objects.get(pk=id)
    d = {
        "article": article,
    }
    return render(request, "blog/detail_page.html", context=d)


def add_page(request):
    return render(request, "blog/add_page.html")
