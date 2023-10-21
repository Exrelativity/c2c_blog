from django.contrib import admin
from .models import UsersProfile

@admin.register(UsersProfile)
class UsersProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'date_of_birth', 'gender')
    list_filter = ('gender', 'date_of_birth')
    search_fields = ('user__username', 'first_name', 'last_name')
    ordering = ('user__username', 'date_of_birth')

    fieldsets = (
        (None, {
            'fields': ('user', 'first_name', 'last_name', 'date_of_birth', 'gender', 'zipcode')
        }),
        ('Location Info', {
            'fields': ('address', 'city', 'region', 'country', 'longitude', 'latitude')
        }),
        ('Additional Info', {
            'fields': ('popularity', 'details')
        }),
    )
