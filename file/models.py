from django.db import models
from authentication.models import Users
from post.models import Post, Category, SubCategory
from userprofile.models import UsersProfile
from blog.models import BaseAbstractModel
# This makes it an abstract model and won't create a table for it

class File(BaseAbstractModel):
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

    def __str__(self):
        return self.name

class BaseRelationModel(BaseAbstractModel):
    # Common fields for models with relations
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)

class FilePost(BaseRelationModel):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)

class FileCategory(BaseRelationModel):
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)

class FileSubCategory(BaseRelationModel):
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

class FileProfile(BaseRelationModel):
    profileId = models.ForeignKey(UsersProfile, on_delete=models.CASCADE)
