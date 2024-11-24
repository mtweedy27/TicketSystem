from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Landing page
def landing(response):
    return render(response, "accounts/landing.html")

# User login forms
def register(request):
    #Form input validity check
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/login")

        else:
            form = UserCreationForm()

    #Define 'form' for html template
    form = UserCreationForm()
    return render(request, "accounts/register.html", {"form":form})

# Login form
def login(request):
    return render(request, 'registration/login.html')
