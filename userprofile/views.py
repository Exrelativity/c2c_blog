from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
@login_required(login_url="/login")
def index(request, msg=None):
    if request.user.is_authenticated:
        if not request.session.__contains__("usersprofile"):
            return redirect(
                "/profile/create", msg="Please fill in your profile information"
            )
    try:
        userId = request.user.id
        userprofileById = UsersProfile.objects.get(userId=userId)
    except UsersProfile.DoesNotExist:
        return redirect(
             "/profile/create", msg="Please fill in your profile information"
        )
    meta = userprofileById.as_meta()
    return render(
        request,
        "profile/show.html",
        {"msg": msg, "userprofile": userprofileById, "meta": meta},
    )
    
@login_required(login_url="/login")
def create(request, msg=None):
    if UsersProfile.objects.filter(userId=request.user.id).exists():
        return redirect(
            "/profile/" + request.user.id + "/update",
            msg="Please update your profile information",
        )
    userprofileForm = UsersProfileForm()

    if request.method == "POST":
        userprofileForm = UsersProfileForm(request.POST, request.FILES)
        if userprofileForm.is_valid():
            userprofileForm.cleaned_data.all()
            userprofileForm.instance.userId = request.user.id
            userprofileForm.instance.firstName = request.user.firstName
            userprofileForm.instance.lastName = request.user.lastName
            userprofileForm.save()
            msg = "Entries saved sucessfully"
            request.session["usersprofile"] = request.POST
            return redirect("/profile/" + request.user.id)
        else:
            msg = "Error validating the form"
    else:
        msg = "Please fill all necessary feild to make a good entry"
    return render(request, "profile/create.html", {"form": userprofileForm, "msg": msg})


@login_required(login_url="/login")
def show(request, userId, msg=None):
    if request.user.is_authenticated:
        if not request.session.__contains__("usersprofile"):
            return redirect(
                "/profile/create", msg="Please fill in your profile information"
            )
    try:
        userprofileById = UsersProfile.objects.get(userId=userId)
    except UsersProfile.DoesNotExist:
        return redirect(
             "/dashboard", msg="Sorry this profile does not exist"
        )
    meta = userprofileById.as_meta()
    return render(
        request,
        "profile/show.html",
        {"msg": msg, "userprofile": userprofileById, "meta": meta},
    )


@login_required(login_url="/login")
def update(request, userId, msg=None):
    if request.user.is_authenticated:
        if not request.session.__contains__("usersprofile"):
            return redirect(
                "/profile/create", msg="Please fill in your profile information"
            )
    userprofileForm = UsersProfileMutationForm()
    userprofileById = UsersProfile.objects.get(userId=userId)
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
        {"form": userprofileForm, "msg": msg, "userprofileById": userprofileById},
    )


@login_required(login_url="/login")
def delete(request, userId, msg=None):
    userprofileById = UsersProfile.objects.get(userId=userId)
    if request.method == "DELETE" and request.user.id == userprofileById.userId:
        userprofileById.soft_delete()
        msg = "Deteted sucessfully"
        return redirect("/profile/usersprofiles", msg)
    else:
        msg = "Error deleting the entry"
        return redirect(f"/profile/{id}", msg)
