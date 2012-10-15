from django.db import models
from django.contrib.auth.models import User


class Manager(models.Model):
    user = models.OneToOneField(User)

    # Additional fields
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False, unique=True)


class Supervisor(models.Model):
    user = models.OneToOneField(User)

    # Additional fields
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False, unique=True)


class Receptionist(models.Model):
    user = models.OneToOneField(User)

    # Additional fields
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False, unique=True)
