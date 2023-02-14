from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request, msg = None):
    category = Category.objects.all()
    subCategory = SubCategory.objects.all() 
    post = Post.objects.all()
    return render(request, "post/index.html", {"msg":msg,"category": category, "subCategory":subCategory, "post":post})
    

def create(request, msg = None):
    postForm = PostForm(request.POST or None)
    category = Category.objects.all()
    subCategory = SubCategory.objects.all()
    if request.method == "POST":
        if postForm.is_valid:
            postForm.save()
            msg = "Entries saved sucessfully"
        else:
            msg = "Error validating the form"
        
    else:
         msg = "Please fill all necessary feild to make a good entry"
    return render(request, "post/create.html", {"form":postForm,"msg":msg,"category":category, "subCategory":subCategory})
        
        
def show(request, id, msg = None):
    try:
        postById = Post.objects.get(id=id)
    except Post.DoesNotExist:
        msg = "Sorry Post Dost not exist"
    return render(request, "post/show.html", {"msg":msg,"post":postById})
    

def update(request, id, msg = None):
    postForm = PostMutationForm(request.POST or None)
    postById = Post.objects.get(id=id)
    category = Category.objects.all()
    subCategory = SubCategory.objects.all()
    if request.method == "PUT":
        if postForm.is_valid:
            postForm.save()
            msg = "Entries updated sucessfully"
        else:
            msg = "Error validating the form"
        
    else:
         msg = "Please fill all necessary feild to make a good entry"
    return render(request, "post/update.html", {"form":postForm,"msg":msg,"postById":postById,"category":category, "subCategory":subCategory})
        

def delete(request, id, msg = None):
    postById = Post.objects.get(id=id)
    if request.method == "DELETE":
        postById.delete()
        msg = "Deteted sucessfully"
    else:
        msg = "Error deleting the entry"
        return HttpResponseRedirect(f"show/{id}", msg)
    return HttpResponseRedirect("/post/", msg)
        
    