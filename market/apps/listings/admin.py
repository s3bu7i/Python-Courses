from django.contrib import admin
from .models import Listing, ListingImage, Favorite


class ImageInline(admin.TabularInline):
model = ListingImage
extra = 0


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
list_display = ('id','title','user','category','price_cents','currency','status','created_at')
list_filter = ('status','category')
inlines = [ImageInline]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
list_display = ('id','user','listing','created_at')