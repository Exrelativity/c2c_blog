from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
# from django.urls import reverse

# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "auth/login.html", {"form":form, "msg":msg})

def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = "User created sucessfully."
            success = True
            return HttpResponseRedirect("/login/")
        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()
    return render(request, "auth/register.html", {"form":form, "msg":msg, "success":success})

def forgot_password(request):
    pass

def update_password(request):
    pass

def confirm_email(request):
    pass