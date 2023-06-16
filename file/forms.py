from django.forms import ModelForm
from .models import *
from django import forms


# def categoryQueryset():
#     try:
#         queryset = Category.objects.all()
#     except Category.DoesNotExist:
#         return None
#     return queryset

# def subCategoryQueryset():
#     try:
#         queryset = SubCategory.objects.all()
#     except SubCategory.DoesNotExist:
#         return None
#     return queryset

# def postQueryset():
#     try:
#         queryset = Post.objects.all()
#     except Post.DoesNotExist:
#         return None
#     return queryset

# def authQueryset(request):
#     try:
#         queryset = Users.objects.get(id = request.user.id)

#     except Users.DoesNotExist:
#         return None
#     return queryset

# def mediaQueryset(request):
#     try:
#         queryset = File.objects.filter(userId = request.user.id)

#     except File.DoesNotExist:
#         return None
#     return queryset

# def profileQueryset(request):
#     try:
#         queryset = UsersProfile.objects.get(userId = request.user.id)

#     except UsersProfile.DoesNotExist:
#         return None
#     return queryset


class FileForm(ModelForm):
    FILETYPE = (
        ("Image", "Image"),
        ("Video", "Video"),
        ("Audio", "Audio"),
        ("Document", "Document"),
        ("Others", "Others"),
    )

    userId = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "post",
                "class": "form-control",
                "value": "{{request.user.id}}",
            }
        ),
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "name", "class": "form-control"})
    )
    
    source = forms.FileField(
        widget=forms.FileInput(attrs={"placeholder": "file", "class": "form-control"})
    )

    fileType = forms.CharField(
        widget=forms.Select(
            choices=FILETYPE, attrs={"placeholder": "country", "class": "form-control"}
        )
    )

    class Meta:
        model = File
        fields = ("source", "userId", "fileType")


class FilePostForm(ModelForm):
    postId = forms.ChoiceField(
        widget=forms.Select(attrs={"placeholder": "post", "class": "form-control"}),
    )

    fileId = forms.ChoiceField(
        widget=forms.Select(attrs={"placeholder": "file", "class": "form-control"}),
    )

    class Meta:
        model = FilePost
        fields = ("postId", "fileId")


class FileCategoryForm(ModelForm):
    categoryId = forms.ChoiceField(
        widget=forms.Select(attrs={"placeholder": "category", "class": "form-control"}),
    )

    fileId = forms.ChoiceField(
        widget=forms.Select(attrs={"placeholder": "file", "class": "form-control"}),
    )

    class Meta:
        model = FileCategory
        fields = ("categoryId", "fileId")


class FileSubCategoryForm(ModelForm):
    subCategoryId = forms.ChoiceField(
        widget=forms.Select(
            attrs={"placeholder": "SubCategory", "class": "form-control"}
        ),
    )

    fileId = forms.ChoiceField(
        widget=forms.Select(attrs={"placeholder": "file", "class": "form-control"}),
    )

    class Meta:
        model = FileSubCategory
        fields = ("subCategoryId", "fileId")


class FileProfileForm(ModelForm):
    profileId = forms.ChoiceField(
        widget=forms.Select(
            attrs={"placeholder": "User Profile", "class": "form-control"}
        ),
    )

    fileId = forms.ChoiceField(
        widget=forms.Select(attrs={"placeholder": "file", "class": "form-control"}),
    )

    class Meta:
        model = FileProfile
        fields = ("profileId", "fileId")
