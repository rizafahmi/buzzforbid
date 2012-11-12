from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'hotel.views.home'),
    url(r'^region/(?P<city>\d+)$', 'hotel.views.get_region'),
    url(r'^search/city/(?P<city>\d+)/checkin/(?P<checkin>.+)/checkout/(?P<checkout>.+)/region/(?P<region>.+)/star/(?P<star>\d+)/price/(?P<price>\d+)/qty/(?P<qty>\d+)$', 'hotel.views.search'),
)
