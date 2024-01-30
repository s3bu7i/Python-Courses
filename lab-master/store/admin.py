from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ('product_name', 'price', 'stock' )
    prepopulated_fields = {'slug': ('product_name',)}


@admin.register(Variation)
class Variation(admin.ModelAdmin):
    list_display= ('product', 'variation_category', 'variation_value','is_active' )
    list_editable= ('is_active', )
    
