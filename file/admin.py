from django.contrib import admin
from .forms import *
from .models import *

# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):

    class Meta:
        form = FileForm
        
        
@admin.register(FilePost)
class FilePostAdmin(admin.ModelAdmin):
    
    class Meta:
        form = FilePostForm
        

@admin.register(FileSubCategory)
class FileSubCategoryAdmin(admin.ModelAdmin):
    
    class Meta:
        form = FileSubCategoryForm
        
@admin.register(FileCategory)
class FileCategoryAdmin(admin.ModelAdmin):
    
    class Meta:
        form = FileCategoryForm
        

@admin.register(FileProfile)
class FileProfileAdmin(admin.ModelAdmin):
    
    class Meta:
        form = FileProfileForm