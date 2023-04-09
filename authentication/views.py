from django.http import HttpResponseRedirect, JsonResponse 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm, ForgotPasswordForm, UpdatePasswordForm
from .models import Users, PasswordReset, VerifiedEmail
from django.conf import settings
from random import choices
from string import ascii_letters, digits
from datetime import datetime, timedelta
from userprofile.models import UsersProfile
# from django.urls import reverse

# Create your views here.

def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    if kwargs.__contains__('msg'):
        msg = kwargs['msg']
    else:
        msg = None
    form = LoginForm(request.POST or None)
    msg = msg
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if not UsersProfile.objects.get(userId = user.id).exists():
                    return redirect("profile/create", msg="Please fill in your profile information")
                return redirect("/dashboard", kwargs={"msg":"Hi, Welcome"})
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    output = render(request, "auth/login.html", {"form":form, "msg":msg})
    return output

@login_required(login_url="/login")
def logout_view(request, *args, **kwargs):
    if kwargs.__contains__('msg'):
        msg = kwargs['msg']
    else:
        msg = None
    msg = msg
    if request.user.is_authenticated:
        logout(request)    
        msg = "Logged out sucessfully"
    else:
        msg = "Error validating the logut"
    output = redirect("/login", msg)
    return output


def register_user(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    if kwargs.__contains__('msg'):
        msg = kwargs['msg']
    else:
        msg = None
    msg = msg
    success = False
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.cleaned_data
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            mailSubject = f"Welcome to {settings.APP_NAME}"
            mailContent = f"""Hi,\n\n\n Welcome to {settings.BASE_URL}.\n One more process to complete...\n\n 
                {settings.BASE_URL}/confirm/email/{email}\n\nPlease click the link above or copy to your browser to send a request of email confirmation.
                \n\nThanks and Regards"""
            send_mail(mailSubject, mailContent, settings.EMAIL, [email])
            msg = "User created sucessfully, Please check your email for a password reset link, if you can't find it in your inbox, please check the spam or junck email box"
            success = True
            return redirect("/dashboard", msg)
        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()
        
    output = render(request, "auth/register.html", {"form":form, "msg":msg, "success":success})
    return output


def forgot_password(request, *args, **kwargs):
    if kwargs.__contains__('msg'):
        msg = kwargs['msg']
    else:
        msg = None
    msg = msg
    form = ForgotPasswordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("email")
            userByEmail = Users.object.get(email)
            token =''.join(choices(ascii_letters + digits, k=16))
            PasswordReset.object.create(userId = userByEmail.id, token=token)
            if userByEmail.exist():
                mailSubject = f"Forgot password Email from {settings.APP_NAME}"
                mailContent = f"""You recently triggered a Reset/Forgot password, from our website {settings.BASE_URL}.\n To proceed with the process...\n\n 
                {settings.BASE_URL}/password/update/{userByEmail.id}/{token}
                \n\nPlease click the link above or copy to your browser and send a request within 48 hours to reset your password.\n\n
                Do neglect this email if this was a mistake or is not important, otherwise send us a report about the activities going on in your account."""
                send_mail(mailSubject, mailContent, settings.EMAIL, email)
                msg = "Please check your email for a password reset link, if you can't find it in your inbox, please check the spam or junck email box "
    else:
        form = ForgotPasswordForm()
  
    output = render(request, "auth/forgot_password.html", {"form":form, "msg":msg})
    return output   
                
    

def update_password(request, id=None, token=None, *args, **kwargs):
    if kwargs.__contains__('msg'):
        msg = kwargs['msg']
    else:
        msg = None
    try:
        userById = Users.objects.get(id)
    except Users.DoesNotExist:
        return redirect("/notfound")
        
    userTokenColumn = PasswordReset.objects.filter(userId=id,token=token)
    form = UpdatePasswordForm(request.POST or userById)
    if request.method == "POST" and userTokenColumn.exist():
        if form.is_valid() and userTokenColumn.createdAt > (datetime.now() - timedelta(2,0,0)):
            password = form.cleaned_data.get("password1")
            userById.set_password(password)
            userById.save()
            msg = " Password Reset/Update was sucessfull"
      
            output = redirect("/login", msg)
            return output
        else:
            msg = "Token has expired, please try the reset password process again at the login page"    
    
    output = render(request, "auth/update_password.html", {"form":form, "msg":msg})
    return output

def confirm_email(request, email, *args, **kwargs):
    if kwargs.__contains__('msg'):
        msg = kwargs['msg']
    else:
        msg = None
    x = VerifiedEmail(email=email)
    x.save()
    msg = "Thanks for confirming your email"
    if request.user.is_authenticated:
        return redirect("/dashboard", msg)
    else:
        msg = "Thanks for confirming your email, Please login"
        return redirect("/login", msg)