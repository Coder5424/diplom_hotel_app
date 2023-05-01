from django import forms
from django.contrib.auth import get_user_model


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()
    password.widget = forms.PasswordInput(attrs={
        'class': 'profile-input__input'
    })

    class Meta:
        model = get_user_model()
        fields = ('firstname', 'lastname', 'email', 'phone_number',)
        required_fields = fields
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'profile-input__input', 'placeholder': 'Иванов'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'profile-input__input', 'placeholder': 'Иван'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'profile-input__input', 'placeholder': '88005553535'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'profile-input__input', 'placeholder': 'example@email.com'
            }),
        }


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    email.widget = forms.EmailInput(attrs={
        'class': 'profile-input__input', 'placeholder': 'example@email.com'
    })

    password = forms.CharField()
    password.widget = forms.PasswordInput(attrs={
        'class': 'profile-input__input'
    })


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



