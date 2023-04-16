from django import forms


class AvailabilityForm(forms.Form):
    room_types = (
        ('Standard', 'Standard'),
        ('Superior', 'Superior'),
        ('Deluxe', 'Deluxe'),
    )
    room_type = forms.TypedChoiceField(choices=room_types, initial=1, required=True)
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)
    phone_number = forms.CharField(max_length=20, required=True)
    check_in = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'}
        ),
        required=True
    )
    check_out = forms.DateField(
        widget=forms.DateTimeInput(
            attrs={'type': 'date'}
        ),
        required=True
    )
