from django.db import models

from geographic_info.models import City
from django.contrib.auth.models import User


class Request(models.Model):

    STATUS_CHOICES = (('unread', 'Unread'),
            ('accepted', 'Accepted'),
            ('expired', 'Expired'),
            ('rejected', 'Rejected'),
            )

    destinations = models.ManyToManyField(City, related_name='destination',
            blank=False, null=False)
    date = models.DateField()
    duration = models.IntegerField(default=2)
    adult = models.IntegerField(default=1)
    child = models.IntegerField(default=0)
    airplane = models.BooleanField(default=True)
    accomodation = models.BooleanField(default=False)
    special_request = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=25, blank=True, null=True,
            choices=STATUS_CHOICES)

    # Metadata
    created = models.DateTimeField(auto_now=True, auto_now_add=True)
    user = models.ForeignKey(User, related_name='request_user')
