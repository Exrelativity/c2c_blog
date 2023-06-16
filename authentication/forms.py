from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"Username",
                "class":"form-control"}
            ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Password",
                "class":"form-control"}
            ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placholder":"Username",
                "class":"form-control"}
            ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placholder":"Email",
                "class":"form-control"}
            ))
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placholder":"Phone",
                "class":"form-control"}
            ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placholder":"Password",
                "class":"form-control"}
            ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placholder":"Password check",
                "class":"form-control"}
            ))
    class Meta:
        model = Users
        fields = ("username", "email","phone", "password1", "password2")

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placholder":"Email",
                "class":"form-control"}
            ))
     
class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placholder":"Password",
                "class":"form-control"}
            ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placholder":"Password check",
                "class":"form-control"}
            ))


class UserForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = "__all__"

class UsersMutationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
