from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
@login_required(login_url="/login")
def index(request, msg=None):
    try:
        userprofileById = UsersProfile.objects.get(userId=request.user.id)
    except UsersProfile.DoesNotExist:
        return redirect(
             "/profile/create", msg="Please fill in your profile information"
        )
    meta = userprofileById.as_meta()
    return render(
        request,
        "profile/show.html",
        {"msg": msg, "profile": userprofileById, "meta": meta},
    )
    
@login_required(login_url="/login")
def create(request, msg=None):
    try:
        UsersProfile.objects.get(userId=request.user.id)
        return redirect(
            "/profile/" + str(request.user.id) + "/update",
            msg="Please update your profile information",
        )
    except UsersProfile.DoesNotExist:
        pass
    userprofileForm = UsersProfileForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if userprofileForm.is_valid():
            userprofileForm.cleaned_data.all()
            userprofileForm.instance.userId = request.user.id
            userprofileForm.instance.firstName = request.user.firstName
            userprofileForm.instance.lastName = request.user.lastName
            userprofileForm.save()
            msg = "Entries saved sucessfully"
            return redirect("/profile/" + request.user.id)
        else:
            msg = "Error validating the form"
    else:
        msg = "Please fill all necessary feild to make a good entry"
    return render(request, "profile/create.html", {"form": userprofileForm, "msg": msg})
    

@login_required(login_url="/login")
def show(request, userId, msg=None):
    try:
        userprofileById = UsersProfile.objects.get(userId=request.user.id)
    except UsersProfile.DoesNotExist:
        return redirect(
                "/profile/create", msg="Please fill in your profile information"
            )
    meta = userprofileById.as_meta()
    return render(
        request,
        "profile/show.html",
        {"msg": msg, "profile": userprofileById, "meta": meta},
    )


@login_required(login_url="/login")
def update(request, userId, msg=None):
    try:
        userprofileById = UsersProfile.objects.get(userId=userId)
    except UsersProfile.DoesNotExist:
        return redirect(
                "/profile/create", msg="Please fill in your profile information"
            )
    userprofileForm = UsersProfileMutationForm(userprofileById or None)
    if request.method == "PUT":
        userprofileForm = UsersProfileMutationForm(request.POST, request.FILES)
        if userprofileForm.is_valid():
            userprofileById.firstName = UsersProfileForm.cleaned_data.get("firstName")
            userprofileById.lastName = UsersProfileForm.cleaned_data.get("lastName")
            userprofileById.image = UsersProfileForm.cleaned_data.get("image")
            userprofileById.dateOfBirth = UsersProfileForm.cleaned_data.get(
                "dateOfBirth"
            )
            userprofileById.gender = UsersProfileForm.cleaned_data.get("gender")
            userprofileById.userId = UsersProfileForm.cleaned_data.get("userId")
            userprofileById.details = UsersProfileForm.cleaned_data.get("details")
            userprofileById.zipcode = UsersProfileForm.cleaned_data.get("zipcode")
            userprofileById.address = UsersProfileForm.cleaned_data.get("address")
            userprofileById.city = UsersProfileForm.cleaned_data.get("city")
            userprofileById.region = UsersProfileForm.cleaned_data.get("region")
            userprofileById.country = UsersProfileForm.cleaned_data.get("country")
            userprofileById.longitude = UsersProfileForm.cleaned_data.get("longitude")
            userprofileById.latitude = UsersProfileForm.cleaned_data.get("latitude")
            userprofileById.popularity = UsersProfileForm.cleaned_data.get("popularity")
            userprofileById.save()
            msg = "Entries updated sucessfully"
        else:
            msg = "Error validating the form"

    else:
        msg = "Please fill all necessary feild to make a good entry"
    return render(
        request,
        "profile/update.html",
        {"form": userprofileForm, "msg": msg, "profile": userprofileById},
    )


@login_required(login_url="/login")
def delete(request, userId, msg=None):
    try:
        userprofileById = UsersProfile.objects.get(userId=userId)
    except UsersProfile.DoesNotExist:
        return redirect(
                "/Dashboard", msg="the requested profile does not exit"
            )
    if request.method == "DELETE" and request.user.id == userprofileById.userId:
        userprofileById.delete()
        msg = "Deteted sucessfully"
        return redirect("/profile/usersprofiles", msg)
    else:
        msg = "Error deleting the entry"
        return redirect(f"/profile/{id}", msg)
