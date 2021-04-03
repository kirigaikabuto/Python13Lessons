from django.shortcuts import render, HttpResponse


def main_page(request):
    return render(request, "products/main_page.html")


def contact_page(request):
    return render(request, "products/contacts.html")
