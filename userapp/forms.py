from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from userapp.models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'display_name', 'homepage', 'age']

    


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)