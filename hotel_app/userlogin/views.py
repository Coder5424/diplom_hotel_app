from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView
from .forms import UserRegisterForm
from .models import User


class RegisterForm(FormView):
    form_class = UserRegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create(
            firstname=data['firstname'],
            lastname=data['lastname'],
            email=data['email'],
            phone_number=data['phone_number'],
            password=data['password']
        )
        user.save()

        return HttpResponse('OK')
