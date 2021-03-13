from django.shortcuts import render,HttpResponse

# Create your views here.
def buy_page(request):
    return HttpResponse("it is buy page")
