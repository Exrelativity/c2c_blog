from django.forms import ModelForm
from .models import UsersProfile

class UsersProfileForm(ModelForm):
    
    class Meta:
        model = UsersProfile
        fields = ("firstName","lastName", "image", "dateOfBirth", "gender","userId","details","zipcode","address","city","region","country","longitude","latitude","popularity")

class UsersProfileMutationForm(ModelForm):
    
    class Meta:
        model = UsersProfile
        fields = ("id","firstName","lastName", "image", "dateOfBirth", "gender","userId","details","zipcode","address","city","region","country","longitude","latitude","popularity")
