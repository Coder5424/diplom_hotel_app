import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.user} has booked in {self.room} from {self.check_in} to {self.check_out}'



