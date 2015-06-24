from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    url = models.CharField(max_length=1024)
