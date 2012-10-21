from hotel.models import Hotel, Facility
from django.contrib import admin


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'city', 'region', 'province', 'phone_number',
            'receptionist')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Facility)
