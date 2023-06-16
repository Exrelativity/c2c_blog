from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from file.forms import FileForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@login_required(login_url="/login")
def index(request, msg=None):
    try:
        userprofileById = UsersProfile.objects.get(userId=request.user.id)
    except UsersProfile.DoesNotExist:
        return redirect(
             "/profile/create", msg="Please fill in your profile information"
        )

    return render(
        request,
        "profile/show.html",
        {"msg": msg, "profile": userprofileById},
    )

@csrf_protect
@login_required(login_url="/login")
def create(request, msg=None):
    if UsersProfile.objects.filter(userId=request.user.id).exists():
        return redirect(
            "/profile/" + str(request.user.id) + "/update",
            msg="Please update your profile information",
        )

    fileForm = FileForm(request.POST or None, request.FILES or None)
    userprofileForm = UsersProfileForm(request.POST or None)

    if request.method == "POST":
        if userprofileForm.is_valid():
            obj = userprofileForm.save(commit=False)
            obj.firstName = userprofileForm.cleaned_data.get("firstName")
            obj.lastName = userprofileForm.cleaned_data.get("lastName")
            obj.image = userprofileForm.cleaned_data.get("image")
            obj.dateOfBirth = userprofileForm.cleaned_data.get(
                "dateOfBirth"
            )
            obj.gender = userprofileForm.cleaned_data.get("gender")
            obj.userId = userprofileForm.cleaned_data.get("userId")
            obj.details = userprofileForm.cleaned_data.get("details")
            obj.zipcode = userprofileForm.cleaned_data.get("zipcode")
            obj.address = userprofileForm.cleaned_data.get("address")
            obj.city = userprofileForm.cleaned_data.get("city")
            obj.region = userprofileForm.cleaned_data.get("region")
            obj.country = userprofileForm.cleaned_data.get("country")
            obj.longitude = userprofileForm.cleaned_data.get("longitude")
            obj.latitude = userprofileForm.cleaned_data.get("latitude")
            obj.popularity = userprofileForm.cleaned_data.get("popularity")
            obj.userId = request.user 
            obj.save(force_create=True)
            msg = "Entries saved sucessfully"
            return redirect("/profile/" + request.user.id)
        else:
            msg = "Error validating the form"
    else:
        msg = "Please fill all necessary feild to make a good entry"
    return render(request, "profile/create.html", {"form": userprofileForm,"fileForm":fileForm, "msg": msg})
    

@login_required(login_url="/login")
def show(request, userId, msg=None):
    if not UsersProfile.objects.filter(userId=request.user.id).exists():
        return redirect(
                "/profile/create", msg="Please fill in your profile information"
            )
    userprofileById = UsersProfile.objects.get(userId=request.user.id)
    return render(
        request,
        "profile/show.html",
        {"msg": msg, "profile": userprofileById},
    )


@csrf_protect
@login_required(login_url="/login")
def update(request, userId, msg=None):
    if not UsersProfile.objects.filter(userId=request.user.id).exists():
        return redirect(
                "/profile/create", msg="Please fill in your profile information"
            )
    userprofileById = UsersProfile.objects.get(userId=request.user.id)
    fileForm = FileForm(request.POST or None, request.FILES or None)
    userprofileForm = UsersProfileMutationForm(userprofileById.__dict__ or None)
  
    if request.method == "POST":
        userprofileForm = UsersProfileMutationForm(request.POST, request.FILES)
        if userprofileForm.is_valid():
            userprofileById.firstName = userprofileForm.cleaned_data.get("firstName")
            userprofileById.lastName = userprofileForm.cleaned_data.get("lastName")
            userprofileById.image = userprofileForm.cleaned_data.get("image")
            userprofileById.dateOfBirth = userprofileForm.cleaned_data.get(
                "dateOfBirth"
            )
            userprofileById.gender = userprofileForm.cleaned_data.get("gender")
            userprofileById.userId = userprofileForm.cleaned_data.get("userId")
            userprofileById.details = userprofileForm.cleaned_data.get("details")
            userprofileById.zipcode = userprofileForm.cleaned_data.get("zipcode")
            userprofileById.address = userprofileForm.cleaned_data.get("address")
            userprofileById.city = userprofileForm.cleaned_data.get("city")
            userprofileById.region = userprofileForm.cleaned_data.get("region")
            userprofileById.country = userprofileForm.cleaned_data.get("country")
            userprofileById.longitude = userprofileForm.cleaned_data.get("longitude")
            userprofileById.latitude = userprofileForm.cleaned_data.get("latitude")
            userprofileById.popularity = userprofileForm.cleaned_data.get("popularity")
            userprofileById.save(force_update=True)
            msg = "Entries updated sucessfully"
        else:
            msg = "Error validating the form"

    else:
        msg = "Please fill all necessary feild to make a good entry"
    return render(
        request,
        "profile/update.html",
        {"form": userprofileForm, "fileForm":fileForm, "msg": msg, "profile": userprofileById},
    )


@login_required(login_url="/login")
def delete(request, userId, msg=None):
    if not UsersProfile.objects.filter(userId=request.user.id).exists():
        return redirect(
                "/Dashboard", msg="the requested profile does not exit"
            )
    userprofileById = UsersProfile.objects.get(userId=userId)
    if request.method == "DELETE" and request.user.id == userprofileById.userId:
        userprofileById.delete()
        msg = "Deteted sucessfully"
        return redirect("/profile/usersprofiles", msg)
    else:
        msg = "Error deleting the entry"
        return redirect(f"/profile/{id}", msg)
