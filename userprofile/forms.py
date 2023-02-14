from django.forms import ModelForm
from .models import Usersprofile

class UsersprofileForm(ModelForm):
    
    class Meta:
        model = Usersprofile
        fields = ("firstName","lastName", "gender","userId","details")

class UsersprofileMutationForm(ModelForm):
    
    class Meta:
        model = Usersprofile
        fields = ("id","firstName","lastName", "gender","userId","details")
