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
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"title",
                "class":"form-control"}
            ))
    status = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"status",
                "class":"form-control"}
            ))
    front = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"front",
                "class":"form-control"}
            ))
    slider = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"slider",
                "class":"form-control"}
            ))
    image = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"image",
                "class":"form-control"}
            ))
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"content",
                "class":"form-control"}
            ))
    userId = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"userId",
                "class":"form-control"}
            ))
    categoryId = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"categoryId",
                "class":"form-control"}
            ))
    subCategoryId = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"subCategoryId",
                "class":"form-control"}
            ))
    class Meta:
        model = Post
        fields = ("title","status","front","slider","image","content","userId","categoryId","subCategoryId")


class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ("name","status","front","image","description","userId")
        

class SubCategoryForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"subCategoryId",
                "class":"form-control"}
            ))
    status = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"subCategoryId",
                "class":"form-control"}
            ))
    front = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"subCategoryId",
                "class":"form-control"}
            ))
    image = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"subCategoryId",
                "class":"form-control"}
            ))
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"subCategoryId",
                "class":"form-control"}
            ))
    categoryId = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"subCategoryId",
                "class":"form-control"}
            ))
    userId = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"subCategoryId",
                "class":"form-control"}
            ))
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