from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse

def register(request):
    reg_form = UserCreationForm()
    if request.method == "POST":
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get("username")
            # if reg_form.objects.filter(username=username).exists():
            #     messages.warning(request, f"User with {username} already exist")
            #     return redirect("register")
            messages.success(request, f"Account created for {username}")
            return redirect("home")
        
        else:
            messages.warning(request, "Please fill all fields")
            return render(request, "account/register.html", {"reg_form":reg_form,})
    context = {
        "title" : "Sign Up",
        "reg_form" : reg_form,
    }
    return render(request, "account/register.html", context)
