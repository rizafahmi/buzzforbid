from django.db import models
from city.models import City
from region.models import Region
from province.models import Province
from django.contrib.auth.models import User


class Facility(models.Model):
    # FACILITY_CHOICE = (
    #         ('WiFi', 'WiFi'),
    #         ('Parking', 'Parking'),
    #         ('Airport Shuttle', 'Airport Shuttle'),
    # )

    facility = models.CharField(max_length=50)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.facility


class HotelManagerUser(models.Model):
    user = models.OneToOneField(User)

    # Additional fields
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False, unique=True)


class HotelSupervisorUser(models.Model):
    user = models.OneToOneField(User)

    # Additional fields
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False, unique=True)


class HotelUser(models.Model):
    user = models.OneToOneField(User)

    # Additional fields
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False, unique=True)


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
    cs_email = models.EmailField(max_length=75, blank=False, null=False, unique=True)
    manager = models.ForeignKey(HotelManagerUser, related_name='manager_user', blank=True,
            null=True)
    supervisor = models.ForeignKey(HotelSupervisorUser, related_name='supervisor_user', blank=True,
            null=True)
    user = models.ForeignKey(HotelUser, related_name='user_user', blank=True, null=True)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.name
