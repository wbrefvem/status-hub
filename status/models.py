from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    ext = models.CharField(max_length=4)
    email = models.EmailField()


class Department(models.Model):
    name = models.CharField(max_length=256)
    contact = models.OneToOneField(Contact)


class Status(models.Model):
    department = models.ForeignKey(Department)
    date = models.DateTimeField()
    message = models.CharField(max_length=1024)
    state = models.CharField(max_length=256)
