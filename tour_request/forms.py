from django import forms
from tour_request.models import Request


class EditRequestForm(forms.ModelForm):
    # STATUS_CHOICES = (('unread', 'Unread'),
    #     ('accepted', 'Accepted'),
    #     ('expired', 'Expired'),
    #     ('rejected', 'Rejected'),
    #     )
    # # destinations
    # date = forms.DateTimeField(label='Date',
    #         widget=forms.TextInput())
    # duration = forms.TextInput()
    # adult = forms.TextInput()
    # child = forms.TextInput()
    # airplane = forms.BooleanField()
    # accomodation = forms.BooleanField()
    # special_request = forms.TextInput()
    # price = forms.TextInput()
    # status = forms.ChoiceField(label='Status', widget=forms.Select,
    #         choices=STATUS_CHOICES)
    print Request

    class Meta:
        model = Request
