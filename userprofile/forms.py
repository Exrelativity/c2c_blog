from django import forms
from .models import UsersProfile

class UsersProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    COUNTRY_CHOICES = (
        ('AF', 'Afghanistan'),
        ('AX', 'Aland Islands'),
        # Add more country choices here
    )

    class Meta:
        model = UsersProfile
        fields = [
            'firstName',
            'lastName',
            'dateOfBirth',
            'gender',
            'details',
            'zipcode',
            'address',
            'city',
            'region',
            'longitude',
            'latitude',
            'popularity',
            'image'
        ]
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'}),
            'details': forms.Textarea(attrs={'rows': 10, 'cols': 100, 'placeholder': 'Here can be your description, Put relevant information, like jobs and what you want others to know about you'}),
            'popularity': forms.HiddenInput()
        }

    # Additional field for country choices
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class UsersProfileMutationForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    COUNTRY_CHOICES = (
        ('AF', 'Afghanistan'),
        ('AX', 'Aland Islands'),
        ('AL', 'Albania'),
        ('DZ', 'Algeria'),
        # Add more country choices here
        ('ZW', 'Zimbabwe')
    )

    class Meta:
        model = UsersProfile
        fields = [
            'firstName',
            'lastName',
            'gender',
            'details',
            'zipcode',
            'address',
            'city',
            'region',
            'longitude',
            'latitude',
            'popularity',
            'image'
        ]

    widgets = {
        'details': forms.Textarea(attrs={'rows': 10, 'cols': 100, 'placeholder': 'Here can be your description, Put relevant information, like jobs and what you want others to know about you'}),
        'popularity': forms.HiddenInput()
    }

    # Additional field for country choices
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

