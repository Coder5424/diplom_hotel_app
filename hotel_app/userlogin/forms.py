from django import forms
from django.contrib.auth import get_user_model


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('firstname', 'lastname', 'email', 'phone_number',)
        required_fields = fields


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

