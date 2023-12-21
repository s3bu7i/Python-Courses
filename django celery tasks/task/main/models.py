from django.db import models
from django.utils import timezone

# Create your models here.

class Result(models.Model):
    num = models.IntegerField()
    tarix = models.DateTimeField(default = timezone.now,db_index=True)
    
    def __str__(self):
        return str(self.num)