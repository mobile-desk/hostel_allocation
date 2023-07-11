from django.contrib import admin
from django.db import models
from .models import Student, Hostel, Room, Utilities, Complaint

# Register your models here.
#admin.site.register(Student)
admin.site.register(Hostel)

class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('room_no',)

admin.site.register(Room, RoomAdmin)

admin.site.register(Utilities)
admin.site.register(Complaint)





@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = ['remove_students_from_rooms']

    def remove_students_from_rooms(self, request, queryset):
        # Update the Student model
        queryset.update(hostel=None, room_for_student=None)

        # Update the Hostel model
        Hostel.objects.update(room_availability=models.F('total_rooms'))

        # Update the Room model
        Room.objects.update(availability=models.F('capacity'))
        for room in Room.objects.all():
            room.students_in_room.clear()

        # Update the Utilities model
        Utilities.objects.all().update(
            fan=True, bed=True, mattress=True,
            pillows=True, wardrobe=True, book_rack=True,
            tables=True, chairs=True, wall_socket=True,
            tiles=True, paint=True, window=True,
            waste_bin=True, door=True, door_lock=True,
            bulb=True, wiring=True, shower=True,
            towel_holder=True, tap=True, water_closet=True,
            TV=True, decoder=True, other=True
            )

        # Delete all objects from the Complaint model
        Complaint.objects.all().delete()

        self.message_user(request, 'Students removed from rooms and related models updated.')

    remove_students_from_rooms.short_description = 'Remove students from rooms and update related models'
