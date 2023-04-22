from django.db import models
from authentication.models import Users
from meta.models import ModelMeta
from blog.models import BaseAbstractModel

# Create your models here.
class Category(BaseAbstractModel, ModelMeta):
    name = models.CharField(max_length=64, unique=True)
    status = models.BooleanField(default=False)
    front = models.BooleanField(default=False)
    description = models.TextField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(to="file.File",through="file.FileCategory",through_fields=("categoryId","fileId"))

    _metadata = {
        "title": "name",
        "description": "content",
        "image": "get_meta_images",
    }

    def get_meta_images(self):
        if self.file:
            return [x.source for x in self.files]
    
    def __str__(self):
        return self.name
    
    class Meta(BaseAbstractModel.Meta):
        abstract = False
    
    
   


class SubCategory(BaseAbstractModel, ModelMeta):
    name = models.CharField(max_length=64, unique=True)
    status = models.BooleanField(default=False)
    front = models.BooleanField(default=False)
    description = models.TextField()
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(to="file.File",through="file.FileSubCategory",through_fields=("subCategoryId","fileId"))

    _metadata = {
        "title": "name",
        "description": "description",
        "images": "get_meta_images",
    }

    def get_meta_images(self):
        if self.file:
            return [x.source for x in self.files]
        
    def __str__(self):
        return self.name
    
    class Meta(BaseAbstractModel.Meta):
        abstract = False
    


class Post(ModelMeta, BaseAbstractModel):
    title = models.CharField(max_length=150, unique=True)
    status = models.BooleanField(default=False)
    front = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)
    content = models.TextField(max_length=1500)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(to="file.File",through="file.FilePost",through_fields=("postId", "fileId"))

    _metadata = {
        "title": "title",
        "description": "description",
        "images": "get_meta_images",
    }

    def get_meta_images(self):
        if self.file:
            return [x.source for x in self.files]
        
    def __str__(self):
        return self.title
    
    class Meta(BaseAbstractModel.Meta):
        abstract = False
    
  

class Comment(BaseAbstractModel):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    #need to add a unique index for userid and content
    # blank=True,
        # null=True,
        
    class Meta(BaseAbstractModel.Meta):
        abstract = False