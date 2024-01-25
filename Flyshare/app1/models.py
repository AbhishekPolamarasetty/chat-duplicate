from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone

import datetime
# Create your models here.

class PostModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    passenger_name = models.CharField(max_length=255)  # Changed field name to snake_case
    date_of_journey = models.DateField()
    gender = models.CharField(max_length=1)
    flight_number = models.CharField(max_length=20)  # Changed to CharField assuming it can contain non-numeric characters
    pnr_number = models.CharField(max_length=20)  # Changed to CharField assuming it can contain non-numeric characters
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    baggage_space = models.IntegerField()  # Changed field name to snake_case
    is_checked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    baggage_number = models.CharField(max_length=5, unique=True)


from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)



