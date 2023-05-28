from django import forms


class AvailabilityForm(forms.Form):
    room_types = (
        ('Standard', 'Стандарт'),
        ('Superior', 'Стандарт+'),
        ('Deluxe', 'Люкс'),
        ('Family', 'Семейный'),
    )
    room_type = forms.TypedChoiceField(
        choices=room_types, initial=1, required=True,
        widget=forms.Select(attrs={'class': 'booking-input__input'})
    )
    firstname = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(attrs={
            'class': 'booking-input__input', 'placeholder': 'Иванов'
        })
    )
    lastname = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(attrs={
            'class': 'booking-input__input', 'placeholder': 'Иван'
        })
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'booking-input__input', 'placeholder': 'example@email.com'
        })
    )
    phone_number = forms.CharField(
        max_length=20, required=True,
        widget=forms.TextInput(attrs={
            'class': 'booking-input__input', 'placeholder': '88005553535'
        })
    )
    check_in = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'booking-input__input'}
        ),
        required=True
    )
    check_out = forms.DateField(
        widget=forms.DateTimeInput(
            attrs={'type': 'date', 'class': 'booking-input__input'}
        ),
        required=True
    )
