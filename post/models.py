from django.db import models
from authentication.models import Users
from meta.models import ModelMeta

# Create your models here.
class Category(ModelMeta, models.Model):
    name = models.CharField(max_length=64)
    status = models.BooleanField()
    front = models.BooleanField()
    image = models.FileField(upload_to="static/uploads/", max_length=150)
    description = models.TextField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    _metadata = {
        'title': 'name',
        'description': 'content',
        'image': 'get_meta_image',
    }
    def get_meta_image(self):
        if self.image:
            return self.image.url

class SubCategory(ModelMeta, models.Model):
    name = models.CharField(max_length=64)
    status = models.BooleanField()
    front = models.BooleanField()
    image = models.FileField(upload_to="static/uploads/", max_length=150)
    description = models.TextField()
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    _metadata = {
        'title': 'name',
        'description': 'description',
        'image': 'get_meta_image',
    }
    def get_meta_image(self):
        if self.image:
            return self.image.url

class Post(ModelMeta, models.Model):
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

    _metadata = {
        'title': 'title',
        'description': 'description',
        'image': 'get_meta_image',
    }
    def get_meta_image(self):
        if self.image:
            return self.image.url
