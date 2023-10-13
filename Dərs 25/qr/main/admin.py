from django.contrib import admin

# Register your models here.
from . models import CustomUser


admin.site.register(CustomUser)

def block_users(modeladmin, request, queryset):
    queryset.update(is_active=False)

def activate_users(modeladmin, request, queryset):
    queryset.update(is_active=True)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')
    actions = [block_users, activate_users]
