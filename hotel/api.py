from tastypie.resources import ModelResource
from hotel.models import Hotel


class HotelResource(ModelResource):
    class Meta:
        queryset = Hotel.objects.all()
        resource_name = 'hotel'
