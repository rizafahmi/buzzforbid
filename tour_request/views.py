from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from tour_request.models import Request
from tour_request.forms import EditRequestForm


def editrequest(request, request_id):
    if request.POST:
        pass

    if request_id:
        article = get_object_or_404(Request, pk=request_id)

    return render_to_response('index.html',
            {'form': EditRequestForm(instance=article)},
            context_instance=RequestContext(request))
