from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to ='images/thumbnail/', default="default.png", null=True, blank=True)
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=100)
    matric_number = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    room_capacity_preference = models.PositiveIntegerField()
    hostel = models.ForeignKey('Hostel', on_delete=models.SET_NULL, null=True)
    room_for_student = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, blank=True)
    


    def __str__(self):
        return str(self.user)

#hostel model
class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    total_rooms = models.PositiveIntegerField()
    room_availability = models.PositiveIntegerField()


    def __str__(self):
        return str(self.hostel_name)


#room model
class Room(models.Model):
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)
    room_no = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    availability = models.PositiveIntegerField()
    students_in_room = models.ManyToManyField(User, blank=True)


    def __str__(self):
        return str(self.hostel) + '|' + str(self.capacity) + '|' + str(self.room_no)



class Utilities(models.Model):
    room = models.ForeignKey('Hostel', on_delete=models.CASCADE)
    fan = models.BooleanField 
    bed = models.BooleanField
    mattress = models.BooleanField
    pillows = models.BooleanField
    wardrobe = models.BooleanField
    book_rack = models.BooleanField
    tables = models.BooleanField
    chairs = models.BooleanField
    wall_socket = models.BooleanField
    tiles = models.BooleanField
    paint = models.BooleanField
    window = models.BooleanField
    waste_bin = models.BooleanField
    door = models.BooleanField
    door_lock = models.BooleanField
    bulb = models.BooleanField
    wiring = models.BooleanField
    shower = models.BooleanField
    towel_holder = models.BooleanField
    tap = models.BooleanField
    water_closet = models.BooleanField
    TV = models.BooleanField
    decoder = models.BooleanField
    other = models.BooleanField