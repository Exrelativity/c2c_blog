from django.db import models
from authentication.models import Users

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    status = models.BooleanField()
    front = models.BooleanField()
    image = models.FileField(upload_to="static/uploads/", max_length=150)
    description = models.TextField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    subCategory = models.ManyToManyField("post.SubCategory", related_name="category_sub_category")
    posts = models.ManyToManyField("post.Post", related_name="category_posts")
    
class SubCategory(models.Model):
    name = models.CharField(max_length=64)
    status = models.BooleanField()
    front = models.BooleanField()
    image = models.FileField(upload_to="static/uploads/", max_length=150)
    description = models.TextField()
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    posts = models.ManyToManyField("post.Post", related_name="sub_category_posts")
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField()
    front = models.BooleanField()
    slider = models.BooleanField()
    image = models.FileField(upload_to="static/uploads/", max_length=150)
    content = models.TextField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

