from django.shortcuts import render, redirect
from email import message
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from hostel import settings
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Hostel, Room
from .forms import ProfileForm
from django.urls import reverse_lazy


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user_profile = Student.objects.filter(user=request.user).first()
        
        has_profile = user_profile is not None

        if has_profile:
            profile = Student.objects.get(user=request.user)
            return render(request, 'home.html', {'has_profile': has_profile, 'profile': profile})
        else:
            return render(request, 'home.html', {'has_profile': has_profile})
    
    else:
        return render(request, 'home.html')


#student 
def create_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('home')
        else:
            form = ProfileForm()
        return render(request, 'uploadprof.html', {'form': form})
    else:
        return render(request, '404.html')



#authentication
def signup(request):
    
    
    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    
        if User.objects.filter(username=username):
            messages.error(request, "Matric Number already exists")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already exists")
            return redirect('home')
        
         
        if password != password2:
            messages.error(request, "Passwords do not match!")  
            return redirect('home')
         

    
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        
        
        myuser.save()    
        
        messages.success(request, "Your Account has been created successfully.")
        return redirect('signin')  
        
       
    
    return render(request, 'signup.html')


def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('home')
            
        else:
            messages.error(request, "Login Error")
            return redirect('home')    
    
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out ")
    return redirect('home')



#allocation

def allocate_hostel(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Student.objects.get(user=user)
        gender = profile.gender
        capacity_pref = profile.room_capacity_preference
        hostels = Room.objects.filter(hostel__gender=gender).order_by('capacity')
        
        allocated_hostel = None
        allocated_room = None

        for hostel in hostels:
            if hostel.availability > 0 and hostel.capacity == capacity_pref:
                allocated_hostel = hostel.hostel
                allocated_room = hostel
                break
            elif hostel.availability > 0 and hostel.capacity <= capacity_pref:
                allocated_hostel = hostel.hostel
                allocated_room = hostel
                break
            elif hostel.availability > 0 and hostel.capacity >= capacity_pref:
                allocated_hostel = hostel.hostel
                allocated_room = hostel
                break
            else:
                pass

        if allocated_hostel and allocated_room:
            profile.hostel = allocated_hostel
            profile.room_for_student = allocated_room
            allocated_room.students_in_room.add(user)
            allocated_room.availability -= 1
            allocated_room.save()

            if allocated_room.availability == 0:
                allocated_room.hostel.room_availability -= 1
                allocated_room.hostel.save()

            profile.save()
            return redirect('home')

        return render(request, 'profile.html', {'profile': profile, 'allocated_hostel': allocated_hostel, 'allocated_room': allocated_room})
    else:
        return render(request, '404.html')