from django.forms import ModelForm
from tour_request.models import Request


class NewRequestForm(ModelForm):
    class Meta:
        model = Request
