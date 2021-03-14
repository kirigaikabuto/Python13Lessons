from django.shortcuts import render, HttpResponse


def main_page(request):
    name = "yerassyl"
    articles = [
        {
            "name": "article1",
            "description": "it is the best article",
        },
        {
            "name": "article2",
            "description": "it is the best article",
        }
    ]
    d = {
        "first_name": name,
        "articles": articles,
    }

    return render(request, "blog/main_page.html", context=d)
