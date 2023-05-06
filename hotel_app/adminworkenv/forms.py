from django import forms
from .models import CheckIn


class CheckInForm(forms.ModelForm):
    check_in = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'date'}
        ),
        required=True
    )
    check_out = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'date'}
        ),
        required=True
    )

    class Meta:
        model = CheckIn
        fields = '__all__'
        required_fields = fields


class GetDataForm(forms.Form):
    check_in_down = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'date'}
        ),
        required=True
    )
    check_in_up = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'date'}
        ),
        required=True
    )

