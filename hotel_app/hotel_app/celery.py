import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_app.settings")

app = Celery("hotel_app", include=['hotel_app.tasks'])
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'change_time': {
        'task': 'hotel_app.tasks.change_checkin_time',
        'schedule': crontab(minute='*/1'),
    },

}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
