from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import JsonResponse
from asgiref.sync import sync_to_async

# Create your views here.
@login_required(login_url="/login")
def index(request, msg=None):
    fileById = File.objects.get(userId=request.user.id)
    status = 200
    if request.accepts('text/html'):
        return render(
        request,
        "file/list.html",
        {"msg": msg, "file": fileById},
    )
    else:
        data = {"msg": msg, "file": fileById}
        return JsonResponse(data, status)
    
@login_required(login_url="/login")
async def create(request, msg=None):
    fileForm = fileForm()
    if request.method == "POST":
        fileForm = fileForm(request.POST, request.FILES)
        if fileForm.is_valid():
            fileForm.cleaned_data.all()
            fileForm.instance.userId = request.user.id

            await sync_to_async(fileForm.save(), thread_sensitive=True)
            msg = "uploaded sucessfully"
            status = 200
            return redirect("file")
        else:
            msg = "Error validating the form"
            status = 400
    else:
        msg = "Please fill all necessary feild to make a good entry"
    if request.accepts('text/html'):
        return render(request, "file/upload.html", {"form": fileForm, "msg": msg})
    else:
        data = {
                "error":fileForm.errors,
                "form": fileForm, 
                "msg": msg
            }
        return JsonResponse(data, status)
       


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
        fileById.soft_delete()
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
