from django.forms import ModelForm
from .models import UsersProfile

class UsersProfileForm(ModelForm):
    
    class Meta:
        model = UsersProfile
        fields = "__all__"

class UsersProfileMutationForm(ModelForm):
    
    class Meta:
        model = UsersProfile
        fields = "__all__"
