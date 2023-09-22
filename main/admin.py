from django.contrib import admin

# Register your models here.
from .models import Student


admin.site.register(Student)


admin.site.site_header = 'Django admine xosh geldiniz'
admin.site.site_title
admin.site.site_url