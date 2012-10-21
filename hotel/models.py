from django.db import models
from geographic_info.models import City, Region, Province
from user_level.models import Manager, Supervisor, Receptionist
from room_type.models import RoomType1, RoomType2, RoomType3, RoomType4


class Facility(models.Model):
    facility = models.CharField(max_length=50)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.facility

    class Meta:
        verbose_name_plural = 'Facilities'


class Hotel(models.Model):

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
    facilities = models.ManyToManyField(Facility, related_name='hotel_facility',
            blank=True, null=True)

    # Room Info
    room_type_1 = models.OneToOneField(RoomType1, related_name='hotel_room_type_1',
            blank=False, null=False)
    room_type_2 = models.OneToOneField(RoomType2, related_name='hotel_room_type_2',
            blank=True, null=True)
    room_type_3 = models.OneToOneField(RoomType3, related_name='hotel_room_type_3',
            blank=True, null=True)
    room_type_4 = models.OneToOneField(RoomType4, related_name='hotel_room_type_4',
            blank=True, null=True)

    # Contact Info
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    fax_number = models.CharField(max_length=50, blank=True, null=True)
    cs_email = models.EmailField(max_length=75, blank=True, null=True, unique=True)
    manager = models.OneToOneField(Manager, related_name='manager_user', blank=True,
            null=True)
    supervisor = models.OneToOneField(Supervisor, related_name='supervisor_user', blank=True,
             null=True)
    receptionist = models.OneToOneField(Receptionist,
            related_name='receptionist_user', blank=False, null=False)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.name
