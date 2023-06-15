import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_app.settings")

app = Celery("hotel_app", include=['hotel.tasks'])
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'delete': {
        'task': 'hotel.tasks.delete_data',
        'schedule': crontab(hour='*/24'),
    },
}

