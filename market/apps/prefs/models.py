from django.db import models
from django.conf import settings


class EmailPref(models.Model):
user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='email_prefs')
new_message = models.BooleanField(default=True)
listing_status = models.BooleanField(default=True)
promotions = models.BooleanField(default=False)
saved_search_hits = models.BooleanField(default=True)