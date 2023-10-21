from django.contrib import admin
from .models import File, FilePost, FileSubCategory, FileCategory, FileProfile

# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass

@admin.register(FilePost)
class FilePostAdmin(admin.ModelAdmin):
    pass

@admin.register(FileSubCategory)
class FileSubCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(FileCategory)
class FileCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(FileProfile)
class FileProfileAdmin(admin.ModelAdmin):
    pass
