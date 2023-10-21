from django.db import models
from authentication.models import Users
from blog.models import BaseAbstractModel

class Category(BaseAbstractModel):
    name = models.CharField(max_length=64, unique=True)
    status = models.BooleanField(default=False)
    front = models.BooleanField(default=False)
    description = models.TextField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    files = models.ManyToManyField('file.File', through='file.FileCategory', through_fields=('category', 'file'))

    def __str__(self):
        return self.name

class SubCategory(BaseAbstractModel):
    name = models.CharField(max_length=64, unique=True)
    status = models.BooleanField(default=False)
    front = models.BooleanField(default=False)
    description = models.TextField()
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    files = models.ManyToManyField('file.File', through='file.FileSubCategory', through_fields=('subCategory', 'file'))

    def __str__(self):
        return self.name

class Post(BaseAbstractModel):
    title = models.CharField(max_length=150, unique=True)
    status = models.BooleanField(default=False)
    front = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)
    content = models.TextField(max_length=1500)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    files = models.ManyToManyField('file.File', through='file.FilePost', through_fields=('post', 'file'))

    def __str__(self):
        return self.title

class Comment(BaseAbstractModel):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)

    class Meta:
        unique_together = ('userId', 'content')
