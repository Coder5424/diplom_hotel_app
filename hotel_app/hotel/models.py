import uuid
from django.conf import settings
from django.db import models


class Room(models.Model):
    room_types = (
        ('Standard', 'Standard'),
        ('Superior', 'Superior'),
        ('Deluxe', 'Deluxe'),
    )
    type = models.CharField(max_length=8, choices=room_types)
    number = models.IntegerField()
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'room number {self.number}. {self.type} with {self.beds} beds for {self.capacity} people.'


class Booking(models.Model):
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.firstname} {self.lastname} has booked in {self.room} from {self.check_in} to {self.check_out}'



