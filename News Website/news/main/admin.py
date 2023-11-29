from django.contrib import admin

from . models import *

admin.site.register(News_data)
# admin.site.register(Test)

admin.site.site_header = 'Salam'
admin.site.site_title = 'Admin'
admin.site.site_url = 'Admi'