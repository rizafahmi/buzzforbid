from tour_request.models import Request, CounterRequest, UserNotification
from django.contrib import admin


class RequestAdmin(admin.ModelAdmin):
    list_display = ('date', 'duration', 'price', 'user', 'status', 'created',)


class CounterRequestAdmin(admin.ModelAdmin):
    list_display = ('origin_request',)


class UserNotificationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Request, RequestAdmin)
admin.site.register(CounterRequest, CounterRequestAdmin)
admin.site.register(UserNotification, UserNotificationAdmin)
