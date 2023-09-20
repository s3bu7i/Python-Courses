from django.db import models

# Create your models here.


class Student(models.Model):
    ad = models.CharField(max_length=50)
    metn = models.TextField(max_length=700, null=True, blank=True)
    tarix = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.ad
    
    
    
    