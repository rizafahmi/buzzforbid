from tastypie.resources import ModelResource, ALL
from tastypie import fields
from geographic_info.models import City, Region


class CityResource(ModelResource):
    regions = fields.ToManyField('geographic_info.api.RegionResource', 'city_region')

    class Meta:
        queryset = City.objects.all()
        resource_name = 'city'


class RegionResource(ModelResource):
    city = fields.ToOneField(CityResource, 'city', full=True)

    class Meta:
        queryset = Region.objects.all()
        resource_name = 'region'
#
#         filtering = {
#                 'region_name': ALL,
#                 }
