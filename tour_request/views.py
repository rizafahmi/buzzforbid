from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from tour_request.models import Request
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
import pprint
from tour_request.forms import NewRequestForm, CounterRequestForm
from tour_request.models import UserNotification, CounterRequest as CounterRequestModel


pp = pprint.PrettyPrinter(indent=4)


def new_notification_count(user):
    return UserNotification.objects.filter(user__username=user,
            status='unread').count()


@login_required
def newRequest(request):
    notification = UserNotification.objects.filter(user__username=request.user).order_by('id')

    if request.POST:
        form = NewRequestForm(request.POST)
        print form
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = NewRequestForm()

    return render_to_response('tour_request/new.html',
        {'form': form,
            'notification': notification,
            'notification_count': new_notification_count(request.user),
            },
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


@login_required
def ViewRequest(request, request_id):
    if request_id:
        tour_request = get_object_or_404(Request, pk=request_id)

    return render_to_response('tour_request/view_request.html',
            {'form': tour_request},
            context_instance=RequestContext(request))


@login_required
def CounterRequest(request):
    if request.POST:
        form = CounterRequestForm(request.POST)
        print form
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = CounterRequestForm()

    return render_to_response('tour_request/counter.html',
        {'form': form},
        context_instance=RequestContext(request))


@login_required
def ViewCounterRequest(request, counter_id):
    if counter_id:
        counter = get_object_or_404(CounterRequestModel, pk=counter_id)

    return render_to_response('tour_request/view_counter.html',
            {'form': counter},
        context_instance=RequestContext(request))


@login_required
def CounterList(request):
    counters = CounterRequestModel.objects.filter(user=request.user)
    return render_to_response('tour_request/counter_list.html',
            {'counters': counters,
            'notification_count': new_notification_count(request.user)},
        context_instance=RequestContext(request))


@login_required
def home(request):

    notification = UserNotification.objects.filter(user__username=request.user).order_by('id')
    return render_to_response('tour_request/home.html',
        {'requests': Request.objects.filter(user=request.user),
            'notification': notification,
            'notification_count': new_notification_count(request.user),
            },
        context_instance=RequestContext(request))
