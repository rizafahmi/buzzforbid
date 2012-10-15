from django.db import models
from city.models import City
from region.models import Region


class Hotel(models.Model):

    ROOM_TYPE_CHOICE = (
            ('st', 'Standard'),
            ('su', 'Superior'),
            ('de', 'Deluxe'),
            ('stu', 'Studio'),
        )

    # General Info
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    address1 = models.CharField(max_length=200, blank=False, null=False)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.ForeignKey(City, related_name='hotel_city')
    region = models.ForeignKey(Region, blank=True, null=True,
            related_name='hotel_region')
    province = models.ForeignKey(Province, blank=True, null=True,
            related_name='hotel_province')
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, default='Indonesia')
    rating = models.IntegerField(default=3)
    room_type = models.CharField(max_length=3, choices=ROOM_TYPE_CHOICE)
    facilities = models.ManyToMany(Facility, related_name='hotel_facility')

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.name
