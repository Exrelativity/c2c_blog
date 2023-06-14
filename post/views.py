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

# Create your views here.
def index(request, msg=None):
    category = Category.objects.filter(status=True)
    subCategory = SubCategory.objects.filter(status=True)
    post = Post.objects.filter(status=True)
    paginator = Paginator(post, 15)  # Show 15 posts per page.
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
            obj.categoryId = postForm.cleaned_data.get("categoryId")
            obj.subCategoryId = postForm.cleaned_data.get("subCategoryId")
            obj.userId = request.user.id
            obj.save(force_create=True)
            for i in postForm.cleaned_data.get("media"):
                FilePost.objects.create(postId=postForm.instance.id, fileId=i)
            msg = "Entries saved sucessfully"
        else:
            msg = "Error validating the form"
    else:
        msg = "please fill in all infomation"
    return render(
        request,
        "post/create.html",
        {
            "form": postForm,
            "fileForm":fileForm,
            "msg": msg,
            "categorys": category,
            "subCategorys": subCategory,
        },
    )


def search(request, msg=None):
    form = SearchForm(request.POST)
    post = {}
    if request.method == "POST":
        if form.is_valid():
            search = form.cleaned_data.get("search")
            search_list = search.split(" ")
            for i in search_list:
                post += Post.objects.filter(
                    Q(title__icontains=i) | Q(content__icontains=i)
                )
    paginator = Paginator(post, 15)  # Show 15 posts per page.
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
        postById = Post.objects.select_related("UserId").get(id=id)
        relatedPostByCategory = Category.objects.prefetch_related("Post").get(
            id=postById.categoryId
        )
        relatedPostBySubCategory = SubCategory.objects.prefetch_related("Post").get(
            id=postById.subCategoryId
        )
    except Post.DoesNotExist:
        msg = "Sorry Post Dost not exist"
    meta = postById.as_meta()
    if request.user.is_authenticated:
        return render(
            request,
            "post/show.html",
            {
                "msg": msg,
                "post": postById,
                "relatedPostByCategory": relatedPostByCategory,
                "relatedPostBySubCategory": relatedPostBySubCategory,
                "meta": meta,
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
                "meta": meta,
            },
        )

@csrf_protect
@login_required(login_url="/login")
def update(request, id, msg=None):
    postForm = PostMutationForm(request.POST, request.FILES)
    postById = Post.objects.get(id=id)
    category = Category.objects.all()
    subCategory = SubCategory.objects.all()
    if request.method == "PUT":
        if postForm.is_valid():
            if request.user.id == postById.userId:
                postById.title = postForm.cleaned_data.get("title")
                postById.status = postForm.cleaned_data.get("status")
                postById.front = postForm.cleaned_data.get("front")
                postById.slider = postForm.cleaned_data.get("slider")
                postById.content = postForm.cleaned_data.get("content")
                postById.categoryId = postForm.cleaned_data.get("categoryId")
                postById.subCategoryId = postForm.cleaned_data.get("subCategoryId")
                postById.save(force_update=True)
                msg = "Entries updated sucessfully"
            else:
                msg = "Permission Denied"
        else:
            msg = "Error validating the form"
    else:
        msg = "please fill in all infomation"
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


@login_required(login_url="/login")
def delete(request, id, msg=None):
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


def byCategory(request, categoryId, msg=None):
    category = Category.objects.filter(status=True)
    subCategory = SubCategory.objects.filter(status=True)
    post = Post.objects.filter(categoryId=categoryId)
    paginator = Paginator(post, 15)  # Show 15 contacts per page.
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
    post = Post.objects.filter(subCategoryId=subCategoryId)
    paginator = Paginator(post, 15)  # Show 15 contacts per page.
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
    commentForm = CommentForm(request.POST or None)
    if request.method == "POST":
        if commentForm.is_valid:
            commentForm.cleaned_data.all()
            commentForm.instance.userId = request.user.id
            commentForm.instance.save(force_create=True)
            msg = "Entries saved sucessfully"
            status = 200
        else:
            msg = "Error validating the form"
            status = 200
    else:
        msg = "please fill in all infomation"
    data = {"form": commentForm, "msg": msg}
    return JsonResponse(data, status)


def postComments(request, postId):
    comments = Comment.objects.filter(postId=postId)
    msg = "list of comments associated with post"
    status = 200
    data = {"comments": comments, "msg": msg}
    return JsonResponse(data, status)


@login_required(login_url="/login")
def deleteComment(request, id, msg=None):
    commentById = Comment.objects.get(id=id)
    if request.method == "DELETE":
        if request.user.id == commentById.userId:
            commentById.delete()
            msg = "Deteted sucessfully"
        else:
            msg = "Permission Denied"
    else:
        msg = "Error deleting the entry"
        return redirect(f"show/{id}", msg)
    return redirect("/post/", msg)
