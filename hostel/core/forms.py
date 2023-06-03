from django import forms
from .models import Student
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



