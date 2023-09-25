from django.db import models

# Create your models here.


class Student(models.Model):
    
    ad = models.CharField(max_length=50,null=True,blank=True)
    metn = models.TextField(max_length=700,null=True,blank=True)
    tarix = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.ad
    
class Telephone(models.Model):
    model = models.CharField(max_length=50,null=True,blank=True)
    dioqqanal = models.TextField(max_length=700,null=True,blank=True)
    prosessor = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.ad
    