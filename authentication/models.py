from django.db import models
from django.contrib.auth.models import AbstractUser as BaseUser

# Create your models here.
class Users(BaseUser):
    phone = models.CharField(max_length=15, null=True)
    profile = models.ManyToManyField("userprofile.UsersProfile")
    posts = models.ManyToManyField("post.Post", related_name="users_posts")


class PasswordReset(models.Model):
    userId = models.ForeignKey("authentication.Users", null=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=15, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_created=True)
    

    class Meta:
        verbose_name = "PasswordReset"
        verbose_name_plural = "PasswordResets"


class VerifiedEmail(models.Model):
    email = models.CharField(max_length=150, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_created=True)
    
    class Meta:
        verbose_name = "VerifiedEmail"
        verbose_name_plural = "VerifiedEmails"

