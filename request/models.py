from django.db import models
from hotel.models import Hotel
from django.contrib.auth.models import User


class HotelRequest(models.Model):
    hotel = models.ForeignKey(Hotel, blank=False, null=False,
            related_name='request_hotel')
    date_request = models.DateField(auto_now=False)
    price = models.IntegerField(blank=False, null=False)
    counter_price = models.IntegerField(blank=True, null=True)
    number_of_rooms = models.IntegerField(default=1)
    request_user = models.ForeignKey(User)
    accept = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    # Metadata
    datetime_added = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeFields(auto_now=True)
