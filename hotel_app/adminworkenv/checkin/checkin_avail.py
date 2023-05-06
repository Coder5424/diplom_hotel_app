from ..models import CheckIn


def check_checkin_avail(room, check_in, check_out):
    available_list = []

    checkin_list = CheckIn.objects.filter(room=room)

    for checkin in checkin_list:
        if checkin.check_in > check_out or checkin.check_out < check_in:
            available_list.append(True)
        else:
            available_list.append(False)

    return all(available_list)

