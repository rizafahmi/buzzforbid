from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.name


class Country(models.Model):
    country = models.CharField(max_length=100, unique=True, blank=False, null=False)
    shortname = models.CharField(max_length=5, unique=True, blank=True, null=True)

    def __unicode__(self):
        return self.country


class City(models.Model):
    city = models.CharField(max_length=50, unique=True, blank=False, null=False)
    country = models.ForeignKey(Country, related_name='city_country')

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.city

    class Meta:
        verbose_name_plural = 'Cities'


class Region(models.Model):
    city = models.ForeignKey(City, related_name='city_region')
    region_name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.region_name
