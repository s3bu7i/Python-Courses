from django.contrib import admin

from . models import *

admin.site.register(Test)

@admin.register(News_data)
class NewsAdmin(admin.ModelAdmin):
    
    
    class Meta:
        model = News_data
        
    list_display = ["title","category"]
    list_display_links = ["title"]
    search_fields = ["category"]
    list_editable = ["category"]