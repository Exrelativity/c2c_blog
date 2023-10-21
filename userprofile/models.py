from django.db import models
from authentication.models import Users
from blog.models import BaseAbstractModel
from django.contrib.gis.db import models as gis_models

class UsersProfile(BaseAbstractModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, unique=True)
    details = models.TextField(max_length=500, null=True, blank=True)
    zipcode = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, verbose_name="state", null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    popularity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Geographic coordinates (latitude and longitude)
    location = gis_models.PointField(null=True, blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta(BaseAbstractModel.Meta):
        abstract = False
