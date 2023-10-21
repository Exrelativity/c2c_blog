from django.db import models
from authentication.models import Users
from post.models import Post, Category, SubCategory
from userprofile.models import UsersProfile

class File(models.Model):
    FILETYPE_CHOICES = (
        ('Image', 'Image'),
        ('Video', 'Video'),
        ('Audio', 'Audio'),
        ('Document', 'Document'),
        ('Others', 'Others')
    )

    name = models.CharField(max_length=100)
    source = models.FileField(upload_to="uploads/%Y/%m/%d/")
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=12, choices=FILETYPE_CHOICES)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FilePost(models.Model):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class FileCategory(models.Model):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class FileSubCategory(models.Model):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class FileProfile(models.Model):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    profileId = models.ForeignKey(UsersProfile, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
