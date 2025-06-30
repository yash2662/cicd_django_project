# # from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render

# def home(request):
#     return render(request, "home.html", {"message": "Welcome to your Django App!"})

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, folks! Welcome to your web app.")