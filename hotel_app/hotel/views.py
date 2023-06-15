import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, FormView, View
from .models import Room, Booking
from .forms import AvailabilityForm
from .booking.booking_availability import check_booking_avail
from datetime import date
from adminworkenv.models import CheckIn


def room_list_view(request):
    room = Room.objects.first()
    room_types = dict(room.room_types)
    room_list = []
    for room_type in room_types:
        room = Room.objects.filter(type=room_type).first()
        room_url = reverse('hotel:RoomDetailView', kwargs={'type': room_type})
        room_list.append((room, room_type, room_url))

    context = {'room_list': room_list}

    return render(request, 'hotel/room_list.html', context)


def error_booking(request):
    return render(request, 'hotel/error_booking.html')


def error_date(request):
    return render(request, 'hotel/error_date.html')


@login_required
def booking_list_view(request):
    booking_list = Booking.objects.filter(
        email=request.user.email,
        phone_number=request.user.phone_number,
        check_in__gte=date.today()
    ).order_by('check_in')

    context = {'booking_list': booking_list}

    return render(request, 'hotel/booking_list.html', context)


@csrf_exempt
def data_handler(request):
    if request.method == 'POST':
        request.method = 'GET'
        sensor1 = request.GET.get('sensor1')

        now = datetime.datetime.now()

        if now.time() >= datetime.time(hour=13, minute=0):
            checkin = CheckIn.objects.get(
                room=sensor1,
                check_in__contains=datetime.date.today(),
            )

            if checkin.check_in.time() == datetime.time(0, 0, 0):
                checkin.check_in = now
                checkin.save()

        if now.time() <= datetime.time(hour=12, minute=0):
            checkout = CheckIn.objects.get(
                room=sensor1,
                check_out__contains=datetime.date.today(),
            )

            checkout.check_out = now
            checkout.save()

        return HttpResponse(200)


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        room_type = self.kwargs.get('type', None)
        room = Room.objects.filter(type=room_type).first()

        context = {'room_type': room_type, 'room': room}
        return render(request, 'hotel/room_detail_view.html', context)


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'hotel/availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(type=data['room_type'])

        check_in = data['check_in']
        check_out = data['check_out']

        if (check_in <= check_out) and (check_in >= date.today()):
            available_check = False
            available_room = None

            for room in room_list:
                if check_booking_avail(room, check_in, check_out):
                    available_check = True
                    available_room = room
                    break

            if available_check:
                booking = Booking.objects.create(
                    firstname=data['firstname'],
                    lastname=data['lastname'],
                    email=data['email'],
                    phone_number=data['phone_number'],
                    room=available_room,
                    check_in=check_in,
                    check_out=check_out,
                )
                booking.save()

                return HttpResponseRedirect(reverse('hotel:booking_list_view'))
            else:
                return HttpResponseRedirect(reverse('hotel:error_booking'))
        else:
            return HttpResponseRedirect(reverse('hotel:error_date'))
