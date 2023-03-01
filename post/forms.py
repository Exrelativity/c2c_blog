from django.forms import ModelForm
from .models import *
from django import forms

class PostMutationForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ("id","title","status","front","slider","image","content","userId","categoryId","subCategoryId")


class CategoryMutationForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ("id","name","status","front","image","description","userId")
        

class SubCategoryMutationForm(ModelForm):
    
    class Meta:
        model = SubCategory
        fields = ("id","name","status","front","image","description","categoryId","userId")
        
        
        
        
class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","status","front","slider","image","content","userId","categoryId","subCategoryId")


class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ("name","status","front","image","description","userId")
        

class SubCategoryForm(ModelForm):
    
    class Meta:
        model = SubCategory
        fields = ("name","status","front","image","description","categoryId","userId")

class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"search",
                "class":"form-control"}
            ))