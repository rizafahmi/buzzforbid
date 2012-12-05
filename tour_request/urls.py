from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^new/+$', 'tour_request.views.newRequest'),
    url(r'^id/(?P<request_id>\d+)$', 'tour_request.views.editRequest'),
)
