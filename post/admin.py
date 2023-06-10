from django.contrib import admin
from .forms import *
from .models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        form = CategoryForm


@admin.register(SubCategory)
class SubCatgoryAdmin(admin.ModelAdmin):
    class Meta:
        form = SubCategoryForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Meta:
        form = PostForm

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    class Meta:
        form = CommentForm