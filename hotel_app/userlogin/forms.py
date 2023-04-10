from django import forms


class UserRegisterForm(forms.Form):
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)