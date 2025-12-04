from django.contrib.auth.models import User
from django.db import models


# a location holds the information for all events that happen at that location
class Location(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# an event holds all the information for that event
# an event can only belong to one location
class Event(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    conditions = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# a Stage holds all the results for that stage
# a stage belongs only to one event
class Stage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    length = models.FloatField()



# A result holds the time for a race/stage
# A result belongs to only one stage
class Result(models.Model):
    time = models.TimeField()
    driver = models.CharField(max_length=100)
    codriver = models.CharField(max_length=100)
    car = models.CharField(max_length=100)
    carclass = models.CharField(max_length=100)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
