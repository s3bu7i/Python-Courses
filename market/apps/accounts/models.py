from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
# username remains; email unique for convenience
email = models.EmailField(unique=True)


def __str__(self):
return self.email or self.username