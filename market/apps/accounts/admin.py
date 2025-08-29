from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as Base


@admin.register(User)
class UserAdmin(Base):
fieldsets = Base.fieldsets + (("Extra", {"fields": ("email",)}),)
list_display = ("id", "username", "email", "is_staff", "date_joined")