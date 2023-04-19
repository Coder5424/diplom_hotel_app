from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView
from .forms import CheckInForm
from hotel.models import Booking
from userlogin.models import User
from .models import CheckIn


def booking_list_view(request):
    firstname = request.GET.get('search_booking')
    booking_list = []
    bookings = Booking.objects.filter(firstname__iregex=firstname)
    for booking in bookings:
        booking_url = reverse('adminworkenv:CheckInView', kwargs={
            'firstname': booking.firstname,
            'lastname': booking.lastname,
            'email': booking.email,
            'phone_number': booking.phone_number,
            'room': booking.room,
            'check_in': booking.check_in,
            'check_out': booking.check_out,
        })
        booking_list.append((booking, booking_url))

    context = {'booking_list': booking_list}

    return render(request, 'adminworkenv/booking_list.html', context)


class CheckInView(FormView):
    form_class = CheckInForm
    template_name = 'adminworkenv/checkin.html'

    def get(self, request, *args, **kwargs):
        firstname = self.kwargs.get('firstname', None)
        lastname = self.kwargs.get('lastname', None)
        email = self.kwargs.get('email', None)
        phone_number = self.kwargs.get('phone_number', None)
        room = self.kwargs.get('room', None)
        check_in = self.kwargs.get('check_in', None)
        check_out = self.kwargs.get('check_out', None)

        booking = Booking.objects.get(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
            room=room,
            check_in=check_in,
            check_out=check_out
        )

        if booking:
            context = {
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'phone_number': phone_number,
                'room': room,
                'check_in': check_in,
                'check_out': check_out
            }

            user = User.objects.get(
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
            )
            user_passport = user.passport
            if user_passport is not None:
                context['passport'] = user_passport
            return render(request, 'adminworkenv/checkin.html', context)
        else:
            return HttpResponse('NO')

    def form_valid(self, form):
        data = form.cleaned_data

        checkin = CheckIn.objects.create(
            firstname=data['firstname'],
            lastname=data['lastname'],
            email=data['email'],
            phone_number=data['phone_number'],
            passport=data['passport'],
            room=data['room'],
            check_in=data['check_in'],
            check_out=data['check_out'],
        )

        if checkin:
            checkin.save()

            user = User.objects.get(
                firstname=data['firstname'],
                lastname=data['lastname'],
                email=data['email'],
                phone_number=data['phone_number'],
            )

            if user:
                if user.passport is None:
                    user_passport = data['passport']
                    user.passport = user_passport
                    user.save()

            return HttpResponse(checkin)
        else:
            return HttpResponse('error')

