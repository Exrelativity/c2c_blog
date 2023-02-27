from django.forms import ModelForm
from .models import Users

class UsersMutationForm(ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

