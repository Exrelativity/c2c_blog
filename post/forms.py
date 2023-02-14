from django.forms import ModelForm
from .models import *

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