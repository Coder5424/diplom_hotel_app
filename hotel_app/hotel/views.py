from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views.generic import ListView, FormView, View
from .models import Room, Booking
from .forms import AvailabilityForm
from .booking.availability import check_availability
from datetime import time, tzinfo
import pytz


def room_list_view(request):
    room = Room.objects.first()
    room_types = dict(room.room_types)
    room_list = []
    for room_type in room_types:
        room_url = reverse('hotel:RoomDetailView', kwargs={'type': room_type})
        room_list.append((room_type, room_url))

    context = {'room_list': room_list}

    return render(request, 'hotel/room_list.html', context)
#
#
# class BookingList(ListView):
#     model = Booking


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        room_type = self.kwargs.get('type', None)
        room = Room.objects.filter(type=room_type)
        if room:
            context = {'room_type': room_type}
            return render(request, 'hotel/room_detail_view.html', context)
        else:
            return HttpResponse('NO')


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'hotel/availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(type=data['room_type'])

        check_in = data['check_in']
        check_out = data['check_out']

        available_check = False
        available_room = None

        for room in room_list:
            if check_availability(room, check_in, check_out):
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

            return HttpResponse(booking)
        else:
            return HttpResponse('All of this type rooms are booked')
