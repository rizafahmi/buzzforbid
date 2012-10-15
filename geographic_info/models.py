from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.name


class City(models.Model):
    city = models.CharField(max_length=50, unique=True, blank=False, null=False)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.city

    class Meta:
        verbose_name_plural = 'Cities'


class Region(models.Model):
    city = models.ForeignKey(City)
    region_name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.region_name
