from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request, msg = None):
    category = Category.objects.filter(status=True)
    subCategory = SubCategory.objects.filter(status=True) 
    post = Post.objects.filter(status=True)
    paginator = Paginator(post, 15) # Show 15 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "post/index.html", {"msg":msg,"category": category, "subCategory":subCategory, 'page_obj': page_obj})
    
@login_required(login_url="/login")
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
         msg = "please fill in all infomation"
    return render(request, "post/create.html", {"form":postForm,"msg":msg,"category":category, "subCategory":subCategory})
        
        
def show(request, id, msg = None):
    try:
        postById = Post.objects.get(id=id)
    except Post.DoesNotExist:
        msg = "Sorry Post Dost not exist"
    return render(request, "post/show.html", {"msg":msg,"post":postById})
    
@login_required(login_url="/login")
def update(request, id, msg = None):
    postForm = PostMutationForm(request.POST or None)
    postById = Post.objects.get(id=id)
    category = Category.objects.all()
    subCategory = SubCategory.objects.all()
    if request.method == "PUT":
        if postForm.is_valid:
            if request.user.id == postById.userId:
                postForm.save()
                msg = "Entries updated sucessfully"
            else:
                msg = "Permission Denied"
        else:
            msg = "Error validating the form"
    else:
         msg = "please fill in all infomation"
    return render(request, "post/update.html", {"form":postForm,"msg":msg,"postById":postById,"category":category, "subCategory":subCategory})
        
@login_required(login_url="/login")
def delete(request, id, msg = None):
    postById = Post.objects.get(id=id)
    if request.method == "DELETE":
        if request.user.id == postById.userId:
            postById.delete()
            msg = "Deteted sucessfully"
        else:
            msg = "Permission Denied"
    else:
        msg = "Error deleting the entry"
        return redirect(f"show/{id}", msg)
    return redirect("/post/", msg)
        

def byCategory(request, categoryId, msg = None):
    category = Category.objects.filter(status=True)
    subCategory = SubCategory.objects.filter(status=True) 
    post = Post.objects.filter(categoryId=categoryId)
    paginator = Paginator(post, 15) # Show 15 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "post/list.html", {"msg":msg,"category": category, "subCategory":subCategory, 'page_obj': page_obj})


def bySubCategory(request, categoryId, subCategoryId, msg = None):
    category = Category.objects.filter(status=True)
    subCategory = SubCategory.objects.filter(status=True) 
    post = Post.objects.filter(subCategoryId=subCategoryId)
    paginator = Paginator(post, 15) # Show 15 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "post/list.html", {"msg":msg,"category": category, "subCategory":subCategory, 'page_obj': page_obj})
