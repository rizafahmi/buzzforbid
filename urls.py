from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from hotel.api import HotelResource, SearchHotelResource
from geographic_info.api import CityResource, RegionResource

urlpatterns = patterns('',
    url(r'^hotel/', include('hotel.urls')),
    url(r'^tour_request/', include('tour_request.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),


    # API
    # url(r'^api/search/', include(SearchHotelResource().urls)),
    url(r'^api/', include(HotelResource().urls)),
    url(r'^api/', include(CityResource().urls)),
    url(r'^api/', include(RegionResource().urls)),
)

urlpatterns += staticfiles_urlpatterns()
