from hotel.models import (Hotel, Facility, HotelManagerUser, HotelSupervisorUser,
HotelUser)
from django.contrib import admin

admin.site.register(Hotel)
admin.site.register(Facility)
admin.site.register(HotelManagerUser)
admin.site.register(HotelSupervisorUser)
admin.site.register(HotelUser)
