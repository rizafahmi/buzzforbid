from django.db import models
from django.contrib.auth.models import User


class Manager(models.Model):
    user = models.OneToOneField(User)

    # Additional fields
    name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.name


class Supervisor(models.Model):
    user = models.OneToOneField(User)

    # Additional fields
    name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.name


class Receptionist(models.Model):
    user = models.OneToOneField(User)

    # Additional fields
    name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.name
