import datetime
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from hotel_app.celery import app
from .models import CheckIn


@app.task(ignore_result=False)
def change_checkin_time():
    now = datetime.datetime.now()

    if now.time() >= datetime.time(hour=13, minute=0):
        try:
            checkin = CheckIn.objects.get(
                room=5,
                check_in__contains=datetime.date.today(),
            )

            if checkin.check_in.time() == datetime.time(0, 0, 0):
                checkin.check_in = now
                checkin.save()
                return 'Change checkin time successfully'
            else:
                return 'No change checkin time'

        except ObjectDoesNotExist:
            return 'Dont get room'
    else:
        return 'Not a time (checkin)'


@app.task(ignore_result=False)
def change_checkout_time():
    now = datetime.datetime.now()

    if (now.time() <= datetime.time(hour=17, minute=30)) and (now.time() >= datetime.time(hour=16, minute=0)):
        try:
            checkin = CheckIn.objects.get(
                room=1,
                check_out__contains=datetime.date.today(),
            )

            if checkin.check_out.time() == datetime.time(0, 0, 0):
                checkin.check_out = now
                checkin.save()
                return 'Change checkout time successfully'
            else:
                return 'No change checkout time'

        except ObjectDoesNotExist:
            return 'Dont get room'
    else:
        return 'Not a time (checkout)'


@app.task(ignore_result=False)
def test():
    now = datetime.datetime.now()

    checkin = CheckIn.objects.filter(
        created_at__contains=datetime.date.today() - datetime.timedelta(days=91),
    ).delete()

    if checkin[0] == 0:
        return 'NO DELETE'
    else:
        return 'DELETE OK'







