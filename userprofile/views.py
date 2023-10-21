# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UsersProfile
from .forms import UsersProfileForm

@login_required(login_url="/login")
def create(request, msg=None):
    user_profile = UsersProfile.objects.filter(userId=request.user).first()
    
    if user_profile:
        return redirect("update_profile", user_id=user_profile.userId.id, msg="Please update your profile information")

    if request.method == "POST":
        userprofileForm = UsersProfileForm(request.POST, request.FILES)
        if userprofileForm.is_valid():
            userprofile = userprofileForm.save(commit=False)
            userprofile.userId = request.user
            userprofile.save()
            msg = "Entries saved successfully"
            return redirect("show_profile", userId=request.user.id)
        else:
            msg = "Error validating the form"
    else:
        msg = "Please fill all necessary fields to make a good entry"
        userprofileForm = UsersProfileForm()

    return render(request, "profile/create.html", {"form": userprofileForm, "msg": msg})

@login_required(login_url="/login")
def update(request, user_id, msg=None):
    user_profile = UsersProfile.objects.filter(userId=request.user).first()
    
    if not user_profile:
        return redirect("create_profile", msg="Please fill in your profile information")

    if request.method == "POST":
        userprofileForm = UsersProfileForm(request.POST, request.FILES, instance=user_profile)
        if userprofileForm.is_valid():
            userprofileForm.save()
            msg = "Entries updated successfully"
        else:
            msg = "Error validating the form"
    else:
        userprofileForm = UsersProfileForm(instance=user_profile)

    return render(request, "profile/update.html", {"form": userprofileForm, "msg": msg, "profile": user_profile})

# Add named URLs to your urls.py for these views
