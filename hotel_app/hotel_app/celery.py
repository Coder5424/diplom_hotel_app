import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_app.settings")

app = Celery("hotel_app", include=['adminworkenv.tasks'])
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'change_checkin_time': {
        'task': 'adminworkenv.tasks.change_checkin_time',
        'schedule': crontab(minute='*/1'),
    },
    'change_checkout_time': {
        'task': 'adminworkenv.tasks.change_checkout_time',
        'schedule': crontab(minute='*/1'),
    },
    'test': {
        'task': 'adminworkenv.tasks.test',
        'schedule': crontab(minute='*/1'),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
