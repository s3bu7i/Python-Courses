from django.db import models

# Create your models here.

class Test(models.Model):
    ad = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    basliq = models.CharField(max_length=500)
    metn = models.TextField(max_length=500)
    img = models.FileField(upload_to='images')
    date = models.DateField(null=True)
   
    def __str__(self):
       return self.category
   
   

   
class Comment(models.Model):
    message = models.CharField(max_length=255)
    email = models.EmailField(max_length=70)
    name = models.CharField(max_length=50)
    comment_id = models.IntegerField()
    date = models.DateField(auto_now=True)
    
