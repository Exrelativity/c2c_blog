from django.contrib import admin
from .models import Users
from .forms import UsersMutationForm

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    form = UsersMutationForm
