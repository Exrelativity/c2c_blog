from django.db import models
from authentication.models import Users
from meta.models import ModelMeta
from blog.models import BaseAbstractModel

# Create your models here.
class UsersProfile(BaseAbstractModel, ModelMeta):
    GENDERSET = (('M', 'Male'),
                 ('F', 'Female'))
    firstName = models.CharField(max_length=64, null=True, blank=True)
    lastName = models.CharField(max_length=64, null=True, blank=True)
    image = models.CharField(max_length=150, null=True, blank=True)
    dateOfBirth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERSET, null=True, blank=True)
    userId = models.OneToOneField(Users, on_delete=models.CASCADE, unique=True)
    details = models.TextField(max_length=500, null=True, blank=True)
    zipcode = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    region = models.CharField(verbose_name="state",max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    longitude = models.CharField(max_length=15, null=True, blank=True)
    latitude = models.CharField(max_length=15, null=True, blank=True)
    popularity = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    media = models.ManyToManyField(to="file.File", through="file.FileProfile",through_fields=("profileId","fileId"))
   
    _metadata = {
        'title': 'get_full_name',
        'description': 'details',
        'image': 'get_meta_images',
    }
    
    def get_meta_images(self):
        if self.media:
            return [x.source for x in self.media]
    
    def get_full_name(self):
        if self.firstName and self.lastName:
            return self.firstName +" "+ self.lastName

    class Meta(BaseAbstractModel.Meta):
        abstract = False
  

