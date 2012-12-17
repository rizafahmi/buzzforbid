from django import template
from tour_request.models import CounterRequest

register = template.Library()


def count_counter(value):
    return CounterRequest.objects.filter(origin_request=value).count()

register.filter('count_counter', count_counter)
