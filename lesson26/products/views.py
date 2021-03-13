from django.shortcuts import render, HttpResponse


def list_page(request):
    firstName = "yerassyl"
    lastName = "tleugazy"
    d = {
        "first_name_html": firstName,
        "last_name_html": lastName,
    }
    return render(request, "products/list.html", context=d)


def detail_page(request):
    return render(request, "products/detail.html")
