from django.forms import ModelForm
from .models import *
from django import forms


class PostMutationForm(ModelForm):


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
    
    # categoryId = forms.ModelChoiceField(
    #     queryset=Category.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "category", "class": "form-control"}
    #     ),
    # )

    # subCategoryId = forms.ModelChoiceField(
    #     queryset=SubCategory.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "sub Category", "class": "form-control"}
    #     )
    # )

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

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "name", "class": "form-control"}
        )
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
    
    image = forms.FileField(
        widget=forms.FileInput(
            attrs={"placeholder": "image", "class": "form-control"}
        )
    )
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "description", "class": "form-control"}
        )
    )


    class Meta:
        model = Category
        fields = ("id", "name", "status", "front", "image", "description")


class SubCategoryMutationForm(ModelForm):


    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "name", "class": "form-control"}
        )
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
    
    image = forms.FileField(
        widget=forms.FileInput(
            attrs={"placeholder": "image", "class": "form-control"}
        )
    )
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "description", "class": "form-control"}
        )
    )
    
    # categoryId = forms.ModelChoiceField(
    #     queryset=Category.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "category", "class": "form-control"}
    #     )
    # )

    class Meta:
        model = SubCategory
        fields = (
            "id",
            "name",
            "status",
            "front",
            "image",
            "description",
            "categoryId"
            
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
    

    # categoryId = forms.ModelChoiceField(
    #     queryset=SubCategory.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "category", "class": "form-control"}
    #     ),
    # )
    
    # subCategoryId = forms.ModelChoiceField(
    #     queryset=SubCategory.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "subCategory", "class": "form-control"}
    #     ),
    # )

    class Meta:
        model = Post
        fields = (
            "title",
            "status",
            "front",
            "slider",
            "image",
            "content",
            "categoryId",
            "subCategoryId",
        )


class CategoryForm(ModelForm):

        
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "name", "class": "form-control"}
        )
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
    
    image = forms.FileField(
        widget=forms.FileInput(
            attrs={"placeholder": "image", "class": "form-control"}
        )
    )
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "description", "class": "form-control"}
        )
    )


    class Meta:
        model = Category
        fields = ("name", "status", "front", "image", "description")


class SubCategoryForm(ModelForm):
        
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "name", "class": "form-control"}
        )
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
    
    image = forms.FileField(
        widget=forms.FileInput(
            attrs={"placeholder": "image", "class": "form-control"}
        )
    )
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "description", "class": "form-control"}
        )
    )

    # categoryId = forms.ModelChoiceField(
    #     queryset=Category.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "category", "class": "form-control"}
    #     ),
    # )


    class Meta:
        model = SubCategory
        fields = (
            "name",
            "status",
            "front",
            "image",
            "description",
            "categoryId"
            
        )

class CommentsForm(ModelForm):
    # postId = forms.ModelChoiceField(
    #     queryset=Post.objects.all() or None,
    #     widget=forms.Select(
    #         attrs={"placeholder": "post", "class": "form-control"}
    #     ),
    # )
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "content", "class": "form-control"})
    )
    
    class Meta:
        model = Comments
        fields = (
            "postId",
            "userId",
            "content"
        )
    
    
class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "search", "class": "form-control"})
    )
