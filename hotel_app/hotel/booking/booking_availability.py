import datetime
from ..models import Booking


def check_booking_avail(room, check_in, check_out):
    available_list = []

    booking_list = Booking.objects.filter(room=room)

    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            available_list.append(True)
        else:
            available_list.append(False)

    return all(available_list)
