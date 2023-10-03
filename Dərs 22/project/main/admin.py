from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Student)
admin.site.register(Telefon)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Item)








admin.site.site_header = 'Django admine xosh geldiniz'
admin.site.site_title
admin.site.site_url