from django.forms import ModelForm
from tour_request.models import Request, CounterRequest


class NewRequestForm(ModelForm):
    class Meta:
        model = Request


class CounterRequestForm(ModelForm):
    class Meta:
        model = CounterRequest
