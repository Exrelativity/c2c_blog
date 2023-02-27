from django.forms import ModelForm
from .models import UsersProfile

class UsersProfileForm(ModelForm):
    
    class Meta:
        model = UsersProfile
        fields = ("firstName","lastName", "gender","userId","details")

class UsersProfileMutationForm(ModelForm):
    
    class Meta:
        model = UsersProfile
        fields = ("id","firstName","lastName", "gender","userId","details")
