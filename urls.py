from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from hotel.api import HotelResource
from geographic_info.api import CityResource

hotel_resource = HotelResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buzzforbid.views.home', name='home'),
    # url(r'^buzzforbid/', include('buzzforbid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    # API
    url(r'^api/', include(hotel_resource.urls)),
    url(r'^api/', include(CityResource().urls)),
)
