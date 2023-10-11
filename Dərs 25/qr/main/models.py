from django.db import models
from django.contrib.auth.models import AbstractUser, User

class CustomUser(AbstractUser):
    img = models.FileField(upload_to = 'images/',null = True,blank = True)
    text = models.CharField(max_length=50)
    
class CostumUser(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False)
    
    
    