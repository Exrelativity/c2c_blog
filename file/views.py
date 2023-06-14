from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@login_required(login_url="/login")
def index(request, msg=None):
    try:
        fileById = File.objects.get(userId=request.user.id)
    except File.DoesNotExist:
        return redirect("/media/upload")
    status = 200
    if request.accepts('text/html'):
        return render(
        request,
        "file/index.html",
        {"msg": msg, "file": fileById},
    )
    else:
        data = {"msg": msg, "file": fileById}
        return JsonResponse(data, status)

@csrf_protect
@login_required(login_url="/login")
def create(request, msg=None):
    fileForm = FileForm()
    if request.method == "POST":
        fileForm = FileForm(request.POST, request.FILES)
        if fileForm.is_valid():
            obj = fileForm.save(commit=False)
            obj.name = fileForm.cleaned_data.get("name")
            obj.userId = request.user
            obj.source = request.FILES['source']
            obj.fileType = fileForm.cleaned_data.get("fileType")
            obj.save(force_create=True)
            msg = "uploaded sucessfully"
            status = 200
            return redirect()
        else:
            msg = "Error validating the form"
            status = 400
    else:
        msg = "Please fill all necessary feild to make a good entry"
    if request.accepts('text/html'):
        return render(request, "file/upload.html", {"fileForm": fileForm, "msg": msg})
    else:
        data = {
                "error":fileForm.errors,
                "fileForm": fileForm, 
                "msg": msg
            }
        return JsonResponse(data, status)

@csrf_protect      
@login_required(login_url="/login")
def update(request, id, msg=None):
    fileForm = FileForm(request.POST, request.FILES)
    fileById = File.objects.get(id=id)
    if request.method == "PUT":
        if fileForm.is_valid():
            if request.user.id == fileById.userId:
                fileById.name = fileForm.cleaned_data.get("name")
                fileById.save(force_update=True)
                msg = "Entries updated sucessfully"
            else:
                msg = "Permission Denied"
        else:
            msg = "Error validating the form"
    else:
        msg = "please fill in all infomation"
    return render(
        request,
        "file/update.html",
        {
            "form": fileForm,
            "msg": msg,
            "fileById": fileById
        },
    )

@login_required(login_url="/login")
def show(request, id, msg=None):
    try:
        fileById = File.objects.get(id=id)
    except File.DoesNotExist:
        return redirect(
             "/file", msg="Sorry this file does not exist"
        )
    meta = fileById.as_meta()

    status = 200
    if request.accepts('text/html'):
        return render(
        request,
        "file/show.html",
        {"msg": msg, "file": fileById, "meta": meta},
    )
    else:
        data =  {"msg": msg, "file": fileById, "meta": meta}
        return JsonResponse(data, status)




@login_required(login_url="/login")
def delete(request, id, msg=None):
    fileById = File.objects.get(id=id)
    if request.method == "DELETE" and request.user.id == fileById.userId:
        fileById.delete()
        msg = "Deteted sucessfully"
        response = redirect("/file", msg)
        status = 200
    else:
        msg = "Error deleting the entry"
        response = redirect(f"/file/{id}", msg)
        status = 400
    if request.accepts('text/html'):
        return response
    else:
        data =  {"msg": msg, "file": fileById}
        return JsonResponse(data, status)
