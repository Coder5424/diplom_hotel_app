from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from .models import User


@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    context = {'user': user}

    return render(request, 'userlogin/profile.html', context)


@login_required
def logout_user(request):
    success_url = reverse_lazy('hotel:room_list_view')
    logout(request)

    return HttpResponseRedirect(success_url)


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('userlogin:profile'))
    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {'form': user_form}

    return render(request, 'userlogin/update_profile.html', context)


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


class UpdateView(FormView):
    template_name = 'userlogin/update_profile.html'
    success_url = reverse_lazy('userlogin:profile')

    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST, instance=request.user)

    def form_valid(self, form):
        data = form.cleaned_data

        user = User.objects.filter(id=self.request.user.id).update(
            firstname=data['firstname'],
            lastname=data['lastname'],
            email=data['email'],
            phone_number=data['phone_number'],
        )
        user.save()

        return HttpResponseRedirect(self.success_url)
