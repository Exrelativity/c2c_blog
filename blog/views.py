
from django.shortcuts import render
from post.models import *
from post.forms import *

# Create your views here.
def index(request, msg = None):
    category = Category.objects.all()
    subCategory = SubCategory.objects.all() 
    post = Post.objects.all()
    return render(request, "index.html", {"msg":msg,"category": category, "subCategory":subCategory, "post":post})


# Create your views here.
def dashboard(request, msg = None):
    category = Category.objects.all()
    subCategory = SubCategory.objects.all() 
    post = Post.objects.all()
    return render(request, "dashboard.html", {"msg":msg,"category": category, "subCategory":subCategory, "post":post})
    
