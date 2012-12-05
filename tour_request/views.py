from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from tour_request.models import Request
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from geographic_info.models import City
import pprint


pp = pprint.PrettyPrinter(indent=4)


def newRequest(request):
    tour_request = ''
    cities = City.objects.all()
    if request.POST:
        print request.POST

    return render_to_response('tour_request/new.html',
            {'tour_request': tour_request, 'cities': cities},
            context_instance=RequestContext(request))


def editRequest(request, request_id):
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
                html_content = """Sorry, your request has been rejected. Try again soon ya!<br /><br />
                This is your rejected request:<br /><br />"""
                html_content = html_content + "Destination(s): "
                for req in tour_request.destinations.all():
                    html_content = html_content + str(req.city) + ", "

                html_content = html_content + "<br />Date: " + str(tour_request.date)
                html_content = html_content + "<br />Duration(s): " + str(tour_request.duration)
                html_content = html_content + "<br />Adult: " + str(tour_request.adult)
                html_content = html_content + "<br />Child: " + str(tour_request.child)
                html_content = html_content + "<br />Airplane: " + str(tour_request.airplane)
                html_content = html_content + "<br />Accomodation: " + str(tour_request.accomodation)
                html_content = html_content + "<br />Special Request: " + str(tour_request.special_request)
                html_content = html_content + "<br />Min. Price: " + str(tour_request.price)

            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

    return render_to_response('tour_request/index.html',
            {'tour_request': tour_request},
            context_instance=RequestContext(request))
