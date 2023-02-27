from django.db import models
from authentication.models import Users

# Create your models here.
class UsersProfile(models.Model):
    GENDERSET = (('M', 'Male'),
                 ('F', 'Female'))
    firstName = models.CharField(max_length=64, null=True)
    lastName = models.CharField(max_length=64, null=True)
    gender = models.CharField(max_length=1, choices=GENDERSET)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    details = models.TextField(max_length=500, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
   
    

