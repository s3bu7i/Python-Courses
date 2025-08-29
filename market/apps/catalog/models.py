from django.db import models
from slugify import slugify


class Category(models.Model):
id = models.BigAutoField(primary_key=True)
name = models.CharField(max_length=120)
slug = models.SlugField(unique=True)
parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
sort = models.IntegerField(default=0)


def save(self, *args, **kwargs):
if not self.slug:
self.slug = slugify(self.name)
super().save(*args, **kwargs)


def __str__(self):
return self.name