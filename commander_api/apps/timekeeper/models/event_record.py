from django.db import models


class EventTypes(models.TextChoices):
    IN = "IN", "Check-In"
    OUT = "OUT", "Check-Out"


class EventRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.CharField(
        max_length=4,
        choices=EventTypes.choices,
    )
    datetime = models.DateTimeField()
