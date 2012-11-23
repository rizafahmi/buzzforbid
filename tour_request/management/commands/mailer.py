from tour_request.models import Request
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    requires_model_validation = False
    can_import_settings = True

    def handle_noargs(self, **options):
        for request in Request.objects.all():
            print request.user.email
