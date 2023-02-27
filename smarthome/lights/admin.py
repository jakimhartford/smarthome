from django.contrib import admin
from lights.models import Bulb, BulbType, Room
# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name',)


@admin.register(BulbType)
class BulbTypeAdmin(admin.ModelAdmin):
    list_display = ('bulb_type_name',)


@admin.register(Bulb)
class BulbAdmin(admin.ModelAdmin):
    list_display = ('bulb_name',)








