from django.db import models

# Create your models here.

class Crud(models.Model):
    name= models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email= models.EmailField()
    passw= models.CharField(max_length=20)
    
