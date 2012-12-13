from django.db import models

from geographic_info.models import City
from django.contrib.auth.models import User


class Request(models.Model):

    STATUS_CHOICES = (('unread', 'Unread'),
            ('read', 'Read'),
            ('accepted', 'Accepted'),
            ('expired', 'Expired'),
            ('rejected', 'Rejected'),
            )

    destinations = models.ManyToManyField(City, related_name='destination',
            blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    duration = models.IntegerField(default=2)
    adult = models.IntegerField(default=1)
    child = models.IntegerField(default=0)
    airplane = models.BooleanField(default=True)
    accomodation = models.BooleanField(default=False)
    special_request = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=25, blank=True, null=True,
            choices=STATUS_CHOICES, default='unread')
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    # Metadata
    created = models.DateTimeField(auto_now=True, auto_now_add=True)
    user = models.ForeignKey(User, related_name='request_user')

    def __unicode__(self):
        return str(self.id) + ' -- ' + str(self.created)


class CounterRequest(models.Model):
    DEPARTURE_CHOICES = (('daily', 'Daily'),
            ('nightly', 'Nightly?'),
        )

    # Relation
    origin_request = models.ForeignKey(Request, related_name='counter_request_request')

    destinations = models.ManyToManyField(City, related_name='counter_destination',
            blank=True, null=True)
    date = models.DateField()
    duration = models.IntegerField(default=2)
    adult = models.IntegerField(default=1)
    child = models.IntegerField(default=0)
    airplane = models.BooleanField(default=True)
    airplane_type = models.CharField(max_length=50, blank=True, null=True)
    accomodation = models.BooleanField(default=False)
    accomodation_desc = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0)
    tour_detail = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True)
    departure = models.CharField(max_length=50, blank=False, null=False,
            choices=DEPARTURE_CHOICES, default='daily')
    terms_conditions = models.TextField(blank=True, null=True)

    # Metadata
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    user = models.ForeignKey(User, related_name='counter_user')

    def save(self, *args, **kwargs):
        # Call the real save
        super(CounterRequest, self).save(*args, **kwargs)

        # Add message to user
        notification = UserNotification(user=self.user,
                subject="Your Request Has Been Countered!",
                message="Congrats! Your request has been Countered!",
                status='unread')
        notification.save()


class UserNotification(models.Model):

    STATUS_CHOICES = (('unread', 'Unread'),
            ('read', 'Read'),
            ('new', 'New'),
            )
    user = models.ForeignKey(User, related_name='notification_user')

    subject = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    status = models.CharField(max_length=10, blank=False, null=False,
            choices=STATUS_CHOICES, default='unread')
