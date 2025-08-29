from rest_framework import serializers
from .models import EmailPref
class EmailPrefOut(serializers.ModelSerializer):
class Meta:
model = EmailPref
fields = ('new_message','listing_status','promotions','saved_search_hits')