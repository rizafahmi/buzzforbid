from django.core.management.base import NoArgsCommand
from tour_request.models import Request


class SendMail(NoArgsCommand):
    def send_mail(self, **options):
        print "sending mail..."
