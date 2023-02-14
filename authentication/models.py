from django.db import models
from django.contrib.auth.models import AbstractUser as BaseUser

# Create your models here.

class User(BaseUser):
    phone = models.CharField(max_length=15, null=True)
    profile = models.OneToOneField("userprofile.Usersprofile", null=True, on_delete=models.SET_NULL)
   