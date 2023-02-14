from django.contrib import admin
from .models import Usersprofile
# Register your models here.
@admin.register(Usersprofile)
class UsersprofileAdmin(admin.ModelAdmin):
    pass
