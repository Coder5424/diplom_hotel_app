import uuid
from django.conf import settings
from django.db import models


class Room(models.Model):
    room_types = (
        ('Standard', 'Standard'),
        ('Superior', 'Superior'),
        ('Deluxe', 'Deluxe'),
    )
    type = models.CharField(max_length=15, choices=room_types)
    img = models.ImageField(upload_to='hotel/images/')
    img_for_detail1 = models.ImageField(upload_to='hotel/images/')
    img_for_detail2 = models.ImageField(upload_to='hotel/images/')
    img_for_detail3 = models.ImageField(upload_to='hotel/images/')
    number = models.IntegerField(primary_key=True, unique=True)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number} : {self.type}'


class Booking(models.Model):
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.firstname} {self.lastname} - {self.room} - {self.check_in} : {self.check_out}'



