from django.forms import ModelForm, Form, TextInput, HiddenInput, Select, SelectMultiple, RadioSelect, CheckboxInput
from .models import Category, SubCategory, Post, Comment

# Common fields for forms
class CommonForm(ModelForm):
    name = forms.CharField(
        widget=TextInput(attrs={"placeholder": "name", "class": "form-control"})
    )

    status = forms.BooleanField(
        widget=CheckboxInput(attrs={"placeholder": "status", "class": "form-control"})
    )

    front = forms.BooleanField(
        widget=CheckboxInput(attrs={"placeholder": "front", "class": "form-control"})
    )

    description = forms.CharField(
        widget=TextInput(attrs={"placeholder": "description", "class": "form-control"})
    )

    media = forms.MultipleChoiceField(
        widget=SelectMultiple(attrs={"placeholder": "profile medias", "class": "form-control"})
    )

# Forms for your models
class CategoryMutationForm(CommonForm):
    """
    Form for creating or updating a Category.
    """
    class Meta:
        model = Category
        fields = ("name", "status", "front", "description")

class SubCategoryMutationForm(CommonForm):
    """
    Form for creating or updating a SubCategory.
    """
    category = forms.ModelChoiceField(
        widget=Select(attrs={"placeholder": "category", "class": "form-control"}),
        queryset=Category.objects.all()
    )

    class Meta:
        model = SubCategory
        fields = ("name", "status", "front", "description", "category")

class PostMutationForm(ModelForm):
    """
    Form for creating or updating a Post.
    """
    class Meta:
        model = Post
        fields = ("title", "status", "front", "slider", "content", "category", "sub_category")

# Existing forms without "Mutation" in their names
class PostForm(ModelForm):
    """
    Form for creating or updating a Post.
    """
    class Meta:
        model = Post
        fields = ("title", "status", "front", "slider", "content", "category", "sub_category")

class CommentForm(ModelForm):
    """
    Form for creating or updating a Comment.
    """
    class Meta:
        model = Comment
        fields = ("post", "user", "content")

class SearchForm(Form):
    """
    Form for searching.
    """
    search = forms.CharField(
        widget=TextInput(attrs={"placeholder": "search", "class": "form-control"})
    )
