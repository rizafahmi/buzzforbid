from django.db import models
from geographic_info.models import City, Region, Province
from user_level.models import Manager, Supervisor, Receptionist


class Facility(models.Model):
    facility = models.CharField(max_length=50)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.facility

    class Meta:
        verbose_name_plural = 'Facilities'


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
    country = models.CharField(max_length=35, default='Indonesia')
    rating = models.IntegerField(default=3)
    room_type = models.CharField(max_length=3, choices=ROOM_TYPE_CHOICE)
    facilities = models.ManyToManyField(Facility, related_name='hotel_facility')

    # Contact Info
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    fax_number = models.CharField(max_length=50, blank=True, null=True)
    cs_email = models.EmailField(max_length=75, blank=True, null=True, unique=True)
    manager = models.ForeignKey(Manager, related_name='manager_user', blank=True,
            null=True)
    supervisor = models.ForeignKey(Supervisor, related_name='supervisor_user', blank=True,
            null=True)
    receptionist = models.ForeignKey(Receptionist, related_name='receptionist_user', blank=True, null=True)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.name
