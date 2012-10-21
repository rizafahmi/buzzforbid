from room_type.models import RoomType1, RoomType2, RoomType3, RoomType4, RoomFacility
from django.contrib import admin


class RoomType(admin.ModelAdmin):
    app_label = 'Room Types'

admin.site.register(RoomType1, RoomType)
admin.site.register(RoomType2)
admin.site.register(RoomType3)
admin.site.register(RoomType4)
admin.site.register(RoomFacility)
