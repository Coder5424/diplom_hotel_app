from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView
from .forms import UserRegisterForm, UserLoginForm
from .models import User


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'userlogin/register.html'

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(
            email=data['email'],
            password=data['password'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            phone_number=data['phone_number']
        )
        login(self.request, user)
        if user is not None:
            return HttpResponse('OK')

        return HttpResponse('?')


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'userlogin/login.html'

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data['email'],
                            password=data['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponse('OKKKK')

        else:
            return HttpResponse('NOT OKKKK')


def logout_user(request):
    logout(request)
    return HttpResponse('logout')
