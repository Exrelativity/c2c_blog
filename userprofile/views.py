from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request, msg = None):
    userprofile = Usersprofile.objects.all()
    return render(request, "profile/index.html", {"msg":msg, "userprofile":userprofile})
    

def create(request, msg = None):
    userprofileForm = UsersprofileForm(request.POST or None)
    
    if request.method == "POST":
        if userprofileForm.is_valid:
            userprofileForm.save()
            msg = "Entries saved sucessfully"
        else:
            msg = "Error validating the form"
        
    else:
         msg = "Please fill all necessary feild to make a good entry"
    return render(request, "profile/create.html", {"form":userprofileForm,"msg":msg })
        
        
def show(request, id, msg = None):
    try:
        userprofileById = Usersprofile.objects.get(id=id)
    except Usersprofile.DoesNotExist:
        msg = "Sorry Usersprofile Dost not exist"
    return render(request, "profile/show.html", {"msg":msg,"userprofile":userprofileById})
    

def update(request, id, msg = None):
    userprofileForm = UsersprofileMutationForm(request.POST or None)
    userprofileById = Usersprofile.objects.get(id=id)
    
    if request.method == "PUT":
        if userprofileForm.is_valid:
            UsersprofileForm.save()
            msg = "Entries updated sucessfully"
        else:
            msg = "Error validating the form"
        
    else:
         msg = "Please fill all necessary feild to make a good entry"
    return render(request, "profile/update.html", {"form":userprofileForm,"msg":msg,"userprofileById":userprofileById })
        

def delete(request, id, msg = None):
    userprofileById = Usersprofile.objects.get(id=id)
    if request.method == "DELETE":
        userprofileById.delete()
        msg = "Deteted sucessfully"
        return HttpResponseRedirect("/profile/usersprofiles", msg)
    else:
        msg = "Error deleting the entry"
        return HttpResponseRedirect(f"/profile/{id}", msg)
        
    