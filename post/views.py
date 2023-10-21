from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *
from file.models import FilePost
from file.forms import FileForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request, msg=None):
    category = Category.objects.filter(status=True)
    subCategory = SubCategory.objects.filter(status=True)
    post = Post.objects.filter(status=True)
    paginator = Paginator(post, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.user.is_authenticated:
        return render(
            request,
            "post/index.html",
            {
                "msg": msg,
                "category": category,
                "subCategory": subCategory,
                "page_obj": page_obj,
            },
        )
    else:
        return render(
            request,
            "post-front/index.html",
            {
                "msg": msg,
                "category": category,
                "subCategory": subCategory,
                "page_obj": page_obj,
            },
        )

@csrf_protect
@login_required(login_url="/login")
def create(request, msg=None):
    postForm = PostForm(request.POST, request.FILES)
    fileForm = FileForm(request.POST or None, request.FILES)
    category = Category.objects.all()
    subCategory = SubCategory.objects.all()
    if request.method == "POST":
        if postForm.is_valid():
            obj = postForm.save(commit=False)
            obj.title = postForm.cleaned_data.get("title")
            obj.status = postForm.cleaned_data.get("status")
            obj.front = postForm.cleaned_data.get("front")
            obj.slider = postForm.cleaned_data.get("slider")
            obj.content = postForm.cleaned_data.get("content")
            obj.categoryId = Category.objects.get(id=postForm.cleaned_data.get("categoryId"))
            obj.subCategoryId = SubCategory.objects.get(id=postForm.cleaned_data.get("subCategoryId"))
            obj.userId = request.user
            obj.save()
            for i in postForm.cleaned_data.get("media"):
                FilePost.objects.create(postId=obj, fileId=i)
            msg = "Entries saved successfully"
        else:
            msg = "Error validating the form"
    else:
        msg = "Please fill in all information"
    return render(
        request,
        "post/create.html",
        {
            "form": postForm,
            "fileForm": fileForm,
            "msg": msg,
            "categorys": category,
            "subCategorys": subCategory,
        },
    )

def search(request, msg=None):
    form = SearchForm(request.POST)
    post = []
    if request.method == "POST":
        if form.is_valid():
            search = form.cleaned_data.get("search")
            search_list = search.split(" ")
            for i in search_list:
                post += Post.objects.filter(
                    Q(title__icontains=i) | Q(content__icontains=i)
                )
    paginator = Paginator(post, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.user.is_authenticated:
        return render(
            request,
            "post/search.html",
            {"msg": msg, "form": form, "page_obj": page_obj},
        )
    else:
        return render(
            request,
            "post-front/search.html",
            {"msg": msg, "form": form, "page_obj": page_obj},
        )

def show(request, id, msg=None):
    try:
        postById = Post.objects.get(id=id)
        relatedPostByCategory = postById.category.post_set.all()
        relatedPostBySubCategory = postById.subCategory.post_set.all()
    except ObjectDoesNotExist:
        msg = "Sorry, this post does not exist"

    if request.user.is_authenticated:
        return render(
            request,
            "post/show.html",
            {
                "msg": msg,
                "post": postById,
                "relatedPostByCategory": relatedPostByCategory,
                "relatedPostBySubCategory": relatedPostBySubCategory,
            },
        )
    else:
        return render(
            request,
            "post-front/show.html",
            {
                "msg": msg,
                "post": postById,
                "relatedPostByCategory": relatedPostByCategory,
                "relatedPostBySubCategory": relatedPostBySubCategory,
            },
        )

@csrf_protect
@login_required(login_url="/login")
def update(request, id, msg=None):
    try:
        postById = Post.objects.get(id=id)
        postForm = PostMutationForm(request.POST or None, instance=postById)
        category = Category.objects.all()
        subCategory = SubCategory.objects.all()
        if request.method == "POST":
            if postForm.is_valid():
                if request.user.id == postById.userId.id:
                    postForm.save()
                    msg = "Entry updated successfully"
                else:
                    msg = "Permission Denied"
            else:
                msg = "Error validating the form"
        else:
            msg = "Please fill in all information"
        return render(
            request,
            "post/update.html",
            {
                "form": postForm,
                "msg": msg,
                "postById": postById,
                "category": category,
                "subCategory": subCategory,
            },
        )
    except ObjectDoesNotExist:
        msg = "Sorry, this post does not exist"
        return render(request, "post/update.html", {"msg": msg})

@login_required(login_url="/login")
def delete(request, id, msg=None):
    try:
        postById = Post.objects.get(id=id)
        if request.method == "POST":
            if request.user.id == postById.userId.id:
                postById.delete()
                msg = "Deleted successfully"
            else:
                msg = "Permission Denied"
        else:
            msg = "Error deleting the entry"
        return redirect("/post/", msg)
    except ObjectDoesNotExist:
        msg = "Sorry, this post does not exist"
        return redirect("/post/", msg)

def byCategory(request, categoryId, msg=None):
    category = Category.objects.filter(status=True)
    subCategory = SubCategory.objects.filter(status=True)
    post = Post.objects.filter(categoryId=categoryId, status=True)
    paginator = Paginator(post, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "post/list.html",
        {
            "msg": msg,
            "category": category,
            "subCategory": subCategory,
            "page_obj": page_obj,
        },
    )

def bySubCategory(request, categoryId, subCategoryId, msg=None):
    category = Category.objects.filter(status=True)
    subCategory = SubCategory.objects.filter(status=True)
    post = Post.objects.filter(subCategoryId=subCategoryId, status=True)
    paginator = Paginator(post, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "post/list.html",
        {
            "msg": msg,
            "category": category,
            "subCategory": subCategory,
            "page_obj": page_obj,
        },
    )

def createComment(request):
    if request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.userId = request.user
            comment.save()
            msg = "Entry saved successfully"
            status = 200
        else:
            msg = "Error validating the form"
            status = 400
    else:
        msg = "Please fill in all information"
        status = 400
    data = {"msg": msg}
    return JsonResponse(data, status=status)

def postComments(request, postId):
    comments = Comment.objects.filter(postId=postId)
    msg = "List of comments associated with the post"
    status = 200
    data = {"comments": comments, "msg": msg}
    return JsonResponse(data, status=status)

@login_required(login_url="/login")
def deleteComment(request, id, msg=None):
    try:
        commentById = Comment.objects.get(id=id)
        if request.method == "POST":
            if request.user.id == commentById.userId.id:
                commentById.delete()
                msg = "Deleted successfully"
            else:
                msg = "Permission Denied"
        else:
            msg = "Error deleting the entry"
        return redirect("/post/", msg)
    except ObjectDoesNotExist:
        msg = "Sorry, this comment does not exist"
        return redirect("/post/", msg)
