from django.db import models
from authentication.models import Users
from meta.models import ModelMeta
from blog.models import BaseAbstractModel

# Create your models here.
class UsersProfile(ModelMeta, BaseAbstractModel):
    GENDERSET = (('M', 'Male'),
                 ('F', 'Female'))
    firstName = models.CharField(max_length=64, null=True)
    lastName = models.CharField(max_length=64, null=True)
    image = models.FileField(upload_to="uploads/%Y/%m/%d/",  null=True)
    dateOfBirth = models.DateTimeField(null=True)
    gender = models.CharField(max_length=1, choices=GENDERSET, null=True)
    userId = models.OneToOneField(Users, on_delete=models.CASCADE, unique=True)
    details = models.TextField(max_length=500, null=True)
    zipcode = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    region = models.CharField(verbose_name="state",max_length=150, null=True)
    country = models.CharField(max_length=150, null=True)
    longitude = models.CharField(max_length=15, null=True)
    latitude = models.CharField(max_length=15, null=True)
    popularity = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
   
    _metadata = {
        'title': 'get_full_name',
        'description': 'details',
        'image': 'get_meta_image',
    }
    
    def get_meta_image(self):
        if self.image:
            return self.image.url
    
    def get_full_name(self):
        if self.firstName and self.lastName:
            return self.firstName +" "+ self.lastName


