from tastypie.resources import ModelResource
from hotel.models import Hotel
from django.conf.urls.defaults import url


class HotelResource(ModelResource):
    class Meta:
        queryset = Hotel.objects.all()
        resource_name = 'hotel'


class SearchHotelResource(ModelResource):
    class Meta:
        queryset = Hotel.objects.all()
        resource_name = 'search_hotel'

    # def dehydrate(self, bundle):
    #     bundle.data['something'] = "Beatles"
    #     return bundle

    def override_urls(self):
        # return [
        #     url(r"^(?P<resource_name>%s/city/(?P<city_id>[\d])/%s$" % (self._meta.resource_name, self.wrap_view('search_all')), name='api_search_all', ),
        # ]
        return [
            url(r"^(?P<resource_name>%s)/city/(?P<city_id>[\d]+)/?format=json$"
                % self._meta.resource_name, self.wrap_view('search_all'),
                name="api_search_all"),
        ]

    def search_all(self, request, **kwargs):
        return HotelResource()
