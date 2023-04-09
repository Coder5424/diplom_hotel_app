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
        return f'Room number {self.number}. {self.type} with {self.beds} beds for {self.capacity} people'
