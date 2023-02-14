from django.db import models
from authentication.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class SubCategory(models.Model):
    name = models.CharField(max_length=64)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to="static/uploads/", max_length=150)
    content = models.TextField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
