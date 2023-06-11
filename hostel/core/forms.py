from django import forms
from .models import Student, Utilities
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_pic', 'gender', 'course', 'matric_number', 'department', 'college', 'room_capacity_preference']


    # Image field
    profile_pic = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )


    #ChoiceField
    CHOICES = (
        ('female', 'Female'),
        ('male', 'Male'),
    )
    
    gender = forms.ChoiceField(
       choices=CHOICES, 
       widget=forms.Select(attrs={
        'class': 'form-control'
        }))

    #numberfield
    room_capacity_preference = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        }
        
        )
    )


    # Charfield
    course = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    matric_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    department = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    college = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )



class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Utilities
        fields = ['utility', 'note']


    #ChoiceField
    CHOICES = (
        ('fan', 'Fan'),
        ('bed', 'Bed'),
        ('mattress', 'Mattress'),
        ('pillows', 'Pillows'),
        ('wardrobe', 'Wardrobe'),
        ('book_rack', 'Book Rack'),
        ('tables', 'Tables'),
        ('chairs', 'Chairs'),
        ('wall_socket', 'Wall Socket'),
        ('tiles', 'Tiles'),
        ('paint', 'Paint'),
        ('window', 'Window'),
        ('waste_bin', 'Waste Bin'),
        ('door', 'Door'),
        ('door_lock', 'Door Lock'),
        ('bulb', 'Bulb'),
        ('wiring', 'Wiring'),
        ('shower', 'Shower'),
        ('towel_holder', 'Towel Holder'),
        ('tap', 'Tap'),
        ('water_closet', 'Water Closet'),
        ('TV', 'TV'),
        ('decoder', 'Decoder'),
        ('other', 'Others')
    )
    
    utility = forms.ChoiceField(
       choices=CHOICES, 
       widget=forms.Select(attrs={
        'class': 'form-control'
        }))
    

    # Charfield
    note = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        })
    )
