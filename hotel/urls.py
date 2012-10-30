from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'hotel.views.home'),
    url(r'^region/(?P<city>\d+)$', 'hotel.views.get_region'),
    url(r'^search/city/(?P<city>\d+)$', 'hotel.views.search'),
)
