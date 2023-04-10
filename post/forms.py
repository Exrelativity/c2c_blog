from django.forms import ModelForm
from .models import *
from django import forms
# from file.models import File

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
#     except SubCategory.DoesNotExist:
#         return None
#     return queryset

# def mediaQueryset(request):
#     try:
#         queryset = File.objects.filter(userId = request.user.id)
       
#     except File.DoesNotExist:
#         return None
#     return queryset

# def authQueryset(request):
#     try:
#         queryset = Users.objects.get(id = request.user.id)

#     except Users.DoesNotExist:
#         return None
#     return queryset
    
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
    
    content = forms.CharField(
        widget=forms.HiddenInput(
            attrs={"placeholder": "content", "class": "form-control"}
        )
    )
    
    categoryId = forms.ChoiceField(
        widget=forms.Select(
            attrs={"placeholder": "category", "class": "form-control"}
        ),
    )

    subCategoryId = forms.ChoiceField(
        widget=forms.Select(
            attrs={"placeholder": "sub Category", "class": "form-control"}
        )
    )
    
    media = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={
            "placeholder":"profile medias",
            "class":"form-control"}
        )
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "status",
            "front",
            "slider",
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
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "description", "class": "form-control"}
        )
    )
    
    media = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={
            "placeholder":"profile medias",
            "class":"form-control"}
        )
    )


    class Meta:
        model = Category
        fields = ("name", "status", "front", "description")


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
    
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "description", "class": "form-control"}
        )
    )
    
    categoryId = forms.ChoiceField(
        widget=forms.Select(
            attrs={"placeholder": "category", "class": "form-control"}
        ),
    )

    media = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={
            "placeholder":"profile medias",
            "class":"form-control"}
        )
    )
    class Meta:
        model = SubCategory
        fields = (
            "name",
            "status",
            "front",
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
    
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "content", "class": "form-control"})
    )
    

    categoryId = forms.ChoiceField(
        
        widget=forms.Select(
            attrs={"placeholder": "category", "class": "form-control"}
        ),
    )

    subCategoryId = forms.ChoiceField(
        widget=forms.Select(
            attrs={"placeholder": "sub Category", "class": "form-control"}
        )
    )
    
    media = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={
            "placeholder":"profile medias",
            "class":"form-control"}
        )
    )
    class Meta:
        model = Post
        fields = (
            "title",
            "status",
            "front",
            "slider",
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
    
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "description", "class": "form-control"}
        )
    )

    media = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={
            "placeholder":"profile medias",
            "class":"form-control"}
        )
    )

    class Meta:
        model = Category
        fields = ("name", "status", "front", "description")


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
    
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "description", "class": "form-control"}
        )
    )
    
    categoryId = forms.ChoiceField(
        
        widget=forms.Select(
            attrs={"placeholder": "category", "class": "form-control"}
        ),
    )

    media = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={
            "placeholder":"profile medias",
            "class":"form-control"}
        )
    )

    class Meta:
        model = SubCategory
        fields = (
            "name",
            "status",
            "front",
            "description",
            "categoryId"
            
        )

class CommentForm(ModelForm):
    postId = forms.ChoiceField(
    widget=forms.Select(
            attrs={"placeholder": "post", "class": "form-control"}
        ),
    )
    
    userId = forms.ChoiceField(
        widget=forms.Select(
            attrs={"placeholder": "user", "class": "form-control"}
        ),
    )
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "content", "class": "form-control"})
    )
    
    class Meta:
        model = Comment
        fields = (
            "postId",
            "userId",
            "content"
        )
    
    
class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "search", "class": "form-control"})
    )
