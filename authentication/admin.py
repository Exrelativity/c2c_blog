from django.contrib import admin
from .forms import UserForm
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    class Meta:
        form = UserForm
    