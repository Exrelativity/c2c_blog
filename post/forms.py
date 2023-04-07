from django.forms import ModelForm
from .models import *
from django import forms


class PostMutationForm(ModelForm):
    id = forms.ModelChoiceField(
        widget=forms.HiddenInput(attrs={"placeholder": "id", "class": "form-control"})
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "title", "class": "form-control"})
    )
    status = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "status", "class": "form-control"}
        )
    )
    front = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "front", "class": "form-control"}
        )
    )
    slider = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "slider", "class": "form-control"}
        )
    )
    image = forms.FileField(
        widget=forms.FileInput(attrs={"placeholder": "image", "class": "form-control"})
    )
    content = forms.CharField(
        widget=forms.HiddenInput(
            attrs={"placeholder": "content", "class": "form-control"}
        )
    )
    userId = forms.ModelChoiceField(
        widget=forms.HiddenInput(
            attrs={"placeholder": "userId", "class": "form-control"}
        )
    )
    categoryId = forms.ModelChoiceField(
        queryset="",
        widget=forms.Select(
            attrs={"placeholder": "categoryId", "class": "form-control"}
        ),
    )

    subCategoryId = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "status",
            "front",
            "slider",
            "image",
            "content",
            "userId",
            "categoryId",
            "subCategoryId",
        )


class CategoryMutationForm(ModelForm):
    id = forms.ModelChoiceField(
        widget=forms.HiddenInput(attrs={"placeholder": "id", "class": "form-control"})
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    status = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    front = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    image = forms.FileField(
        widget=forms.FileInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    description = forms.TextField(
        widget=forms.TextInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )

    userId = forms.ModelChoiceField(
        widget=forms.HiddenInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )

    class Meta:
        model = Category
        fields = ("id", "name", "status", "front", "image", "description", "userId")


class SubCategoryMutationForm(ModelForm):
    id = forms.ModelChoiceField(
        widget=forms.HiddenInput(attrs={"placeholder": "id", "class": "form-control"})
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    status = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    front = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    image = forms.FileField(
        widget=forms.FileInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    description = forms.TextField(
        widget=forms.TextInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    categoryId = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )

    userId = forms.ModelChoiceField(
        widget=forms.HiddenInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )

    class Meta:
        model = SubCategory
        fields = (
            "id",
            "name",
            "status",
            "front",
            "image",
            "description",
            "categoryId",
            "userId",
        )


class PostForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "title", "class": "form-control"})
    )
    status = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "status", "class": "form-control"}
        )
    )
    front = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "front", "class": "form-control"}
        )
    )
    slider = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "slider", "class": "form-control"}
        )
    )
    image = forms.FileField(
        widget=forms.FileInput(attrs={"placeholder": "image", "class": "form-control"})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "content", "class": "form-control"})
    )
    userId = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                "placeholder": "userId",
                "class": "form-control",
                "value": request.user.id,
            }
        )
    )
    categoryId = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        widget=forms.Select(
            attrs={"placeholder": "categoryId", "class": "form-control"}
        ),
    )
    subCategoryId = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        widget=forms.Select(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        ),
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "status",
            "front",
            "slider",
            "image",
            "content",
            "userId",
            "categoryId",
            "subCategoryId",
        )


class CategoryForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    status = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    front = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    image = forms.FileField(
        widget=forms.FileInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    description = forms.TextField(
        widget=forms.TextInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )

    userId = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                "placeholder": "userId",
                "class": "form-control",
                "value": request.user.id,
            }
        )
    )

    class Meta:
        model = Category
        fields = ("name", "status", "front", "image", "description", "userId")


class SubCategoryForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    status = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    front = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    image = forms.FileField(
        widget=forms.FileInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )
    description = forms.TextField(
        widget=forms.TextInput(
            attrs={"placeholder": "subCategoryId", "class": "form-control"}
        )
    )

    categoryId = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        widget=forms.Select(
            attrs={"placeholder": "categoryId", "class": "form-control"}
        ),
    )

    userId = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                "placeholder": "userId",
                "class": "form-control",
                "value": request.user.id,
            }
        )
    )

    class Meta:
        model = SubCategory
        fields = (
            "name",
            "status",
            "front",
            "image",
            "description",
            "categoryId",
            "userId",
        )


class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "search", "class": "form-control"})
    )
