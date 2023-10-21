from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import File
from .forms import FileForm
from django.http import JsonResponse

@login_required(login_url="/login")
def index(request, msg=None):
    file = get_object_or_404(File, userId=request.user.id)
    if request.accepts('text/html'):
        return render(request, "file/index.html", {"msg": msg, "file": file})
    else:
        data = {"msg": msg, "file": file}
        return JsonResponse(data, status=200)

@csrf_exempt
@login_required(login_url="/login")
def create(request, msg=None):
    if request.method == "POST":
        fileForm = FileForm(request.POST, request.FILES)
        if fileForm.is_valid():
            obj = fileForm.save(commit=False)
            obj.name = fileForm.cleaned_data.get("name")
            obj.userId = request.user
            obj.source = request.FILES['source']
            obj.fileType = fileForm.cleaned_data.get("fileType")
            obj.save()
            msg = "Uploaded successfully"
            if request.accepts('text/html'):
                return redirect("index")
            else:
                return JsonResponse({"msg": msg}, status=201)
        else:
            msg = "Error validating the form"
            status = 400
    else:
        msg = "Please fill in all necessary fields"
    if request.accepts('text/html'):
        return render(request, "file/upload.html", {"fileForm": fileForm, "msg": msg})
    else:
        return JsonResponse({"error": fileForm.errors, "msg": msg}, status=400)

# Other views (update, show, delete) can be refactored in a similar way.


@login_required(login_url="/login")
def update(request, id, msg=None):
    file = get_object_or_404(File, id=id)
    if request.method == "PUT":
        fileForm = FileForm(request.POST, request.FILES, instance=file)
        if fileForm.is_valid():
            if request.user.id == file.userId.id:
                file.name = fileForm.cleaned_data.get("name")
                file.save()
                msg = "Entry updated successfully"
                if request.accepts('text/html'):
                    return redirect("show", id=id)
                else:
                    return JsonResponse({"msg": msg}, status=200)
            else:
                msg = "Permission Denied"
        else:
            msg = "Error validating the form"
    else:
        msg = "Please fill in all information"
    if request.accepts('text/html'):
        return render(request, "file/update.html", {"form": fileForm, "msg": msg, "file": file})
    else:
        return JsonResponse({"error": fileForm.errors, "msg": msg}, status=400)

@login_required(login_url="/login")
def show(request, id, msg=None):
    file = get_object_or_404(File, id=id)
    meta = file.as_meta()
    if request.accepts('text/html'):
        return render(request, "file/show.html", {"msg": msg, "file": file, "meta": meta})
    else:
        data = {"msg": msg, "file": file, "meta": meta}
        return JsonResponse(data, status=200)

@login_required(login_url="/login")
def delete(request, id, msg=None):
    file = get_object_or_404(File, id=id)
    if request.method == "DELETE" and request.user.id == file.userId.id:
        file.delete()
        msg = "Deleted successfully"
        if request.accepts('text/html'):
            return redirect("index", msg)
        else:
            return JsonResponse({"msg": msg}, status=204)
    else:
        msg = "Error deleting the entry"
        if request.accepts('text/html'):
            return redirect("show", id=id, msg)
        else:
            return JsonResponse({"msg": msg}, status=400)
