from django.contrib import admin
from .models import Student, Hostel, Room, Utilities, Complaint

# Register your models here.
admin.site.register(Student)
admin.site.register(Hostel)

class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('room_no',)

admin.site.register(Room, RoomAdmin)

admin.site.register(Utilities)
admin.site.register(Complaint)
