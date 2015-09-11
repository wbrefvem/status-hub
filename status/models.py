from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField()


class Status(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    destinations = models.ManyToManyField(Destination)


class DestinationRecord(models.Model):
    destination = models.ForeignKey(Destination)
    destination = models.ForeignKey(Status)
    record_id = models.IntegerField()
