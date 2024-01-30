from django.contrib import admin
from .models import *


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display= ('cart_id', 'date_added')
    
@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display= ('product', 'cart', 'quantity', 'is_active')
    
    
# Register your models here.

