from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    profile = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=75, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.name
