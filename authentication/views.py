from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from .forms import LoginForm, SignUpForm, ForgotPasswordForm, UpdatePasswordForm
from .models import Users, PasswordReset, VerifiedEmail
from django.conf import settings
from random import choices
from string import ascii_letters, digits
from datetime import datetime, timedelta
from userprofile.models import UsersProfile

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")

    msg = request.GET.get('msg', None)
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                try:
                    UsersProfile.objects.get(userId=user.id)
                except UsersProfile.DoesNotExist:
                    return redirect("profile/create", msg="Please fill in your profile information")

                return redirect("/dashboard", msg="Hi, Welcome")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "auth/login.html", {"form": form, "msg": msg})

@login_required(login_url="/login")
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        msg = "Logged out successfully"
    else:
        msg = "Error validating the logout"

    return redirect("/login", msg=msg)

def register_user(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")

    msg = request.GET.get('msg', None)
    success = False
    form = SignUpForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=raw_password)

            # Assuming 'can_publish_article' is the codename of the permission
            publish_permission = Permission.objects.get(codename='can_publish_article')

            # Add the permission to the user's user_permissions
            user.user_permissions.add(publish_permission)

            mail_subject = f"Welcome to {settings.APP_NAME}"
            mail_content = f"""Hi,\n\n\nWelcome to {settings.BASE_URL}.\nOne more process to complete...\n\n
                {settings.BASE_URL}/confirm/email/{email}\n\nPlease click the link above or copy it to your browser to send a request for email confirmation.
                \n\nThanks and Regards"""

            send_mail(mail_subject, mail_content, settings.EMAIL, [email])
            msg = "User created successfully. Please check your email for a password reset link. If you can't find it in your inbox, please check the spam or junk email box."
            success = True

            return redirect("/dashboard", msg=msg)
        else:
            msg = "Form is not valid"

    return render(request, "auth/register.html", {"form": form, "msg": msg, "success": success})

def forgot_password(request):
    msg = request.GET.get('msg', None)
    form = ForgotPasswordForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user_by_email = Users.objects.filter(email=email).first()
            
            if user_by_email:
                token = ''.join(choices(string.ascii_letters + string.digits, k=16))
                PasswordReset.objects.create(userId=user_by_email, token=token)
                
                mail_subject = f"Forgot Password Email from {settings.APP_NAME}"
                reset_link = f"{settings.BASE_URL}/password/update/{user_by_email.id}/{token}"
                mail_content = f"""You recently triggered a password reset for your account on {settings.APP_NAME}.\n
                To proceed with the process, please click the link below or copy it into your browser within the next 48 hours:\n\n
                {reset_link}\n\n
                If you did not request this password reset, please report any suspicious activities in your account.
                """

                send_mail(mail_subject, mail_content, settings.EMAIL, [email])
                msg = "Please check your email for a password reset link. If you can't find it in your inbox, please check the spam or junk email folder."

    return render(request, "auth/forgot_password.html", {"form": form, "msg": msg})

def update_password(request, id, token):
    msg = request.GET.get('msg', None)

    try:
        user_by_id = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return redirect("/notfound")

    user_token_column = PasswordReset.objects.filter(userId=id, token=token)
    form = UpdatePasswordForm(request.POST or None)

    if request.method == "POST" and user_token_column.exists():
        if form.is_valid() and user_token_column[0].createdAt > (datetime.now() - timedelta(days=2)):
            password = form.cleaned_data.get("password1")
            user_by_id.set_password(password)
            user_by_id.save()
            msg = "Password Reset/Update was successful"
            return redirect("/login", msg=msg)
        else:
            msg = "Token has expired. Please try the password reset process again at the login page"

    return render(request, "auth/update_password.html", {"form": form, "msg": msg})

def confirm_email(request, email):
    msg = request.GET.get('msg', None)
    VerifiedEmail.objects.create(email=email)
    msg = "Thanks for confirming your email"

    if request.user.is_authenticated:
        return redirect("/dashboard", msg=msg)
    else:
        msg = "Thanks for confirming your email. Please log in"
        return redirect("/login", msg=msg)
