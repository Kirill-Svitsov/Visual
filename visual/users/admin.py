from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'registration_date', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('-registration_date',)
