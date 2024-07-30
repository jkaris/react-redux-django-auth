from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin model for CustomUser
    """
    list_display = ("username", "email")
    list_display_links = ("username", "email")
    prepopulated_fields = {"username": ("username",)}
