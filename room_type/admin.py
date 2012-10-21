from room_type.models import RoomType1, RoomType2, RoomType3, RoomType4, RoomFacility
from django.contrib import admin


class RoomTypeAdmin(admin.ModelAdmin):
    # app_label = 'Room Types'
    list_display = ('room_type_name', 'allotment', 'room_size', 'bed_size',
            'default_price', 'get_facilities', )

admin.site.register(RoomType1, RoomTypeAdmin)
admin.site.register(RoomType2, RoomTypeAdmin)
admin.site.register(RoomType3, RoomTypeAdmin)
admin.site.register(RoomType4, RoomTypeAdmin)
admin.site.register(RoomFacility)
