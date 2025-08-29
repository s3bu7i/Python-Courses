from django.contrib import admin
from .models import EmailPref
@admin.register(EmailPref)
class EmailPrefAdmin(admin.ModelAdmin):
list_display = ('id','user','new_message','listing_status','promotions','saved_search_hits')