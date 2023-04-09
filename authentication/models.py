from django.db import models
from django.contrib.auth.models import AbstractUser as BaseUser
from blog.models import BaseAbstractModel

# Create your models here.
class Users(BaseUser, BaseAbstractModel):
    phone = models.CharField(max_length=15, null=True, unique=True)
    
    def get_full_name(self):
        if self.firstName and self.lastName:
            return self.firstName +" "+ self.lastName


class PasswordReset(BaseAbstractModel):
    userId = models.OneToOneField("authentication.Users", null=True, on_delete=models.SET_NULL, unique=True)
    token = models.CharField(max_length=15, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_created=True)
    

    class Meta:
        verbose_name = "PasswordReset"
        verbose_name_plural = "PasswordResets"


class VerifiedEmail(BaseAbstractModel):
    email = models.CharField(max_length=150, null=True, unique=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_created=True)
    
    class Meta:
        verbose_name = "VerifiedEmail"
        verbose_name_plural = "VerifiedEmails"

