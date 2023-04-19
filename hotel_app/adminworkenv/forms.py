from django import forms
from .models import CheckIn


class CheckInForm(forms.ModelForm):
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

    class Meta:
        model = CheckIn
        fields = '__all__'
        required_fields = fields

