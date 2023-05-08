import datetime
from .celery import app
from adminworkenv.models import CheckIn


@app.task(ignore_result=False)
def change_checkin_time():
    now = datetime.datetime.now()

    checkin = CheckIn.objects.get(firstname='sss')

    if checkin.check_in.time() == datetime.time(0, 0, 0):
        checkin.check_in = now
        checkin.save()

