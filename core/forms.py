from django import forms
from .models import Student, Utilities
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_pic', 'gender', 'college', 'matric_number', 'department', 'room_capacity_preference']


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



    COLLEGECHOICES = (
        ('college of medical and health sciences', 'College of Medical and Health Sciences'),
        ('college of natural and applied sciences', 'College of Natural and Applied Sciences'),
        ('college of management and social sciences', 'College of Management and Social Sciences'),
        ('college of law', 'College of Law'),
        ('college of computing and telecommunication', 'College of Computing and Telecommunication'),
    )

    college = forms.ChoiceField(
       choices=COLLEGECHOICES, 
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
  

    matric_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )



    

    COURSECHOICES = (
        ('medicine and surgery', 'Medicine and Surgery'), 
        ('dentistry', 'Dentistry'), 
        ('pharmacy', 'Pharmacy'), 
        ('optometry', 'Optometry'), 
        ('nursing', 'Nursing'),
        ('medical laboratory science', 'Medical Laboratory Science'),
        ('pharmacology', 'Pharmacology'),
        ('anatomy', 'Anatomy'),
        ('physiology', 'Physiology'),
        ('public and community health', 'Public and Community Health'),
        ('energy and petroleum studies', 'Energy and Petroleum Studies'), 
        ('petrochemical and industrial chemistry', 'Petrochemical and Industrial Chemistry'),
        ('chemistry', 'Chemistry'),
        ('biochemistry', 'Biochemistry'),
        ('microbiology', 'Microbiology'),
        ('intelligence and security studies', 'Intelligence and Security Studies'),
        ('international relations and strategic studies', 'International Relations and Strategic Studies'),
        ('business administration', 'Business Administration'),
        ('public administration', 'Public Administration'),
        ('political science', 'Political Science'),
        ('sociology', 'Sociology'),
        ('marketing', 'Marketing'),
        ('mass communication', 'Mass Communication'),
        ('accounting', 'Accounting'),
        ('economics', 'Economics'),
        ('finance', 'Finance'),
        ('ll.b. law', 'LL.B. Law'),
        ('computer science', 'Computer Science')
    )

    department = forms.ChoiceField(
       choices=COURSECHOICES, 
       widget=forms.Select(attrs={
        'class': 'form-control'
        }))


        


    






 



            



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
