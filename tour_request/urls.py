from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^id/(?P<request_id>\d+)$', 'tour_request.views.editrequest'),
)
