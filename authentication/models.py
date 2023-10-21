from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, unique=True)

class PasswordReset(models.Model):
    user = models.OneToOneField(Users, on_delete=models.SET_NULL, null=True, unique=True)
    token = models.CharField(max_length=15, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Password Reset"
        verbose_name_plural = "Password Resets"

class VerifiedEmail(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Verified Email"
        verbose_name_plural = "Verified Emails"

class UserMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_media/')
    # Add other fields for media files
