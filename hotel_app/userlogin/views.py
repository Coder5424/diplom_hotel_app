from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from .forms import UserRegisterForm, UserLoginForm
from .models import User


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'userlogin/register.html'
    success_url = reverse_lazy('hotel:room_list_view')

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(
            email=data['email'],
            password=data['password'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            phone_number=data['phone_number']
        )
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponse('No')


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'userlogin/login.html'
    success_url = reverse_lazy('hotel:room_list_view')

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data['email'],
                            password=data['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponse('NOT OKKKK')


def logout_user(request):
    success_url = reverse_lazy('hotel:room_list_view')
    logout(request)

    return HttpResponseRedirect(success_url)
