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


class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(required=False)
    password.widget = forms.PasswordInput(attrs={'class': 'profile-input__input'})

    class Meta:
        model = get_user_model()
        fields = ('firstname', 'lastname', 'email', 'phone_number')
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'profile-input__input'}),
            'lastname': forms.TextInput(attrs={'class': 'profile-input__input'}),
            'phone_number': forms.TextInput(attrs={'class': 'profile-input__input'}),
            'email': forms.EmailInput(attrs={'class': 'profile-input__input'}),
        }

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()



