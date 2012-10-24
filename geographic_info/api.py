from tastypie.resources import ModelResource
from geographic_info.models import City


class CityResource(ModelResource):
    class Meta:
        queryset = City.objects.all()
        resource_name = 'city'
