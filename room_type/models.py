from django.db import models


class RoomFacility(models.Model):
    facility = models.CharField(max_length=50)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.facility

    class Meta:
        verbose_name_plural = 'Room Facilities'

BED_SIZE_CHOICES = (('single', 'Single'), ('double', 'Double'))


class RoomType1(models.Model):
    """Model for Hotel Room Type"""
    room_type_name = models.CharField(max_length=50, blank=False, null=False)
    allotment = models.IntegerField(blank=True, null=True)
    room_size = models.CharField(max_length=25, blank=True, null=True)
    bed_size = models.CharField(max_length=25, blank=True, null=True, choices=BED_SIZE_CHOICES)
    number_of_bed = models.IntegerField(blank=False, null=False, default=1)
    room_facilities = models.ManyToManyField(RoomFacility,
            related_name='room1_facility', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)

    # Price Info
    default_price = models.IntegerField(blank=False, null=False)

    high_season_from = models.DateField(blank=True, null=True)
    high_season_to = models.DateField(blank=True, null=True)
    high_season_price = models.IntegerField(blank=True, null=True)

    low_season_from = models.DateField(blank=True, null=True)
    low_season_to = models.DateField(blank=True, null=True)
    low_season_price = models.IntegerField(blank=True, null=True)

    special_occation_from = models.DateField(blank=True, null=True)
    special_occation_to = models.DateField(blank=True, null=True)
    special_occation_price = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        from hotel.models import Hotel
        hotel = Hotel.objects.filter(room_type_1__room_type_name=self.room_type_name)
        return self.room_type_name + " - " + hotel[0].name

    class Meta:
        verbose_name_plural = 'Room Type 1'


class RoomType2(models.Model):
    """Model for Hotel Room Type2"""
    room_type_name = models.CharField(max_length=50, blank=False, null=False)
    allotment = models.IntegerField(blank=True, null=True)
    room_size = models.CharField(max_length=25, blank=True, null=True)
    bed_size = models.CharField(max_length=25, blank=True, null=True)
    number_of_bed = models.IntegerField(blank=False, null=False, default=1)
    room_facilities = models.ManyToManyField(RoomFacility,
            related_name='room2_facility', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)

    # Price Info
    default_price = models.IntegerField(blank=False, null=False)

    high_season_from = models.DateField(blank=True, null=True)
    high_season_to = models.DateField(blank=True, null=True)
    high_season_price = models.IntegerField(blank=True, null=True)

    low_season_from = models.DateField(blank=True, null=True)
    low_season_to = models.DateField(blank=True, null=True)
    low_season_price = models.IntegerField(blank=True, null=True)

    special_occation_from = models.DateField(blank=True, null=True)
    special_occation_to = models.DateField(blank=True, null=True)
    special_occation_price = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.room_type_name

    class Meta:
        verbose_name_plural = 'Room Type 2'


class RoomType3(models.Model):
    """Model for Hotel Room Type 3"""
    room_type_name = models.CharField(max_length=50, blank=False, null=False)
    allotment = models.IntegerField(blank=True, null=True)
    room_size = models.CharField(max_length=25, blank=True, null=True)
    bed_size = models.CharField(max_length=25, blank=True, null=True)
    number_of_bed = models.IntegerField(blank=False, null=False, default=1)
    room_facilities = models.ManyToManyField(RoomFacility,
            related_name='room3_facility', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)

    # Price Info
    default_price = models.IntegerField(blank=False, null=False)

    high_season_from = models.DateField(blank=True, null=True)
    high_season_to = models.DateField(blank=True, null=True)
    high_season_price = models.IntegerField(blank=True, null=True)

    low_season_from = models.DateField(blank=True, null=True)
    low_season_to = models.DateField(blank=True, null=True)
    low_season_price = models.IntegerField(blank=True, null=True)

    special_occation_from = models.DateField(blank=True, null=True)
    special_occation_to = models.DateField(blank=True, null=True)
    special_occation_price = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.room_type_name

    class Meta:
        verbose_name_plural = 'Room Type 3'


class RoomType4(models.Model):
    """Model for Hotel Room Type 4"""
    room_type_name = models.CharField(max_length=50, blank=False, null=False)
    allotment = models.IntegerField(blank=True, null=True)
    room_size = models.CharField(max_length=25, blank=True, null=True)
    bed_size = models.CharField(max_length=25, blank=True, null=True)
    number_of_bed = models.IntegerField(blank=False, null=False, default=1)
    room_facilities = models.ManyToManyField(RoomFacility,
            related_name='room4_facility', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)

    # Price Info
    default_price = models.IntegerField(blank=False, null=False)

    high_season_from = models.DateField(blank=True, null=True)
    high_season_to = models.DateField(blank=True, null=True)
    high_season_price = models.IntegerField(blank=True, null=True)

    low_season_from = models.DateField(blank=True, null=True)
    low_season_to = models.DateField(blank=True, null=True)
    low_season_price = models.IntegerField(blank=True, null=True)

    special_occation_from = models.DateField(blank=True, null=True)
    special_occation_to = models.DateField(blank=True, null=True)
    special_occation_price = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.room_type_name

    class Meta:
        verbose_name_plural = 'Room Type 4'
