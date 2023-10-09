from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    img = models.FileField(upload_to = 'images/',null = True,blank = True)
    text = models.CharField(max_length=50)