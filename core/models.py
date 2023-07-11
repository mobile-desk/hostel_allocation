from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete


# Create your models here.

#student model
class Student(models.Model):
    STATUS_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to ='images/thumbnail/', default="default.png", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=STATUS_CHOICES)
    matric_number = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    room_capacity_preference = models.PositiveIntegerField()
    hostel = models.ForeignKey('Hostel', on_delete=models.SET_NULL, null=True, blank=True)
    room_for_student = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, blank=True)
    


    def __str__(self):
        return str(self.user)

#hostel model
class Hostel(models.Model):
    STATUS_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    hostel_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=STATUS_CHOICES)
    total_rooms = models.PositiveIntegerField()
    room_availability = models.PositiveIntegerField()
    room_capacity = models.PositiveIntegerField()


    def __str__(self):
        return str(self.hostel_name)
    
    def save(self, *args, **kwargs):
        if self.room_availability > self.total_rooms:
            self.room_availability = self.total_rooms
        super().save(*args, **kwargs)



#room model
class Room(models.Model):
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)
    room_no = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    availability = models.PositiveIntegerField()
    students_in_room = models.ManyToManyField(User, blank=True)


    def __str__(self):
        return str(self.hostel) + '|' + str(self.capacity) + '|' + str(self.room_no)
    
   


@receiver(post_save, sender=Hostel)
def create_rooms(sender, instance, created, **kwargs):
    if created:
        total_rooms = instance.total_rooms

        # Create rooms based on total_rooms
        for room_no in range(1, total_rooms + 1):
            room = Room.objects.create(
                hostel=instance,
                room_no=room_no,
                capacity=instance.room_capacity,
                availability=instance.room_capacity
            )
            room.save()


class Utilities(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    fan = models.BooleanField(default=True) 
    bed = models.BooleanField(default=True)
    mattress = models.BooleanField(default=True)
    pillows = models.BooleanField(default=True)
    wardrobe = models.BooleanField(default=True)
    book_rack = models.BooleanField(default=True)
    tables = models.BooleanField(default=True)
    chairs = models.BooleanField(default=True)
    wall_socket = models.BooleanField(default=True)
    tiles = models.BooleanField(default=True)
    paint = models.BooleanField(default=True)
    window = models.BooleanField(default=True)
    waste_bin = models.BooleanField(default=True)
    door = models.BooleanField(default=True)
    door_lock = models.BooleanField(default=True)
    bulb = models.BooleanField(default=True)
    wiring = models.BooleanField(default=True)
    shower = models.BooleanField(default=True)
    towel_holder = models.BooleanField(default=True)
    tap = models.BooleanField(default=True)
    water_closet = models.BooleanField(default=True)
    TV = models.BooleanField(default=True)
    decoder = models.BooleanField(default=True)
    other = models.BooleanField(default=True)

    def __str__(self):
        return "utilities" + '|' + str(self.room)
    

    @receiver(post_save, sender=Room)
    def create_utilities(sender, instance, created, **kwargs):
        if created:
            Utilities.objects.create(room=instance)



class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    utility = models.CharField(max_length=100)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.utility} - {self.room} - {self.created_at}"
    


@receiver(pre_delete, sender=Complaint)
def handle_complaint_delete(sender, instance, **kwargs):
    utilities = Utilities.objects.filter(room=instance.room)
    for util in utilities:
        setattr(util, instance.utility, True)
        util.save()