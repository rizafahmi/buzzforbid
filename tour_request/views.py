from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from tour_request.models import Request
from django.core.mail import EmailMultiAlternatives
import pprint


pp = pprint.PrettyPrinter(indent=4)


def editrequest(request, request_id):
    if request_id:
        tour_request = get_object_or_404(Request, pk=request_id)

        if request.POST:
            if request.POST.get('acceptButton'):
                status = 'accepted'
            else:
                status = 'rejected'

            tour_request.status = status
            tour_request.save()

            # send email to user directly : Temporary attemp only!
            if status == 'accepted':
                subject, from_email, to = 'Buzzforbid: Your Tour Request Has Accepted!', 'tour@buzzforbid.com', tour_request.user.email
                html_content = 'Congratulations, your request has been accepted!'
            else:
                subject, from_email, to = 'Buzzforbid: Your Tour Request Has Rejected!', 'tour@buzzforbid.com', tour_request.user.email
                html_content = 'Sorry, your request has been rejected. Try again soon ya!'
            text_content = html_content
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

    return render_to_response('tour_request/index.html',
            {'tour_request': tour_request},
            context_instance=RequestContext(request))
