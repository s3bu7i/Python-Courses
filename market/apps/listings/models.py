from django.db import models
from django.conf import settings
from slugify import slugify
from apps.catalog.models import Category


class Listing(models.Model):
class Condition(models.TextChoices):
NEW = 'NEW', 'New'
LIKE_NEW = 'LIKE_NEW', 'Like New'
GOOD = 'GOOD', 'Good'
FAIR = 'FAIR', 'Fair'
POOR = 'POOR', 'Poor'


class Status(models.TextChoices):
DRAFT = 'DRAFT'
PENDING = 'PENDING'
ACTIVE = 'ACTIVE'
REJECTED = 'REJECTED'
EXPIRED = 'EXPIRED'


id = models.BigAutoField(primary_key=True)
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')
category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='listings')
title = models.CharField(max_length=160)
slug = models.SlugField(unique=True)
description = models.TextField()
price_cents = models.IntegerField()
currency = models.CharField(max_length=8, default='AZN')
condition = models.CharField(max_length=16, choices=Condition.choices)
city = models.CharField(max_length=80)
status = models.CharField(max_length=16, choices=Status.choices, default=Status.PENDING)
views = models.IntegerField(default=0)
featured = models.BooleanField(default=False)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
expires_at = models.DateTimeField(null=True, blank=True)


def save(self, *args, **kwargs):
if not self.slug:
base = slugify(self.title)
self.slug = f"{base}-{str(abs(hash(self.title)))[-4:]}"
super().save(*args, **kwargs)


def __str__(self):
return self.title


class ListingImage(models.Model):
listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
url = models.URLField()
is_cover = models.BooleanField(default=False)
sort = models.IntegerField(default=0)


class Favorite(models.Model):
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
created_at = models.DateTimeField(auto_now_add=True)


class Meta:
unique_together = ('user','listing')