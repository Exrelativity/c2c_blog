from django.contrib import admin
from .forms import *

# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    class Meta:
        form = UsersMutationForm
        
