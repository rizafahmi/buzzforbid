from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tour_request.views.home', name='home'),
    url(r'^new/+$', 'tour_request.views.newRequest', name='new_request'),
    url(r'^counter/+$', 'tour_request.views.CounterRequest', name='counter_request'),
    url(r'^counter/(?P<counter_id>\d+)/+$',
        'tour_request.views.ViewCounterRequest',
        name='view_counter_request'),
    url(r'^counter_list/+$', 'tour_request.views.CounterList',
        name='counter_list'),
    url(r'^id/(?P<request_id>\d+)$', 'tour_request.views.editRequest'),
    url(r'^view_request/(?P<request_id>\d+)$', 'tour_request.views.ViewRequest'),
)
