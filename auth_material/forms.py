from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User


class UserProfileInfoForm(forms.ModelForm):
    aws_access_key = forms.CharField(required=False)
    aws_auth_token = forms.CharField(required=False)

    class Meta:
        model = UserProfileInfo
        exclude = ('user', )
