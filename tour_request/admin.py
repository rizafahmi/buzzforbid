from tour_request.models import Request
from django.contrib import admin


class RequestAdmin(admin.ModelAdmin):
    list_display = ('date', 'duration', 'price', 'user', 'status', 'created')

admin.site.register(Request, RequestAdmin)
