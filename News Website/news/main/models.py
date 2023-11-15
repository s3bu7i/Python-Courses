from django.db import models

# Create your models here.


class News_data(models.Model):
    
    
    title = models.CharField(max_length=200,null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    img = models.CharField(max_length=250,null=True,blank=True)
    date = models.CharField(max_length=50,null=True,blank=True)
    weather = models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.category
    
class Test(models.Model):
    category_id = models.ManyToManyField(News_data)
    
   
