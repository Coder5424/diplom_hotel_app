import datetime
from hotel_app.celery import app
from adminworkenv.models import CheckIn


@app.task(ignore_result=False)
def delete_data():
    now = datetime.datetime.now()

    checkin = CheckIn.objects.filter(
        created_at__contains=datetime.date.today() - datetime.timedelta(days=91),
    ).delete()

    if checkin[0] == 0:
        return 'NO DELETE'
    else:
        return 'DELETE SUCCESSFUL'







