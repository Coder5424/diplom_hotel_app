from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, FormView
from .models import Room, Booking
from .forms import AvailabilityForm
from .booking.availability import check_availability


# class RoomList(ListView):
#     model = Room
#
#
# class BookingList(ListView):
#     model = Booking


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

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
                user=self.request.user,
                room=available_room,
                check_in=check_in,
                check_out=check_out,
            )
            booking.save()

            return HttpResponse(booking)

        else:
            return HttpResponse('All of this type rooms are booked')
