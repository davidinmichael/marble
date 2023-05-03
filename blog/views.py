from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        "title" : "Home",
    }
    return render(request, "blog/home.html", context)

def about(request):
    context = {
        "title" : "About",
    }
    return render(request, "blog/about.html", context)

    # https://teams.live.com/meet/9496154298076