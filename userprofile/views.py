from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url="/login")
def index(request, msg = None):
    userprofile = UsersProfile.objects.all()
    return render(request, "profile/index.html", {"msg":msg, "userprofile":userprofile})
    
    
@login_required(login_url="/login")
def create(request, msg = None):
    userprofileForm = UsersProfileForm(request.POST or None)
    
    if request.method == "POST":
        if userprofileForm.is_valid:
            userprofileForm.save()
            msg = "Entries saved sucessfully"
            request.session['usersprofile'] = request.POST
        else:
            msg = "Error validating the form"
        
    else:
         msg = "Please fill all necessary feild to make a good entry"
    return render(request, "profile/create.html", {"form":userprofileForm,"msg":msg })
        
        
@login_required(login_url="/login")
def show(request, id, msg = None):
    if request.user.is_authenticated:
            if not request.session.__contains__("usersprofile"):
                 return redirect("/profile/create", alert="Please fill in your profile information")
    userprofileById:object
    try:
        userprofileById = UsersProfile.objects.get(id=id)
    except UsersProfile.DoesNotExist:
        msg = "Sorry UsersProfile Dost not exist"
   
    return render(request, "profile/show.html", {"msg":msg,"userprofile":userprofileById})
    
    
@login_required(login_url="/login")
def update(request, id, msg = None):
    if request.user.is_authenticated:
            if not request.session.__contains__("usersprofile"):
                 return redirect("/profile/create", alert="Please fill in your profile information")
    userprofileForm = UsersProfileMutationForm(request.POST or None)
    userprofileById = UsersProfile.objects.get(id=id)
    
    if request.method == "PUT":
        if userprofileForm.is_valid:
            UsersProfileForm.save()
            msg = "Entries updated sucessfully"
        else:
            msg = "Error validating the form"
        
    else:
         msg = "Please fill all necessary feild to make a good entry"
    return render(request, "profile/update.html", {"form":userprofileForm,"msg":msg,"userprofileById":userprofileById })
        
        
@login_required(login_url="/login")
def delete(request, id, msg = None):
    userprofileById = UsersProfile.objects.get(id=id)
    if request.method == "DELETE":
        userprofileById.delete()
        msg = "Deteted sucessfully"
        return redirect("/profile/usersprofiles", msg)
    else:
        msg = "Error deleting the entry"
        return redirect(f"/profile/{id}", msg)
        
    