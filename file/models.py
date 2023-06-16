from django.db import models
from authentication.models import Users
from blog.models import BaseAbstractModel
from post.models import *
from userprofile.models import UsersProfile

# Create your models here.
class File(BaseAbstractModel):
    FILETYPE = (('Image', 'Image'),
            ('Video', 'Video'),
            ('Audio', 'Audio'),
            ('Document', 'Document'),
            ('Others', 'Others'))
    name = models.CharField(max_length=100)
    source = models.FileField(upload_to="uploads/%Y/%m/%d/")
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=12, choices=FILETYPE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "<div><img src=" +  str(self.source) + "></div>"
    
    class Meta(BaseAbstractModel.Meta):
        abstract = False

    
class FilePost(BaseAbstractModel):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta(BaseAbstractModel.Meta):
        abstract = False
class FileCategory(BaseAbstractModel):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE) 
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta(BaseAbstractModel.Meta):
        abstract = False

class FileSubCategory(BaseAbstractModel):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE) 
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta(BaseAbstractModel.Meta):
        abstract = False
    
class FileProfile(BaseAbstractModel):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    profileId = models.ForeignKey(UsersProfile, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta(BaseAbstractModel.Meta):
        abstract = False
