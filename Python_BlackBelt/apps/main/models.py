from __future__ import unicode_literals
from django.db import models
from ..login_register.models import Users, UsersManager

class TripsManager(models.Manager):
    def validate(self, present, destination, description, travel_date_from, travel_date_to):
        error_messages = []

        destination_l = len(destination)
        description_l = len(description)

        if destination_l < 1 or description_l < 1:
            error_messages.append('All fields are required and must not be blank')
        if not str.isalpha(str(destination)):
            error_messages.append('Invalid Destination')
        if travel_date_from < present:
            error_messages.append("You can't travel to the past (just yet)")
        if travel_date_from > travel_date_to:
            error_messages.append("You can't stay negative amount of days, silly!")

        return error_messages

class Trips(models.Model):
    destination = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()
    user = models.ForeignKey(Users, related_name="trips")
    activeUserPlanned = models.BooleanField(default=False)
    objects = TripsManager()

class Joins(models.Model):
    trip = models.ForeignKey(Trips, related_name="trips_joined")
    joining_user = models.ForeignKey(Users)
