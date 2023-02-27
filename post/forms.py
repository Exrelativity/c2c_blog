from django.forms import ModelForm
from .models import *
from django import forms

class PostMutationForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ("id","title","image","content","userId")


class CategoryMutationForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ("id","name","userId")
        

class SubCategoryMutationForm(ModelForm):
    
    class Meta:
        model = SubCategory
        fields = ("id","name","categoryId","userId")
        
        
        
        
class PostForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placholder":"title",
                "class":"form-control"}
            ))
    image = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "placholder":"image",
                "class":"form-control"}
            ))
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placholder":"content",
                "class":"form-control"}
            ))
    userId = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                "placholder":"userId",
                "class":"form-control"}
            ))
    
    class Meta:
        model = Post
        fields = ("title","image","content","userId")


class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ("name","userId")
        

class SubCategoryForm(ModelForm):
    
    class Meta:
        model = SubCategory
        fields = ("name","categoryId","userId")