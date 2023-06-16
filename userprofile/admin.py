from django.contrib import admin
from .models import UsersProfile


# Register your models here.
@admin.register(UsersProfile)
class UsersprofileAdmin(admin.ModelAdmin):
    pass
