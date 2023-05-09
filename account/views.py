from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from .models import *
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
            return redirect("profile")
        else:
            messages.warning(request, "Invalid Email or Password")
    context = {
        "title" : "Sign In",
    }
    return render(request, "account/login.html", context)

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")

@login_required
def profile(request):
    profile_user = Profile.objects.get(user=request.user)
    context = {
        "profile_user" : profile_user,
    }
    return render(request, "account/profile.html", context)

@login_required
def edit_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
        else:
            messages.warning(request, "Error while updating, try again")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "u_form" : u_form,
        "p_form" : p_form,
    }
    return render(request, "account/editprofile.html", context)