from tour_request.models import Request
from travel_agent.models import Agent

from django.core.management.base import NoArgsCommand
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Command(NoArgsCommand):
    requires_model_validation = False
    can_import_settings = True

    def handle_noargs(self, **options):
        for agent in Agent.objects.all():
            # print "TO: " + agent.email,
            # print "\nContent: "

            requests = Request.objects.filter(status='unread')
                # compile the html
            subject, from_email, to = 'Buzzforbid Tour Summary', 'iloveschool@iyaa.com', agent.email

            html_content = render_to_string("template.html", {'requests': requests,
                'name': agent.name})
            text_content = strip_tags(html_content)

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

                # print content
