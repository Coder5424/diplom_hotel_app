import datetime
from django.db import models
from hotel.models import Room


def get_date():
    return datetime.date.today()


class CheckIn(models.Model):
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    passport = models.CharField(max_length=10)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return f'{self.room} - {self.email} '

