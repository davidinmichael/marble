from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import HttpResponse

def register(request):
    reg_form = UserRegisterForm()
    if request.method == "POST":
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get("username")

            messages.success(request, f"Account created for {username}")
            return redirect("login")
        
        else:
            messages.warning(request, "Please fill all fields")
            return render(request, "account/register.html", {"reg_form":reg_form,})
    context = {
        "title" : "Sign Up",
        "reg_form" : reg_form,
    }
    return render(request, "account/register.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"{username}, Login Successful")
            return redirect("home")
        else:
            messages.warning(request, "Invalid Email or Password")
    context = {
        "title" : "Sign In",
    }
    return render(request, "account/login.html", context)