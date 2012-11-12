from django import forms
from geographic_info.models import City, Region


class SearchForm(forms.Form):
    STAR_CHOICES = (('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'))

    city = forms.ModelChoiceField(label='City', required=True,
            queryset=City.objects.all(),
            widget=forms.Select(attrs={'onchange': 'FilterModel();'}))
    date = forms.DateTimeField(label='Date',
            widget=forms.TextInput(attrs={'placeholder': 'dd-mm-yyyy'}))
    region = forms.ModelChoiceField(label='Region', required=False,
            queryset=Region.objects.all(),
            widget=forms.Select(attrs={'disabled': '', 'multiple': '',
                'name': 'region[]'}))
    stars = forms.ChoiceField(label='Stars', widget=forms.Select,
            choices=STAR_CHOICES)
    price = forms.IntegerField(label='Price',
            widget=forms.TextInput(attrs={'placeholder': '250000'}))
