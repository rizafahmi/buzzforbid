from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)

    def __unicode__(self):
        """docstring for __unicode__"""
        return self.name
