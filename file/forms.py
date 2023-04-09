from django.forms import ModelForm
from .models import *
from django import forms


class FileForm(ModelForm):
    FILETYPE = (
        ("Image", "Image"),
        ("Video", "Video"),
        ("Audio", "Audio"),
        ("Document", "Document"),
        ("Others", "Others"),
    )

    # userId = forms.ModelChoiceField(
    #     queryset=User.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "post", "class": "form-control"}
    #     ),
    # )

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
    # postId = forms.ModelChoiceField(
    #     queryset=Post.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "post", "class": "form-control"}
    #     ),
    # )

    # fileId = forms.ModelChoiceField(
    #     queryset=File.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "file", "class": "form-control"}
    #     ),
    # )
    class Meta:
        model = FilePost
        fields = ("postId", "fileId")


class FileCategoryForm(ModelForm):
    # categoryId = forms.ModelChoiceField(
    #     queryset=Category.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "category", "class": "form-control"}
    #     ),
    # )

    # fileId = forms.ModelChoiceField(
    #     queryset=File.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "file", "class": "form-control"}
    #     ),
    # )
    class Meta:
        model = FileCategory
        fields = ("categoryId", "fileId")


class FileSubCategoryForm(ModelForm):
    # subCategoryId = forms.ModelChoiceField(
    #     queryset=SubCategory.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "SubCategory", "class": "form-control"}
    #     ),
    # )

    # fileId = forms.ModelChoiceField(
    #     queryset=File.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "file", "class": "form-control"}
    #     ),
    # )
    class Meta:
        model = FileSubCategory
        fields = ("subCategoryId", "fileId")


class FileProfileForm(ModelForm):
    # profileId = forms.ModelChoiceField(
    #     queryset=UserProfile.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "User Profile", "class": "form-control"}
    #     ),
    # )

    # fileId = forms.ModelChoiceField(
    #     queryset=File.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "file", "class": "form-control"}
    #     ),
    # )

    class Meta:
        model = FileProfile
        fields = ("profileId", "fileId")
