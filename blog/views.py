
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from post.models import *
from post.forms import *

# Create your views here.
def index(request, msg = None):
    category = Category.objects.select_related("subCategory__posts").filter(status=True, front=True)[:7]
    subCategory = category.posts
    post = category.post
    return render(request, "post-front/index.html", {"msg":msg,"category": category, "subCategory":subCategory, "post":post})

def search(request, msg = None):
    form = SearchForm(request.POST or None)
    post = {} 
    if request.method == "POST":
        if form.is_valid():
            search = form.cleaned_data.get("search")
            search_list = search.split(" ")
            for i in search_list:
                post += Post.objects.filter(Q(title__icontains= i) | Q(content__icontains= i))
    paginator = Paginator(post, 15) # Show 15 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "post-front/search.html", {"msg":msg, "form":form, "page_obj":page_obj})
    
# Create your views here.
def dashboard(request, msg = None):
    category = Category.objects.select_related("subCategory__posts").filter(status=True, front=True)[:7]
    subCategory = category.subCategory
    post = category.posts
    return render(request, "dashboard.html", {"msg":msg,"category": category, "subCategory":subCategory, "post":post})
    
def error_404_handler(request, exception):
    return render(request, 'notfound.html')