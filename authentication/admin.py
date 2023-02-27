from django.contrib import admin
from .mutationForms import *

# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    class Meta:
        model = UsersMutationForm
        
