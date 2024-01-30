from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    desc = models.TextField(blank=True)

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


    def __str__(self) -> str:
        return self.category_name
    
    
# Create your models here.
