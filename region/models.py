from django.db import models
from city.models import City


class Region(models.Model):
    city = models.ForeignKey(City)
    region_name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.region_name
